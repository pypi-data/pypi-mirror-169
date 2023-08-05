#!/usr/bin/env python
# Author: ASU --<andrei.suiu@gmail.com>

from glob import glob
from pathlib import Path
from typing import List, Literal

import numpy as np
import pandas as pd
import yfinance as yf
from keras import activations
from keras import backend as K
from keras import layers, Model
from keras.losses import mean_squared_error, Loss
from keras.optimizer_v2.adam import Adam
from pydantic import PositiveInt, conint
from sklearn.preprocessing import MinMaxScaler
from tensorflow import Tensor
from tsx import TS

from keras_generators.encoders import ScaleEncoder
from keras_generators.generators import TimeseriesDataSource, TimeseriesTargetsParams, DataSet, XYBatchGenerator, \
    TensorDataSource, TargetTimeseriesDataSource
from keras_generators.model_abstractions.model_object import SimpleModelObject
from keras_generators.model_abstractions.model_params import ModelParams
from keras_generators.splitters import OrderedSplitter


class LSTMModelParams(ModelParams):
    input_symbols: List[str]
    target_symbol_idx: int  # index in the above array of symbols
    start_ts: TS
    stop_ts: TS
    lookback: PositiveInt
    pred_len: PositiveInt = 1  # should be higher than n_true_trends
    delay: conint(ge=0) = 0
    seq_input_name: str = "seq"
    target_name: str = "target"
    max_epochs: PositiveInt = 5
    lstm_dropout: float = 0.2
    rnn_type: Literal["RNN", "LSTM", "GRU", "DENSE"] = "LSTM"
    use_cuDNN: bool = True
    lstm_rec_dropout: float = 0.1
    lstm_units: PositiveInt = 20
    bidirectional: bool = False

    @property
    def out_dim(self):
        return 2


def trading_loss(y_true: Tensor, y_pred: Tensor):
    pred_price = K.cast(y_pred[:, 0], dtype="float32")
    prev_price = K.cast(y_true[:, 0], dtype="float32")
    true_price = K.cast(y_true[:, 1], dtype="float32")

    long_sign = K.sign(pred_price - prev_price)
    roi = long_sign * (true_price - pred_price)
    return K.mean(-roi)


def mse_custom_loss(y_true: Tensor, y_pred: Tensor):
    pred_price = K.cast(y_pred[:, 0], dtype="float32")
    true_price = K.cast(y_true[:, 1], dtype="float32")

    return mean_squared_error(true_price, pred_price)


def simple_lstm_model_factory(mp: LSTMModelParams):
    """
    This is a factory function that creates a model object for the LSTM model.
    """
    input_tensor = layers.Input(shape=(mp.lookback, len(mp.input_symbols)), name=mp.seq_input_name)
    model_inputs = input_tensor

    if mp.rnn_type.upper() == "DENSE":
        d_l = layers.Flatten()(model_inputs)
    else:
        recurrent_args = dict(dropout=mp.lstm_dropout, kernel_initializer="glorot_normal", bias_initializer="zero")
        if mp.rnn_type.upper() == "LSTM":
            rnn_layer_type = layers.LSTM
            recurrent_args["recurrent_activation"] = "sigmoid"
        elif mp.rnn_type.upper() == "GRU":
            rnn_layer_type = layers.GRU
            recurrent_args["recurrent_activation"] = "sigmoid"
        elif mp.rnn_type.upper() == "RNN":
            rnn_layer_type = layers.SimpleRNN
        else:
            raise ValueError(f"Unknown rnn_type: {mp.rnn_type}")

        if mp.use_cuDNN:
            recurrent_args["activation"] = "tanh"
            recurrent_args["recurrent_dropout"] = 0
            recurrent_args["unroll"] = False
            recurrent_args["use_bias"] = True
        else:
            recurrent_args["activation"] = "selu"
            recurrent_args["recurrent_dropout"] = mp.lstm_rec_dropout

        rnn_layer = rnn_layer_type(mp.lstm_units, **recurrent_args)
        if mp.bidirectional:
            rnn1 = layers.Bidirectional(rnn_layer)(model_inputs)
        else:
            rnn1 = rnn_layer(model_inputs)
        d_l = rnn1

    output_tensor = layers.Dense(mp.out_dim, )(d_l)

    output_tensor = layers.Activation(activations.sigmoid, name=mp.target_name)(output_tensor)

    model_name = f"{['', 'bi'][mp.bidirectional]}{mp.rnn_type}{mp.lstm_units}"
    model = Model(inputs=model_inputs, outputs=output_tensor, name=model_name)
    # metrics = ['mse', 'mae']
    # loss = mse_custom_loss
    loss = trading_loss
    metrics = [trading_loss, mse_custom_loss]
    model.compile(optimizer=Adam(learning_rate=mp.learning_rate), loss=loss, metrics=metrics)
    return model


