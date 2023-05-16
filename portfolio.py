from src import make_portfolio
from src import make_prediction

BREAK = 'STOP'
EXIT = 'EXIT'

def get_tokens(tokens=None, again=False):
    if not again:
        print(f'Please add cryptocurrencies that will be in your optimized portfolio, to continue input {BREAK}, to exit input {EXIT}')

    _tokens = set() if not tokens else tokens
    while True:
        parse = input()
        if parse == BREAK:
            break
        elif parse == EXIT:
            exit(0)
        for _token in parse.strip().split():
            if not make_prediction.is_valid_coin(_token):
                print(f'Token {_token} is incorrect')
                continue
            else:
                _tokens.add(_token.upper())
        print(f'Current tokens: {_tokens}')

    output = list(_tokens)
    output.sort()

    return output

if __name__ == '__main__':
    tokens = get_tokens()

    while len(tokens) <= 1: # when there is only 1 token no reason to make a prediction
        print(f'Please add more than 1 token')
        tokens = get_tokens(tokens=tokens, again=True)

    print(f'Finally: {tokens}')

    views = {}
    for token in tokens:
        print(f'Predicting price for {token}')
        prediction = make_prediction.make_predict(token, None, None)
        views[token + '-USD'] = prediction
        print(f'Price will go {prediction:.5f}')

    tokens = [token + '-USD' for token in tokens]

    weights = make_portfolio.optimize_portfolio(tokens, views)

    print(f'Output: {weights}')