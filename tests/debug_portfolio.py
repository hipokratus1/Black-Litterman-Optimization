from src import make_portfolio

'''
Debug function to test only optimization
'''

if __name__ == '__main__':
    tokens = ['ETH', 'BTC']
    tokens.sort()
    views = {}
    for token in tokens:
        views[token] = 100 if token != 'BTC' else 0.1


    tokens = [token + '-USD' for token in tokens]
    tokens.sort()



    print(f'Tokens: {tokens}')
    weights = make_portfolio.optimize_portfolio(tokens, views)
    print('Results:')
    for token, percent in weights.items():
        print(f'{token}: {percent}')