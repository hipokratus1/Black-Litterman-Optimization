import collections
import numpy as np
import cvxpy as cp
import pandas as pd


class EfficientFrontierOptimizer:
    """
    https://ru.wikipedia.org/wiki/Граница_эффективности
    """
    def __init__(self, expected_returns, covariance_matrix, risk_free_rate=0.02):
        self.expected_returns = expected_returns.values
        self.covariance_matrix = covariance_matrix
        self.risk_free_rate = risk_free_rate

        self.tokens = list(expected_returns.index)
        self.N = len(self.tokens)

        self.w = cp.Variable(self.N)

    def optimize(self, L2_reg = False):
        """
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
        self.weights = self.w.value.round(16) + 0.0
        self.weights = (self.w.value / k.value).round(16) + 0.0

        if abs(self.weights.sum() - 1.0) > 0.05:
            raise Exception('Something wrong with calculation of weights in portfolio')

        return collections.OrderedDict(zip(self.tokens, self.weights))

    def _clean_weights(self, cutoff=1e-4, rounding=5):
        clean_weights = self.weights.copy()
        clean_weights[np.abs(clean_weights) < cutoff] = 0
        if rounding is not None:
            clean_weights = np.round(clean_weights, rounding)
        if abs(clean_weights.sum() - 1.0) > 0.05:
            raise Exception('Something wrong with calculation of weights in portfolio')
        return clean_weights

    def get_weights(self, df=False, clean=False):
        weights = self.weights if not clean else self._clean_weights()
        if df:
            return pd.DataFrame(weights, index=self.tokens)

        return collections.OrderedDict(zip(self.tokens, weights))
