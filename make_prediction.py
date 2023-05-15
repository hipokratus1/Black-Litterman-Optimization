import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from messari.messari import Messari
from sklearn.model_selection import train_test_split
from statsmodels.tsa.stattools import adfuller as adf
from statsmodels.tsa.arima.model import ARIMA
import warnings
import numpy as np


def make_predict(coin):
    messari = Messari()
    assets = [coin]
    metric = 'price'
    start = '2020-05-01'
    end = '2023-05-01'
    df = messari.get_metric_timeseries(asset_slugs=assets, asset_metric=metric, start=start, end=end)
    df = df[coin]

    period = 7
    dates = df.reset_index()['timestamp'].tolist()
    close = df['close'].tolist()
    train, test = train_test_split(close, test_size=period, shuffle=False)
    train_dates, test_dates = train_test_split(dates, test_size=period, shuffle=False)
    train, val = train_test_split(train, test_size=period, shuffle=False)
    train_dates, val_dates = train_test_split(train_dates, test_size=period, shuffle=False)

    d = 0
    if adf(train)[1] >= 0.05:
        d = 1

    p_values = range(0, 6)
    q_values = range(0, 15)
    best_rmse = np.inf
    arima_order = (0, 0, 0)

    for p in p_values:
        for q in q_values:
            warnings.filterwarnings("ignore")
            order = (p,d,q)
            model_ = ARIMA(train, order=order).fit()
            y_pred_ = model_.forecast(period)
            rmse = mean_squared_error(val, y_pred_, squared=False)
            if rmse < best_rmse:
                best_rmse = rmse
                arima_order = order
    
    model_ = ARIMA(close, order=arima_order).fit()
    pred = model_.forecast(period)
    last_pred = pred[-1]
    change_pred = (last_pred - close[-1]) / close[-1] * 100
    return change_pred