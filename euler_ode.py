import numpy


def f(x, y):
    return 2*x - y


def euler_ode(x, y0):
    y = [0 for i in range(len(x))]
    y[0] = y0
    h = x[1] - x[0]
    for i in range(len(x) - 1):
        y[i+1] = y[i] + h*f(x[i], y[i])
    return y


# approximate up to 1.0, so make evenly spaced
# point from 0 to 1.1 with step = 0.1
x = numpy.arange(0, 1.1, 0.1).tolist()

# get predicted euler(with initial solution y0 = 1)
y_euler = euler_ode(x, 1)

# x points and its predicted y value
print(x)
print(y_euler)
