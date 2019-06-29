def f(x):

    return (x-10)*(x-20)*(x+3)


def secant(a, b, e, N):
    x = [None for i in range(N)]
    x[0] = a
    x[1] = b

    for i in range(1, N-1):

        # change the bracket point
        x[i + 1] = x[i] - f(x[i]) * (((x[i] - x[i - 1])) /
                                     (f(x[i])-f(x[i - 1])))

        # convergence check
        if abs(x[i + 1] - x[i]) < e:
            return x[i + 1]

    # if we still cant satify convergent check,
    # then it must not converge
    return "not converge"


print(secant(-4, 2, 1e-6, 100))
