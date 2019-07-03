import numpy
import math


def f(x):
    return math.exp(-1*x) * math.cos(x)


def finite_difference_first(x, i, mode):
    """
    note: this function does not check the validity of i
    keep in mind that:
        backward cant work at i = 0
        forward cant work at i = len(x) - 1
        central only work at interior points, 0 < i < len(x) - 1
    """
    if mode == "backward":
        print(x[i])
        h = x[i] - x[i-1]
        return (f(x[i-2]) - 2*f(x[i-1]) + f(x[i])) / h**2

    if mode == "forward":
        h = x[i+1] - x[i]
        return (f(x[i+2]) - 2*f(x[i+1]) + f(x[i])) / h**2

    if mode == "central":
        h = x[i+1] - x[i]
        return (f(x[i-1]) - 2*f(x[i]) + f(x[i+1])) / h**2


# making data (an evenly spaced data with step = 0.2)
x = numpy.arange(0.0, 2, 0.2).tolist()

# we are approximating f(1.4), the correct index is
# 7 since x[7] = 1.4
backward_diff = finite_difference_first(x, 7, mode="backward")
print(backward_diff)

forward_diff = finite_difference_first(x, 7, mode="forward")
print(forward_diff)

central_diff = finite_difference_first(x, 7, mode="central")
print(central_diff)
