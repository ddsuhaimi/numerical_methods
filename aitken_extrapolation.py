def f(x):
    return (x - 2)*(x - 3)


def g(x):
    return f(x)/h(x) + x


def h(x):
    return 1


def aitken(x, e, N):
    for i in range(N):
        # convergence check
        if abs(f(x)) < e:
            return x

        # update new value to check
        x = x - (g(x) - x)**2 / (g(g(x)) - 2*g(x) + x)

    # if we still cant satisfy convergence check,
    # the it must not converge
    if abs(f(x)) > e:
        return None


print(aitken(5, 1e-15, 1000))
