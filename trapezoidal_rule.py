import numpy
import math


def f(x):
    return math.exp(x) * math.cos(x/2)


def trapezoidal(a, b, n):
    h = (b-a) / n

    # making evenly spaced data points with step = h
    x = numpy.arange(a, b, h).tolist()

    # add last point to x, the (n+1)th point, which is b
    x.append(b)

    return (h/2) * sum(f(x[i]) + f(x[i + 1]) for i in range(len(x)-1))


result = trapezoidal(-1, 1, 8)
print(result)
