import numpy


def f(x, y):
    return 2*x - y


def fprime(x, y):
    return y - 2*x + 2


def taylor(x, y0):
    """
    2nd order taylor method, 1st order is euler method
    """
    y = [0 for i in range(len(x))]
    y[0] = y0
    h = x[1] - x[0]
    for i in range(len(x) - 1):
        xi = x[i]
        yi = y[i]
        y[i+1] = yi + h*(f(xi, yi) + (1/2)*h*fprime(xi, yi))
    return y


# approximate up to 1.0, so make evenly spaced
# point from 0 to 1.1 with step = 0.1
x = numpy.arange(0, 1.1, 0.1).tolist()

# get predicted taylor(with initial solution y0 = 1)
y_taylor = taylor(x, 1)

# x points and its predicted y value
print(x)
print(y_taylor)
