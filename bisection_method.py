def f(x):
    
    return pow(x, 3) - x + 5


def bisection(a, b, e):

    if f(a)*f(b) > 0:
        print(a, b, "input invalid, c")
        return
    
    if abs(a-b) < e:
        result = (a+b)/2
        return result

    mid = (a+b)/2

    if f(mid) < 0:
        a = mid
    else:
        b = mid

    return bisection(a, b, e)


print(bisection(-10, 10, 0.001))