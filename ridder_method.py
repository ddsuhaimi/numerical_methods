from math import sqrt, inf

"""
reference:  C. Ridders. A new algorithm for computing a single root of a real
continuous function.
Circuits and Systems, IEEE Transactions on, 26(11):979–980, Nov 1979.
"""


def f(x):
    return (x - 10) * (x - 4)


def get_new_bracket(x1, x2, x3, x4):
    """
    this function return the approriate bracket point (closest and has
    different sign to x4)
    """
    points = [x1, x2, x3]
    dist = float(inf)
    for point in points:
        if abs(x4 - point) < dist and f(point) * f(x4) < 0:
            valid_point = point
            dist = abs(x4 - point)
    return valid_point


def sign(x):
    return x and (1, -1)[x < 0]


def ridder(x1, x2, e):

    if f(x1) * f(x2) > 0:
        print("invalid input")
        return

    # calculate and update points
    x3 = (x1 + x2) / 2
    f1 = f(x1)
    f2 = f(x2)
    f3 = f(x3)

    x4 = x3 - sign(f1 - f2) * (f3 / (sqrt(f3**2 - f1 * f2))) * (x3 - x1)

    # convergence check
    if abs(f(x4)) < e:
        return x4

    x1 = get_new_bracket(x1, x2, x3, x4)
    x2 = x4

    # recursive call
    return ridder(x1, x2, e)


print(ridder(-5, 8, 1e-10))
