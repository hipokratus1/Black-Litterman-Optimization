import numpy as np
from messari.messari import Messari
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from statsmodels.tsa.stattools import adfuller as adf
from statsmodels.tsa.arima.model import ARIMA
import warnings

def is_valid_coin(coin):
    try:
        Messari().get_asset(asset_slugs=[coin])
    except:
        return False
    return True

def make_predict(coin, start='2020-05-01', end='2023-05-01', period=7):
    messari = Messari()
    assets = [coin]
    metric = 'price'
    df = messari.get_metric_timeseries(asset_slugs=assets, asset_metric=metric, start=start, end=end)
    df = df[coin]
    close = df['close'].tolist()
    train, test = train_test_split(close, test_size=period, shuffle=False)

    d = 0
    if adf(train)[1] >= 0.05:
        d = 1

    p_values = range(0, 6)
    q_values = range(0, 16)
    best_RMSE = np.inf
    best_arima_order = (0, 0, 0)

    for p_ in p_values:
        for q_ in q_values:
            warnings.filterwarnings("ignore")
            order_ = (p_,d,q_)
            model_ = ARIMA(train, order=order_).fit()
            test_pred_ = model_.forecast(period)
            test_RMSE_ = mean_squared_error(test, test_pred_, squared=False)
            if test_RMSE_ < best_RMSE:
                best_RMSE = test_RMSE_
                best_arima_order = order_

    best_model = ARIMA(close, order=best_arima_order).fit()
    future_pred = best_model.forecast(period)
    change_pred = (future_pred[-1] - close[-1]) / close[-1]
    return change_pred