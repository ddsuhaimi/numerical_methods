def f(x):

    return (x-10)*(x-20)*(x+3)


def bisection(a, b, e):

    if f(a)*f(b) > 0:
        print("input invalid")
        return

    mid = (a+b)/2

    if f(mid) == 0:
        return mid

    # change the bracket point
    if f(mid) < 0:
        a = mid
    else:
        b = mid

    # convergence check
    if abs(a-b) < e:
        result = (a+b)/2
        return result

    # recursive call
    return bisection(a, b, e)


print(bisection(-4, 2, 1e-15))  # -3.0
