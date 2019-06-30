def Lagrange(x, x_p, i):
    """
    Get lagrange coefficient L_i(x_p)
    """
    result = 1
    for j in range(len(x)):
        if i != j:
            result = result * (x_p - x[j])/(x[i] - x[j])
    return result


def lagrange_interpolation(x, y, x_p):
    n = len(x)
    L = [None for i in range(n)]
    for i in range(n):
        L[i] = 1
        for j in range(n):
            if j != i:
                L[i] = Lagrange(x, x_p, i)
    y_p = sum([y[i]*L[i] for i in range(n)])
    return y_p


# data
x = [0.1, 0.5, 0.9, 1]
y = [0.12, 0.47, 0.65, 0.8]

# get interpolated y_p at x_p
y_p = lagrange_interpolation(x, y, 1.2)
print(y_p)
