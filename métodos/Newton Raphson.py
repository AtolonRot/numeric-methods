import numpy as np
import math

# INGRESO
fx  = lambda x: math.sin(x) - x**2
dfx = lambda x: math.cos(x) - (2 * x)

P0 = 1
for i in range(5):
    P1 = P0 - (fx(P0)/dfx(P0))
    print(i+1, P1)
    P0 = P1

    0.8767263
    0.87672622