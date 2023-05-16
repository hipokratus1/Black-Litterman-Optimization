from src import make_portfolio
from src import make_prediction


def get_tokens(tokens=None, again=False):
    BREAK = 'BREAK'
    if not again:
        print(f'Please add cryptocurrencies that will be in your optimized portfolio, to stop just input {BREAK}')

    tokens = [] if not tokens else tokens
    while True:
        parse = input()
        if parse == BREAK:
            break
        tokens.extend(parse.split())
        print(f'Current tokens: {tokens}')
    tokens.sort()
    return tokens

if __name__ == '__main__':
    tokens = get_tokens()

    while len(tokens) == 1: # when there is only 1 token no reason to make a prediction
        print(f'Please add more than 1 token')
        tokens = get_tokens(tokens=tokens, again=True)

    print(f'Finally: {tokens}')

    print('Please, wait...')
    views = {}
    for token in tokens:
        print(f'Predicting price for {token}')
        prediction = make_prediction.make_predict(token, None, None)
        views[token + '-USD'] = prediction
        print(f'Price will go {prediction:.5f}')

    tokens = [token + '-USD' for token in tokens]

    weights = make_portfolio.optimize_portfolio(tokens, views)

    print(f'Output: {weights}')