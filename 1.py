import math
def fun(x):
    y = math.log((math.exp(1/(math.sin(x) + 1))/(5/4 + 1/(x ** 15))), 1 + x ** 2)
    return y
print(fun(1), fun(10), fun(1000))
