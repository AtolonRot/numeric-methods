import math

n = 1
a = 3
b = 5


def f(x):
    return (-1 * x ** 2) + (8 * x) - 12


h = (b - a) / n

result = 0
last_x = a

for i in range(n + 1):
    if i == 0:
        print(f"f({a}) = {f(a)}")
        result = result + f(a)
    elif i == n:
        print(f"f({b}) = {f(b)}")
        result = result + f(b)
    else:
        last_x = last_x + h
        print(f"f({last_x}) = {f(last_x)}")
        result = result + 2 * f(last_x)

print(f"\n\nh/2 = {h / 2}")
print(f"** RESULT (result * (h/2)) = {result * (h / 2)}")
