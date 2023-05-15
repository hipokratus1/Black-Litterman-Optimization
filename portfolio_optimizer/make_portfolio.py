import yfinance
from black_litterman import model, optimizers

class DataLoader:
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
                end=end
            )
        else:
            ohlc = yfinance.download(
                tickers=tokens,
                period='max'
            )
        self.prices = ohlc['Adj Close'].dropna()

        if start or end:
            self.market_prices = yfinance.download(
                tickers=market,
                start=start,
                end=end
            )['Adj Close']
        else:
            self.market_prices = yfinance.download(
                tickers=market,
                period='max'
            )['Adj Close']


def optimize_portfolio(tokens, views):
    data = DataLoader(
        tokens=tokens,
    )

    prices = data.prices # dataframe with historical prices of cryptocurrencies
    market_prices = data.market_prices # smth like S&P 500
    market_capitalizations = data.market_capitalizations # {token: capitalization}

    covariance_matrix = model.get_covariance_matrix(prices)
    risk_aversion = model.get_risk_aversion(market_prices)

    market_prior = model.market_implied_prior_returns(
        capitalization=market_capitalizations,
        risk_aversion=risk_aversion,
        covariance_matrix=covariance_matrix,
        risk_free_rate=0.02
    )

    bl = model.BlackLitterman(
        covariance_matrix=covariance_matrix,
        prior=market_prior,
        views=views
    )

    frontier = optimizers.EfficientFrontierOptimizer(
        expected_returns=bl.bl_returns(),
        covariance_matrix=bl.bl_covariance(),
        risk_free_rate=0.02
    )
    frontier.optimize(
        L2_reg=True
    )

    return frontier.get_weights(
        df=True,
        clean=True
    )

