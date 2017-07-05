# pcca-granger-causality
Implementation of Partial Canonical Correlation Analysis(PCCA) interpretation of Granger Causality, which is described in [1], in Python.

# test data
To check whether the calculation result is correct,`create-test-data.py` generates test data.
The data is generated following the below equation.

<img src="http://i.imgur.com/i2YLFLW.png" alt="test-equation" width="300"/>
<img src="http://i.imgur.com/HybVljm.png" alt="test-equation" width="200"/>

<!--- 
```math
\begin{align*}
& \bm{X}_{t}=\bm{Y}_{t-1}+\epsilon_{x,t} \\
& \bm{Y}_{t}= \left(\begin{array}{ccc}
        0.3 & 0.3 & 0.3 \\
        0.3 & 0.3 & 0.3 \\
        0.3 & 0.3 & 0.3
    \end{array}\right)
    \bm{Y}_{t-1}+\epsilon_{y,t}\\
\end{align*}

\begin{align*}
& \epsilon_{x,t},\epsilon_{y,t}\ are\ Gaussian\ noise\ with\\
& E[\epsilon_{x,t}]=E[\epsilon_{y,t}]=0\\
& \sigma_{x}^{2}=\sigma_{y}^{2}=0.1
\end{align*}
```
--->
 

# Reference
[1]: [Causal flow](http://ieeexplore.ieee.org/document/6175964/), Yamashita, Yuya Harada, Tatsuya Kuniyoshi, Yasuo, IEEE Transactions on Multimedia(2012)