def plotGraph(X, Y, m_x, m_y, N):
    import matplotlib.pyplot as plt
    t = range(N)

    fig = plt.figure()
    for i in range(m_x):
        ax = fig.add_subplot(m_x, 1, i + 1)
        ax.plot(t, X.T[i], color='r', lw=0.5)
        ax.plot(t, Y.T[i], color='b', lw=0.5)
        ax.set_ylim(-1, 1)
        ax.legend(labels=['X', 'Y'])
    plt.show()

if __name__ == "__main__":
    import numpy as np
    import json


    N = 100         # length of time series
    m_x = 3         # the number of variables of X
    m_y = 3         # the number of variables of X

    mean, sigma = 0, 0.1
    s_x = np.array([np.random.normal(mean, sigma, m_x) for i in range(N)])
    s_y = np.array([np.random.normal(mean, sigma, m_y) for i in range(N)])

    X = np.array([np.zeros(m_x) for i in range(N)])
    Y = np.array([np.zeros(m_y) for i in range(N)])
    A = np.array([
        [0.3, 0.3, 0.3],
        [0.3, 0.3, 0.3],
        [0.3, 0.3, 0.3],
    ])

    Y[0] = s_y[0]
    X[0] = s_x[0]
    for t in range(1, N):
        Y[t] = np.dot(A, Y[t-1]) + s_y[t]
        X[t] = Y[t-1] + s_x[t]

    plotGraph(X, Y, m_x, m_y, N)

    save_json = {
        "X": X.tolist(),
        "Y": Y.tolist()
    }
    f = open("./test-data.json", "w")
    json.dump(save_json, f)
    f.close()

