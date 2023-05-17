import sys, os

RISK_FREE_RATE_DEFAULT = 0.02
STOP = 'STOP'
EXIT = 'EXIT'

def no_print(func):
    """
    Decorator for removing all prints in function
    """
    def _wrapper(*args, **kwargs):
        sys.stdout = open(os.devnull, 'w')
        output = func(*args, **kwargs)
        sys.stdout = sys.__stdout__
        return output

    return _wrapper
