from src.make_portfolio import optimize_portfolio

if __name__ == '__main__':
    views = {
        'BTC-USD': 0.1,
        'ETH-USD': 0.1,
    }
    tokens = ['BTC-USD', 'ETH-USD']

    weights = optimize_portfolio(
        tokens=tokens,
        views=views
    )
    print(weights)