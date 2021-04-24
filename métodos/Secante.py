import math
fx = lambda x: math.sin(x)

x0 = 3
x1 = 4
erroru = 10 ** -3
raiz = []
raiz.insert(0, 0)
i = 0
error = 1
while abs(error) > erroru:
    x2 = x1 - (fx(x1) * (x1 - x0)) / (fx(x1) - fx(x0))
    raiz.append(x2)
    x0 = x1
    x1 = x2
    i = i + 1
    error = (raiz[i] - raiz[i - 1]) / raiz[i]
    print(x2)
