from src import make_portfolio
from src import make_prediction
from src import utils

def get_tokens(tokens=None, again=False):
    if not again:
        print(f'Add cryptocurrencies that will be in your optimized portfolio, to continue input {utils.STOP}, to exit input {utils.EXIT}')

    _tokens = set() if not tokens else tokens
    while True:
        parse = input()
        if parse == utils.STOP:
            break
        elif parse == utils.EXIT:
            exit(0)
        for _token in parse.strip().split():
            if not make_prediction.is_valid_token(_token):
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
        print(f'Add more than 1 token')
        tokens = get_tokens(tokens=tokens, again=True)

    print(f'Finally: {tokens}')

    risk_free_rate = input('Please input Risk-Free Rate in % (by default it is 2%): ')
    risk_free_rate = risk_free_rate if risk_free_rate else utils.RISK_FREE_RATE_DEFAULT * 100

    views = {}
    for token in tokens:
        print(f'Predicting price view for {token}')
        prediction = make_prediction.make_predict(token, None, None)
        views[token + '-USD'] = prediction
        print(f'Prediction is: {prediction:.5f}')

    tokens = [token + '-USD' for token in tokens]
    weights = make_portfolio.optimize_portfolio(tokens, views, risk_free_rate=int(risk_free_rate) / 100)

    print(f'Result: {weights}')