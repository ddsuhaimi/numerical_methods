def f(x):

    return (x-10)*(x-20)*(x+3)


def secant(a, b, e, N):

    for i in range(N):
        # convergence check
        if abs(a-b) < e:
            return (a-b)/2

        # change the bracket point
        new_p = b - f(b) * ((b-a) / f(b)-f(a))
        a = b
        b = new_p

    # if we still cant satify convergent check,
    # then it must not converge
    if (b-a) > e:
        return None


print(secant(-4, 2, 1e-6, 100))
