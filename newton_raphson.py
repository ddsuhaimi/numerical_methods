import sympy as sym


def f(x):
    return (x-2)*(x-3)


# get derivative of f
x = sym.symbols('x')
diff_f = sym.diff(f(x), x)


def fprime(a):
    return diff_f.subs({x: a})


def newton_raphson(a, e, N):
    x = [None for i in range(N)]
    x[0] = a

    for i in range(N-1):
        # update new value to check
        x[i + 1] = x[i] - f(x[i]) / float(fprime(x[i]))

        # convergence check
        if abs(x[i + 1]-x[i]) < e:
            return x[i + 1]

    # if we still cant satisfy convergence check,
    # the it must not converge
    return "not converge"


print(newton_raphson(5, 1e-15, 1000))
