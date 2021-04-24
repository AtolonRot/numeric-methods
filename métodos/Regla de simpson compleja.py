import math

# N tiene que ser par
n = 4
a = 0
b = 1


def f(x):
    return math.sqrt(5 + (x ** 3))


h = (b - a) / n

current = a

Xi = []
Xmi = []


# Encontrar Xi y Xmi
for i in range(n + 1):
    if i == 0:
        print(f"X{i}: f({a}) = {f(a)}")
    elif i == n:
        print(f"X{i}: f({b}) = {f(b)}")

    if i != 0:
        # current = x1, x2, xn...
        last_x = current
        current = current + h
        if i != n:
            print(f"X{i}: f({current}) = {f(current)}")
            Xi.append(current)

        # xm1, xm2, xmn...
        if i > 0:
            Xm = (last_x + current) / 2
            print(f"Xm{i}: f({Xm}) = {f(Xm)}")
            Xmi.append(Xm)

print(f"\nXi list: {Xi}")
print(f"Xmi list: {Xmi}")

# Formulas del medio
result_Xmi = 0
result_Xi = 0

for item in Xmi:
    result_Xmi += f(item)

for item in Xi:
    result_Xi += f(item)

# Resultado Final
result = ((b - a) / (6 * n)) * (f(a) + (2 * result_Xi) + (4 * result_Xmi) + f(b))

print(f"\n\n[(b-a)/6n] = {(b - a) / (6 * n)}")
print(f"** RESULT (result * [(b-a)/6n] ) = {result}")
