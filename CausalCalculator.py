import numpy as np

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