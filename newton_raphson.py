import sympy as sym


def f(x):
    return (x-2)*(x-3)


# get derivative of f
x = sym.symbols('x')
diff_f = sym.diff(f(x), x)


def fprime(a):
    return diff_f.subs({x: a})


def newton_raphson(a, e, N):
    for i in range(N):
        # convergence check
        if abs(f(a)) < e:
            return a

        # update new value to check
        a = a - f(a) / float(fprime(a))

    # if we still cant satisfy convergence check,
    # the it must not converge
    if abs(f(a)) > e:
        return None


print(newton_raphson(5, 1e-15, 1000))
