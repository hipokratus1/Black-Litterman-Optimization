import yfinance
from src import black_litterman
from src import optimizers
from src import utils

class DataLoader:
    """
    Helper class for loading data from messari and/or yahoo finance APIs
    """
    def __init__(self, tokens, market='BTC-USD', start=None, end=None):
        market_capitalizations = {}
        for token in tokens:
            try:
                t = yfinance.Ticker(token)
                market_capitalizations[token] = t.info['marketCap']
            except:
                raise ValueError(f'{token} is invalid token')

        self.market_capitalizations = market_capitalizations

        if start or end:
            ohlc = yfinance.download(
                tickers=tokens,
                start=start,
                end=end,
                progress=False
            )
        else:
            ohlc = yfinance.download(
                tickers=tokens,
                period='max',
                progress=False
            )
        self.prices = ohlc['Adj Close'].dropna()

        if start or end:
            self.market_prices = yfinance.download(
                tickers=market,
                start=start,
                end=end,
                progress=False
            )['Close']
        else:
            self.market_prices = yfinance.download(
                tickers=market,
                period='max',
                progress=False
            )['Close']


def optimize_portfolio(tokens, views, risk_free_rate=utils.RISK_FREE_RATE_DEFAULT):
    """
    Helper function for portfolio optimization pipeline
    Originally was an ipynb
    """
    data = DataLoader(
        tokens=tokens,
    )

    prices = data.prices # dataframe with historical prices of cryptocurrencies
    market_prices = data.market_prices # smth like S&P 500
    market_capitalizations = data.market_capitalizations # {token: capitalization}

    covariance_matrix = black_litterman.get_covariance_matrix(prices)
    risk_aversion = black_litterman.get_risk_aversion(market_prices, risk_free_rate=risk_free_rate)

    market_prior = black_litterman.market_implied_prior_returns(
        capitalization=market_capitalizations,
        risk_aversion=risk_aversion,
        covariance_matrix=covariance_matrix,
        risk_free_rate=risk_free_rate
    )

    bl = black_litterman.BlackLitterman(
        covariance_matrix=covariance_matrix,
        prior=market_prior,
        views=views
    )

    frontier = optimizers.EfficientFrontierOptimizer(
        expected_returns=bl.bl_returns(),
        covariance_matrix=bl.bl_covariance(),
        risk_free_rate=risk_free_rate
    )
    frontier.optimize(
        L2_reg=True
    )

    weights = frontier.get_weights(
        df=False,
        clean=True
    )

    return weights

