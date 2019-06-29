def linear_regression(x, y):

    n = len(x)
    sumx = sum(x)
    sumy = sum(y)

    xx = [i*i for i in x]
    xy = [x[i]*y[i] for i in range(len(x))]

    sumxx = sum(xx)
    sumxy = sum(xy)

    print(sumx, sumy, sumxx, sumxy)

    denom = (n*sumxx) - sumx**2

    a0 = (sumxx*sumy - sumx*sumxy)/denom
    a1 = (n*sumxy - sumx*sumy)/denom

    return (a0, a1)


# data
x = [0.2, 0.4, 0.6, 0.8, 1.0, 1.2]
y = [8.0, 8.4, 8.8, 8.6, 8.5, 8.7]

# get predicted params
(a0, a1) = linear_regression(x, y)

# predicted y
y_p = [a1 * x[i] + a0 for i in range(len(x))]

# total error
err = sum([(y_p[i] - y[i])**2 for i in range(len(x))])
print(err)
