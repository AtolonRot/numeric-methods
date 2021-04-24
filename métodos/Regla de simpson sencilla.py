import math

# N tiene que ser igual 2 para la sencilla
n = 2
a = 0
b = 1


def f(x):
    return math.sqrt(5 + (x ** 3))


# Resultado Final
result = ((b - a) / 6) * (f(a) + (4 * f((a + b) / 2)) + f(b))

print(f"\n\n[(b-a)/6] = {(b - a) / 6}")
print(f"** RESULT (result * [(b-a)/6n] ) = {result}")
