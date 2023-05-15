from src import make_portfolio
from src import make_prediction

if __name__ == '__main__':
    BREAK = 'BREAK'
    print(f'Please add cryptocurrencies that will be in your optimized portfolio, to stop just input {BREAK}')
    tokens = []
    while True:
        parse = input()
        if parse == BREAK:
            break
        tokens.extend(parse.split())
        print(f'Current tokens: {tokens}')

    print(f'Finally: {tokens}')

    print('Please, wait...')
    views = {}
    for token in tokens:
        print(f'Predicting price for {token}')
        prediction = make_prediction.make_predict(token, None, None)
        views[token + '-USD'] = prediction
        print(f'Price will go {prediction:.2f}')

    tokens = [token + '-USD' for token in tokens]

    weights = make_portfolio.optimize_portfolio(tokens, views)

    print(f'Output: {weights}')