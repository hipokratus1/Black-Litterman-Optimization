import collections
import numpy as np
import cvxpy as cp

class EfficientFrontierOptimizer:
    """
    https://ru.wikipedia.org/wiki/Граница_эффективности
    """
    def init(self, expected_returns, cov_matrix, risk_free_rate=0.02):
        self.expected_returns = expected_returns.values
        self.cov_matrix = cov_matrix
        self.risk_free_rate = risk_free_rate

        self.tokens = list(expected_returns.index)
        self.N = len(self.tokens)

        self._w = cp.Variable(self.N)

    def optimize(self, L2_reg = False):
        """
        https://ru.wikipedia.org/wiki/Коэффициент_Шарпа
        """
        self.objective = cp.quad_form(self._w, self.cov_matrix)
        if L2_reg:
            self.objective += cp.sum_squares(self._w)

        k = cp.Variable()
        constraints = [
            (self.expected_returns - self.risk_free_rate).T @ self._w == 1,
            cp.sum(self._w) == k,
            k >= 0,
            self._w >= (np.array([0] * self.N) * k),
            self._w <= (np.array([1] * self.N) * k)
        ]
        _opt = cp.Problem(cp.Minimize(self.objective), constraints)
        _opt.solve()
        self.weights = self._w.value.round(16) + 0.0
        self.weights = (self._w.value / k.value).round(16) + 0.0
        return collections.OrderedDict(zip(self.tokens, self.weights))

    def clean_weights(self, cutoff=1e-4, rounding=5):
        clean_weights = self.weights.copy()
        clean_weights[np.abs(clean_weights) < cutoff] = 0
        if rounding is not None:
            clean_weights = np.round(clean_weights, rounding)
        return collections.OrderedDict(zip(self.tokens, clean_weights))