import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from messari.messari import Messari
from sklearn.model_selection import train_test_split
from statsmodels.tsa.stattools import adfuller as adf
from statsmodels.tsa.arima.model import ARIMA
import warnings
import numpy as np
from src.make_portfolio import optimize_portfolio
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt


def make_predict(coin, start, end, period):
    messari = Messari()
    assets = [coin]
    metric = 'price'
    df = messari.get_metric_timeseries(asset_slugs=assets, asset_metric=metric, start=start, end=end)
    df = df[coin]
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

def make_plot(coins, start, end, period):
    views = dict()
    for coin in coins:
        views[coin] = make_predict(coin[0:-4], start, end, period)
        print(coin)
    
    weights = optimize_portfolio(
        tokens=tokens,
        views=views
    )
    
    print(weights)
    
    messari = Messari()
    coin = 'btc'
    assets = [coin]
    metric = 'price'

    end_date = datetime.strptime(end, '%Y-%m-%d').date()
    test_end = (end_date + timedelta(days=period)).strftime("%Y-%m-%d")
    start_date = datetime.strptime(start, '%Y-%m-%d').date()
    test_start = (end_date + timedelta(days=1)).strftime("%Y-%m-%d")
    
    df = messari.get_metric_timeseries(asset_slugs=assets, asset_metric=metric, start=test_start, end=test_end)
    df = df[coin]
    
    prices_df = pd.DataFrame(columns = coins)
    prices_df = pd.DataFrame(np.random.rand(len(df.index.tolist()), len(coins)), index=df.index, columns=list(coins))
    for coin in coins:
        messari = Messari()
        x = coin[0:-4]
        assets = [x]
        metric = 'price'
        start = '2023-04-02'
        end = '2023-05-01'
        prices_df[coin] = messari.get_metric_timeseries(asset_slugs=assets, asset_metric=metric, start=start, end=end)[x]['close']
    
    portfolio_prices = []
    prices = list(sum(list(prices_df.iloc[i][coin] for coin in coins)) for i in range(prices_df.shape[0]))
    
    %config InlineBackend.figure_format = 'retina'
    plt.rcParams['figure.figsize'] = 20, 10
    plt.plot(prices_df.index.tolist(), prices)
    plt.xlabel("Date", fontsize = 25)
    plt.ylabel("Portfolio price", fontsize = 25)
    plt.title(f" Portfolio price per date", fontsize = 30)
    plt.xticks(fontsize = 15)
    plt.yticks(fontsize = 15)
    plt.show()
