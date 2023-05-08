import numpy as np
import pandas as pd
from sklearn.covariance import ledoit_wolf


def get_covariance_matrix(prices, frequency=252):
    """
    ledoit_wolf: http://www.ledoit.net/ole2.pdf, https://habr.com/ru/companies/skillfactory/articles/683498/

    :param prices: dataframe with prices of crypto-tokens
    :param frequency: number of trading days
    :return: ledoit_wolf method covariance matrix from sklearn
    """

    returns = prices.pct_change().dropna(how='all')
    returns = np.nan_to_num(returns.values)

    shrunk_cov, _ = ledoit_wolf(returns)
    covariance_matrix = pd.DataFrame(shrunk_cov, index=prices.columns, columns=prices.columns) * frequency
    return covariance_matrix

def get_risk_aversion(prices, frequency=252, risk_free_rate=0.02):
    returns = prices.pct_change().dropna()
    R = returns.mean() * frequency
    var = returns.var() * frequency
    return (R -  risk_free_rate) / var

def market_implied_prior_returns(capitalization, risk_aversion, covariance_matrix, risk_free_rate=0.02):
    """
    :param capitalization: market capitalization of tokens
    :param risk_aversion: risk aversion from get_risk_aversion method
    :param covariance_matrix: covariance matrix, basically from get_covariance_matrix method
    :param risk_free_rate: risk-free rate, https://www.wallstreetmojo.com/risk-free-rate/
    :return: market implied prior returns dataframe
    """
    capitalization = pd.Series(capitalization)
    weights = capitalization / capitalization.sum()
    return risk_free_rate + risk_aversion * covariance_matrix.dot(weights)



class BlackLitterman:
    """
    https://www.wallstreetmojo.com/black-litterman-model/
    """
    def init(
            self,
            covariance_matrix,
            prior,
            views,
            omega=None,
            confidences=None,
            tau=0.05,
            risk_aversion=1
    ):
        """

        :param covariance_matrix: market covariance matrix
        :param prior: prior returns
        :param views: views of tokens, will be converted to P, Q inside
        :param omega: uncertainty matrix
        :param confidences: confidences for uncertainly matrix
        :param tau: scaling factor
        :param risk_aversion:
        """
        self.N = len(covariance_matrix)
        self.tokens = list(range(self.N))

        self.covariance_matrix = covariance_matrix

        self.prior = prior.values.reshape(-1, 1)

        self.P, self.Q = self.__convert_views(views)
        self.K = len(self.Q)

        self.risk_aversion = risk_aversion
        self.tau = tau

        # TODO: add izdorek method here and different way to calculate omega
        if omega:
            self.omega = omega
        else:
            self.omega = np.diag(np.diag(tau * self.P @ self.covariance_matrix @ self.P.T))

        self.confidences = confidences

        self.__is_valid()

    def __convert_views(self, views):
        """
        helper function to convert dataframe views to P, Q
        P: matrix that identifies the assets involved in the views.
        Q: view Vector
        """
        # TODO: mb add cross view?
        views = pd.Series(views)
        P = np.eye(self.N)
        Q = np.zeros((len(views), 1))
        for i, view_ticker in enumerate(views.keys()):
            Q[i] = views[view_ticker]
        return P, Q

    def __is_valid(self) -> None:
        """
        helper function to check that all parameters are correct
        """
        # TODO: more validation
        if self.covariance_matrix is None:
            raise Exception('Covariance matrix parameter is None')
        if self.prior is None:
            raise Exception('Prior returns parameter is None')
        if self.P is None or self.Q is None:
            raise Exception('Something is wrong with views')
        if self.prior.shape != (self.N, 1):
            raise Exception('Bad shape of prior')
        if self.P.shape != (self.K, self.N):
            raise Exception('Bad shape of P')
        if self.covariance_matrix.shape != (self.N, self.N):
            raise Exception('Bad shape of covariance matrix')
        if self.omega.shape != (len(self.Q), len(self.Q)):
            raise Exception('Bad shape of omega')

    def bl_returns(self) -> pd.Series:
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

    def bl_covariance(self):
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
        return estimate

    def simple_weights(self):
        """
        simple variant of optimizer
        """
        estimate_return = self.bl_returns()

        weights = np.linalg.solve(self.risk_aversion * self.covariance_matrix, estimate_return)
        weights = weights / weights.sum()

        if abs(weights.sum() - 1.0) > 0.05:
            raise Exception('Something wrong with calculation of weights in portfolio')

        return weights