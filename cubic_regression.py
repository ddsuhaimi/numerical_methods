import numpy as np


def cubic_regression(x, y):
    n = len(x)
    sumx = sum(x)
    sumy = sum(y)
    sumxx = sum([i**2 for i in x])
    sumx3 = sum([i**3 for i in x])
    sumx4 = sum([i**4 for i in x])
    sumx5 = sum([i**5 for i in x])
    sumx6 = sum([i**6 for i in x])
    sumxy = sum([x[i] * y[i] for i in range(n)])
    sumx2y = sum([x[i]**2 * y[i] for i in range(n)])
    sumx3y = sum([x[i]**3 * y[i] for i in range(n)])

    # create coefficient matrix and solution vector
    A = [[n, sumx, sumxx, sumx3],
         [sumx, sumxx, sumx3, sumx4],
         [sumxx, sumx3, sumx4, sumx5],
         [sumx3, sumx4, sumx5, sumx6]]

    # create solution vector
    b = [sumy,
         sumxy,
         sumx2y,
         sumx3y]

    # solve A|b
    xsol = np.linalg.solve(A, b)

    # return solution tuple
    return tuple(xsol)


# data
x = [0, 0.4, 0.8, 1.2, 1.6]
y = [2.90, 3.10, 3.56, 4.6, 6.70]

# get predicted params
(a0, a1, a2, a3) = cubic_regression(x, y)

# get predicted y
y_p = [a0 + a1*x[i] + a2 * x[i]**2 + a3 * x[i]**3for i in range(len(x))]

# error
err = sum([(y[i] - y_p[i])**2 for i in range(len(x))])
