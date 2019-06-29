def f(x):
    return (x-10)*(x-20)*(x+3)


def regula_falsi(a, b, e):

    if f(a)*f(b) > 0:
        print('invalid input')
        return

    mid = (a*f(b) - b*f(a))/(f(b) - f(a))

    # convergence check
    if abs(a-b) < e:
        return mid

    # change the bracket point
    if f(mid) > 0:
        b = mid
    else:
        a = mid

    # recursive call
    return regula_falsi(a, b, e)


print(regula_falsi(-4, 2, 1e-15))
