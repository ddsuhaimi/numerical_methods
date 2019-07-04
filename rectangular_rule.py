import math
import numpy


def f(x):
    return math.exp(x) * math.cos(x/2)


def rectangular(a, b, n, mode):
    h = (b-a) / n

    # create n dimensional evenly spaced with step = h
    x = numpy.arange(a, b, h).tolist()
    if mode == "left":
        return h * sum(f(x[i]) for i in range(len(x)))

    if mode == "right":
        # add the (n+1)th point, which is b
        x.append(b)
        return h * sum(f(x[i]) for i in range(1, len(x)))

    if mode == "mid":
        # add the (n+1)th point, which is b
        x.append(b)
        return h * sum(f(1/2 * (x[i+1] + x[i])) for i in range(len(x)-1))


left_approx = rectangular(-1, 1, 8, mode="left")
right_approx = rectangular(-1, 1, 8, mode="right")
mid_approx = rectangular(-1, 1, 8, mode="mid")
print(left_approx, right_approx, mid_approx)
