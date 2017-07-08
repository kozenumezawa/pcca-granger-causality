import math
import numpy as np
from scipy import linalg

class CausalCalculator:
    def __init__(self, X, Y_cause):
        """data for test whether the time series Y_cause causes X
        :param X: dim(X) = (N, dm) = (length of time series, dimension of X)
        :param Y_cause:
        """
        self.X = X
        self.Y = Y_cause
        self.X_t = X.T
        self.Y_t = Y_cause.T

    def calcSigmaHat(self, sigma, eta):
        return sigma + eta * np.identity(sigma.shape[0])

    def calcGrangerCausality(self, k, m):
        """

        :param k:
        :param m:
        :return:
        """
        N = self.X.shape[0]
        dim_X = self.X.shape[1]
        dim_Y = self.Y.shape[1]


        x_t = []
        y_t = []
        x_tk_m = []
        y_tk_m = []

        for t in range(k + m - 1, N):
            x_t.append(self.X[t])
            y_t.append(self.Y[t])

            cut_x = self.X[t - k - m + 1: t - k + 1]
            x_tk_m.append(np.ravel(cut_x[::-1]))         # reverse the array and make the array 1d array
            cut_y = self.Y[t - k - m + 1: t - k + 1]
            y_tk_m.append(np.ravel(cut_y[::-1]))         # reverse the array and make the array 1d array

        x_t = np.array(x_t)
        y_t = np.array(y_t)
        x_tk_m = np.array(x_tk_m)
        y_tk_m = np.array(y_tk_m)

        sigma_xt_xt = np.cov(m=x_t, y=x_t, rowvar=False)    # each column represents a variable, while the rows contain observations
        sigma_xt_yt = np.cov(m=x_t, y=y_t, rowvar=False)
        sigma_xt_xtkm = np.cov(m=x_t, y=x_tk_m, rowvar=False)
        sigma_xt_ytkm = np.cov(m=x_t, y=y_tk_m, rowvar=False)

        sigma_yt_xt = np.cov(m=y_t, y=x_t, rowvar=False)
        sigma_yt_yt = np.cov(m=y_t, y=y_t, rowvar=False)
        sigma_yt_xtkm = np.cov(m=y_t, y=x_tk_m, rowvar=False)
        sigma_yt_ytkm = np.cov(m=y_t, y=y_tk_m, rowvar=False)

        sigma_xtkm_xt = np.cov(m=x_tk_m, y=x_t, rowvar=False)
        sigma_xtkm_yt = np.cov(m=x_tk_m, y=y_t, rowvar=False)
        sigma_xtkm_xtkm = np.cov(m=x_tk_m, y=x_tk_m, rowvar=False)
        sigma_xtkm_ytkm = np.cov(m=x_tk_m, y=y_tk_m, rowvar=False)

        sigma_ytkm_xt = np.cov(m=y_tk_m, y=x_t, rowvar=False)
        sigma_ytkm_yt = np.cov(m=y_tk_m, y=y_t, rowvar=False)
        sigma_ytkm_xtkm = np.cov(m=y_tk_m, y=x_tk_m, rowvar=False)
        sigma_ytkm_ytkm = np.cov(m=y_tk_m, y=y_tk_m, rowvar=False)

        eta_xtkm = 0.00001
        eta_xt = eta_xtkm
        eta_yt = eta_xtkm

        sigma_tilde_ytkm_xt_xtkm = sigma_ytkm_xt\
                                 - np.dot(np.dot(2 * sigma_ytkm_xtkm, np.linalg.inv(self.calcSigmaHat(sigma=sigma_xtkm_xtkm, eta=eta_xtkm))), sigma_xtkm_xt)\
                                 + np.dot(np.dot(np.dot(np.dot(sigma_ytkm_xtkm, np.linalg.inv(self.calcSigmaHat(sigma=sigma_xtkm_xtkm, eta=eta_xtkm))),sigma_xtkm_xtkm), np.linalg.inv(self.calcSigmaHat(sigma=sigma_xtkm_xtkm, eta=eta_xtkm))), sigma_xtkm_xt)

        sigma_tilde_xt_xt_xtkm = sigma_xt_xt \
                                   - np.dot(np.dot(2 * sigma_xt_xtkm, np.linalg.inv(self.calcSigmaHat(sigma=sigma_xtkm_xtkm, eta=eta_xtkm))), sigma_xtkm_xt) \
                                   + np.dot(np.dot(np.dot(np.dot(sigma_xt_xtkm, np.linalg.inv(self.calcSigmaHat(sigma=sigma_xtkm_xtkm, eta=eta_xtkm))),sigma_xtkm_xtkm), np.linalg.inv(self.calcSigmaHat(sigma=sigma_xtkm_xtkm, eta=eta_xtkm))), sigma_xtkm_xt)

        sigma_tilde_xt_ytkm_xtkm = sigma_xt_xt \
                                   - np.dot(np.dot(2 * sigma_xt_xtkm, np.linalg.inv(self.calcSigmaHat(sigma=sigma_xtkm_xtkm, eta=eta_xtkm))), sigma_xtkm_ytkm) \
                                   + np.dot(np.dot(np.dot(np.dot(sigma_xt_xtkm, np.linalg.inv(self.calcSigmaHat(sigma=sigma_xtkm_xtkm, eta=eta_xtkm))),sigma_xtkm_xtkm), np.linalg.inv(self.calcSigmaHat(sigma=sigma_xtkm_xtkm, eta=eta_xtkm))), sigma_xtkm_ytkm)

        sigma_tilde_ytkm_ytkm_xtkm = sigma_ytkm_xt \
                                   - np.dot(np.dot(2 * sigma_ytkm_xtkm, np.linalg.inv(self.calcSigmaHat(sigma=sigma_xtkm_xtkm, eta=eta_xtkm))), sigma_xtkm_ytkm) \
                                   + np.dot(np.dot(np.dot(np.dot(sigma_ytkm_xtkm, np.linalg.inv(self.calcSigmaHat(sigma=sigma_xtkm_xtkm, eta=eta_xtkm))),sigma_xtkm_xtkm), np.linalg.inv(self.calcSigmaHat(sigma=sigma_xtkm_xtkm, eta=eta_xtkm))), sigma_xtkm_ytkm)

        A = np.dot(np.dot(sigma_tilde_ytkm_xt_xtkm, np.linalg.inv(sigma_tilde_xt_xt_xtkm + eta_xt * np.identity(sigma_tilde_xt_xt_xtkm.shape[0]))), sigma_tilde_xt_ytkm_xtkm)
        B = sigma_tilde_ytkm_ytkm_xtkm + eta_yt * np.identity(sigma_tilde_xt_xt_xtkm.shape[0])

        eigenvalues = np.real(linalg.eig(a=A, b=B)[0])
        eigenvalue = np.max(eigenvalues)
        if eigenvalue > 1.0:
            eigenvalue = 0.9999
        Gyx = 0.5 * math.log(1 / (1 - eigenvalue), 2)
        print Gyx
        # np.set_printoptions(precision=3, suppress=True)