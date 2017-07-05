# pcca-granger-causality
Implementation of Partial Canonical Correlation Analysis(PCCA) interpretation of Granger Causality, which is described in [1], in Python.

# test data
To check whether the calculation result is correct,`create-test-data.py` generates test data.
The data is generated following the below equation.

```math
\begin{align*}
& \bm{X}_{t}=\bm{Y}_{t-1}+\epsilon_{x,t} \\
& \bm{Y}_{t}= \left(\begin{array}{ccc}
        0.3 & 0.3 & 0.3 \\
        0.3 & 0.3 & 0.3 \\
        0.3 & 0.3 & 0.3
    \end{array}\right)
    \bm{Y}_{t-1}+\epsilon_{y,x}\\
\end{align*}
```

 

# Reference
[1]: [Causal flow](http://ieeexplore.ieee.org/document/6175964/), Yamashita, Yuya Harada, Tatsuya Kuniyoshi, Yasuo, IEEE Transactions on Multimedia(2012)