if __name__ == '__main__':
    _mp = LSTMModelParams(
        input_symbols=["BRK-A", "GOOG"],
        target_symbol_idx=0,
        start_ts=TS("2010-01-01"), stop_ts=TS("2021-08-01"),
        lookback=60,
        batch_size=2048,
        max_epochs=50,
        learning_rate=0.001,
    )
    close_prices_by_symbol = {}
    for symbol in _mp.input_symbols:
        ticker_df = yf.download(symbol, start=_mp.start_ts.as_iso_date, end=_mp.stop_ts.as_iso_date, interval="1d")
        close_inputs = ticker_df['Close']
        close_prices_by_symbol[symbol] = close_inputs

    input_df = pd.DataFrame(close_prices_by_symbol)
    target_symbol = _mp.input_symbols[_mp.target_symbol_idx]
    target_close_prices = close_prices_by_symbol[target_symbol]
    target_df = pd.DataFrame(target_close_prices)

    target_params = TimeseriesTargetsParams(delay=_mp.delay, pred_len=_mp.pred_len, stride=1,
                                            target_idx=_mp.target_symbol_idx)

    price_input_ds = TimeseriesDataSource(name=_mp.seq_input_name, tensors=input_df.values, length=_mp.lookback,
                                          target_params=target_params)
    scaled_price_input_ds = price_input_ds.fit_encode([ScaleEncoder(MinMaxScaler())])

    next_price_ds = TargetTimeseriesDataSource.from_timeseries_datasource(scaled_price_input_ds, name=_mp.target_name)
    last_price_na = scaled_price_input_ds.select_features([_mp.target_symbol_idx])[:][:, -1]
    last_price_ds = TensorDataSource(name=_mp.target_name, tensors=last_price_na, encoders=next_price_ds.get_encoders())

    targets_ds = last_price_ds + next_price_ds

    dataset = DataSet(input_sources={_mp.seq_input_name: scaled_price_input_ds},
                      target_sources={_mp.target_name: targets_ds})
    train_ds, val_ds, test_ds = dataset.split(splitter=OrderedSplitter(train=0.6, val=0.2))
    train_gen = XYBatchGenerator(train_ds.input_sources, train_ds.target_sources, batch_size=_mp.batch_size)
    val_gen = XYBatchGenerator(val_ds.input_sources, val_ds.target_sources, batch_size=_mp.val_batch_size)
    test_gen = XYBatchGenerator(test_ds.input_sources, test_ds.target_sources, batch_size=_mp.val_batch_size)

    model = simple_lstm_model_factory(_mp)
    model_object = SimpleModelObject(mp=_mp, model=model, encoders=train_ds.get_encoders())
    model_dir = SimpleModelObject.construct_model_dir(name=model.name, base_dir="model-data")
    history = model_object.train(train_gen, val_gen, device="/CPU:0", model_dir=model_dir)
    all_epochs = glob(str(model_dir / "*.hdf5"))
    last_hdf5 = all_epochs[-1]
    new_model_obj = SimpleModelObject.from_model_dir(Path(last_hdf5), model_params_cls=_mp.__class__, device="/CPU:0",
                                                     custom_classes=[trading_loss, mse_custom_loss])
    metrics = new_model_obj.model.evaluate(test_gen)
    result_ds = new_model_obj.predict(test_gen.get_X_generator(), device="/CPU:0")
    result_ds = result_ds.select_features([0])
    true_pred = np.concatenate((test_gen.targets['target'].decode()[:], result_ds[:]), axis=1)
    true_pred = true_pred[:, [1, 2]]
    print(true_pred)
    print(metrics)
