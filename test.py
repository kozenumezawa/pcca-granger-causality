
if __name__ == "__main__":
    import json
    import numpy as np
    import matplotlib.pyplot as plt
    from CausalCalculator import CausalCalculator

    m = 1
    k = 1

    f = open("./test-data.json", "r")
    json_data = json.load(f)

    X = np.array(json_data["X"], dtype=np.float) # dim(X) = (N, dm) = (length of time series, dimension of X)
    Y = np.array(json_data["Y"], dtype=np.float)

    calc_xy = CausalCalculator(X=X, Y_cause=Y)
    calc_yx = CausalCalculator(X=Y, Y_cause=X)

    Gy_to_x = calc_xy.calcGrangerCausality(k=k, m=m)
    Gx_to_y = calc_yx.calcGrangerCausality(k=k, m=m)

    print "Granger Causality Y -> X :", Gy_to_x
    print "Granger Causality X -> Y :", Gx_to_y