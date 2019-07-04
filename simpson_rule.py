import numpy
import math


def f(x):
    return math.exp(x) * math.cos(x/2)


def simpson(a, b, n, mode):
    h = (b-a) / n
    x = numpy.arange(a, b, h).tolist()
    n = len(x)
    x.append(b)

    if mode == "1/3":
        even_sum = sum(f(x[i]) for i in range(n)[1::2])
        odd_sum = sum(f(x[i]) for i in range(n-1)[2::2])
        return (h/3) * (f(x[0]) + 4*even_sum + 2*odd_sum + f(x[n]))

    if mode == "3/8":
        even_sum = sum(f(x[i]) + f(x[i+1]) for i in range(n-1)[1::3])
        odd_sum = sum(f(x[i]) for i in range(n-2)[3::3])
        return (3*h/8) * (f(x[0]) + 3*even_sum + 2*odd_sum + f(x[n]))


# if the # number of interval is even, use 1/3
# else, use 3/8
even_interval = simpson(-1, 1, 8, mode="1/3")
odd_interval = simpson(-1, 1, 9, mode="3/8")
print(even_interval, odd_interval)
