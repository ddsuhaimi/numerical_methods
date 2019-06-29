def f(x):
    return (x - 2)*(x - 3)


def fprime(x, h):
    return (f(x + h) - f(x)) / h


def steffensen(x, e, N):
    for i in range(N):
        # convergence check
        if abs(f(x)) < e:
            return x

        # update new value to check
        h = f(x)
        x = x - f(x) / fprime(x, h)

    # if we still cant satisfy convergence check,
    # the it must not converge
    if abs(f(x)) > e:
        return None


print(steffensen(5, 1e-15, 1000))
