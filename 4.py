A = float(input())
n = int(input())
x0 = float(input())
accuracy = float(input())

x1 = (1/n)*((n-1)*x0+A/pow(x0, n))

while abs(x1 - x0) > accuracy:
    x0 = x1
    x1 = (1/n)*((n-1)*x0+A/pow(x0, n-1))

print(x1, x0)