import collections
import numpy as np
import cvxpy as cp
import pandas as pd

from src import utils

class EfficientFrontierOptimizer:
    """
    Class for optimization of portfolio
    https://ru.wikipedia.org/wiki/Граница_эффективности
    """
    def __init__(self, expected_returns, covariance_matrix, risk_free_rate=utils.RISK_FREE_RATE_DEFAULT):
        self.expected_returns = expected_returns.values
        self.covariance_matrix = covariance_matrix
        self.risk_free_rate = risk_free_rate

        self.tokens = list(expected_returns.index)
        self.N = len(self.tokens)

        self.w = cp.Variable(self.N)

    def optimize(self, L2_reg = False):
        """
        Maximizing max sharpe of portfolio
        https://ru.wikipedia.org/wiki/Коэффициент_Шарпа
        """
        self.objective = cp.quad_form(self.w, self.covariance_matrix)
        if L2_reg:
            self.objective += cp.sum_squares(self.w)

        k = cp.Variable()
        constraints = [
            (self.expected_returns - self.risk_free_rate).T @ self.w == 1,
            cp.sum(self.w) == k,
            k >= 0,
            self.w >= (np.array([0] * self.N) * k),
            self.w <= (np.array([1] * self.N) * k)
        ]
        opt = cp.Problem(cp.Minimize(self.objective), constraints)
        opt.solve()
        self.weights = (self.w.value / k.value).round(16) + 0.0

        if abs(self.weights.sum() - 1.0) > 0.05:
            raise Exception('Something wrong with calculation of weights in portfolio')

        return self.get_weights()

    def _clean_weights(self, drop=1e-4):
        """
        Remove bad weights of tokens that are close to zero
        """
        clean_weights = self.weights.copy()
        clean_weights[np.abs(clean_weights) < drop] = 0

        if abs(clean_weights.sum() - 1.0) > 0.05:
            raise Exception('Something wrong with calculation of weights in portfolio')
        return clean_weights

    def get_weights(self, df=False, clean=False):
        """
        Helper function for output type of weights
        """
        weights = self.weights if not clean else self._clean_weights()
        if df:
            return pd.DataFrame(weights, index=self.tokens) # just a dataframe with info

        return collections.OrderedDict(zip(self.tokens, weights)) # {token: weight}
