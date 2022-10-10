def newton(A, accuracy = 0.001, n = 2):
    x0 = float(A)
    x1 = (1/n)*((n-1)*x0+A/pow(x0, n-1))

    while abs(x1 - x0) > accuracy:
        x0 = x1
        x1 = (1/n)*((n-1)*x0+A/pow(x0, n-1))
    return x1


print(newton(225))
print(newton(783))