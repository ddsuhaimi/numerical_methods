def f(x):
    
    return (x-10)*(x-20)*(x+3)


def bisection(a, b, e):

    if f(a)*f(b) > 0:
        print(a, b, "input invalid, c")
        return
    
    # convergence check
    if abs(a-b) < e:
        result = (a+b)/2
        return result

    mid = (a+b)/2

    # change the bracket point
    if f(mid) < 0:
        a = mid
    else:
        b = mid

    # recursive call
    return bisection(a, b, e)


print(bisection(-4, 2, 1e-15))