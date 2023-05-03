import numpy as np
import pandas as pd
from sklearn.covariance import ledoit_wolf


def get_covariance_matrix(prices, frequency=252):
    """
    ledoit_wolf: http://www.ledoit.net/ole2.pdf
    also: https://habr.com/ru/companies/skillfactory/articles/683498/
    frequency: 252 = number of trading
    """

    X = prices.pct_change().dropna(how="all")
    XS = np.nan_to_num(X.values)

    shrunk_cov, _ = ledoit_wolf(XS)
    covariance_matrix = pd.DataFrame(shrunk_cov, index=prices.columns, columns=prices.columns) * frequency
    return covariance_matrix

def market_implied_prior_returns(market_caps, risk_aversion, cov_matrix, risk_free_rate=0.02):
    weights = pd.Series(market_caps) / pd.Series(market_caps).sum()
    return risk_aversion * np.dot(cov_matrix, weights) + risk_free_rate

def market_implied_risk_aversion(market_prices, frequency=252, risk_free_rate=0.02):
    returns = market_prices.pct_change().dropna()
    R = returns.mean() * frequency
    var = returns.var() * frequency
    return (R -  risk_free_rate) / var


class BlackLitterman:
    """
    https://www.wallstreetmojo.com/black-litterman-model/
    """
    def __init__(
            self,
            covariance_matrix,
            prior,
            absolute_views,
            omega=None,
            confidences=None,
            tau=0.05,
            risk_aversion=1
    ):
        self.N = len(covariance_matrix)
        self.tokens = list(range(self.N))

        self.covariance_matrix = covariance_matrix

        self.prior = prior.values.reshape(-1, 1)

        self.P, self.Q = self.get_PQ(absolute_views)
        self.K = len(self.Q)

        self.risk_aversion = risk_aversion
        self.tau = tau

        self.omega = omega if omega else np.diag(np.diag(tau * self.P @ self.covariance_matrix @ self.P.T)) # TODO: add izdorek method here
        if self.omega.shape != (len(self.Q), len(self.Q)):
            raise Exception('Bad shape of omega')

        self.confidences = confidences

        self.validate()

    def get_PQ(self, absolute_views):
        # TODO: mb add cross view?
        views = pd.Series(absolute_views)
        P = np.eye(self.N)
        Q = np.zeros((len(views), 1))
        for i, view_ticker in enumerate(views.keys()):
            Q[i] = views[view_ticker]
        return P, Q

    def validate(self):
        # TODO: more validation
        if self.prior.shape != (self.N, 1):
            raise Exception('Bad shape of prior')
        if self.P.shape != (self.K, self.N):
            raise Exception('Bad shape of P')
        if self.covariance_matrix.shape != (self.N, self.N):
            raise Exception('Bad shape of covariance matrix')

    def model_returns(self):
        """
        posterior estimate of returns
        """
        tau_cov = np.linalg.inv(np.dot(self.tau, self.covariance_matrix))

        left = np.linalg.inv(
            tau_cov +
            np.dot(
                np.dot(self.P.T, np.linalg.inv(self.omega)),
                self.P
            )
        )
        right = np.dot(tau_cov, self.prior) + np.dot(np.dot(self.P.T, np.linalg.inv(self.omega)), self.Q)
        estimate = np.dot(left, right)

        return pd.Series(estimate.flatten(), index=self.tokens)

    def model_covariance(self):
        """
        posterior estimate of covariance
        """
        # TODO: add better optimizer, this function might be useful
        tau_cov = np.linalg.inv(np.dot(self.tau, self.covariance_matrix))

        left = self.covariance_matrix
        right = np.linalg.inv(
            tau_cov +
            np.dot(
                np.dot(self.P.T, np.linalg.inv(self.omega)),
                self.P
            )
        )
        estimate = left + right

        return pd.DataFrame(estimate, index=self.tokens, columns=self.tokens)


    def simple_weights(self):
        """
        Simple variant of optimizer
        """
        estimate_return = self.model_returns()

        weights = np.linalg.solve(self.risk_aversion * self.covariance_matrix, estimate_return)
        weights = weights / weights.sum()

        if abs(weights.sum() - 1.0) > 0.05:
            raise Exception('Something wrong with calculation of weights in portfolio :(')

        return weights