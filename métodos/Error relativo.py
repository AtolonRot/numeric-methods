import numpy as np
import matplotlib.pyplot as plt

raiz = np.sqrt(5)
a = -1 * np.sqrt(5) * 0.9995
b = np.sqrt(5) * 1.0005

def err_relativo(a, b):
    return abs(raiz - (a+b)) / abs(raiz)

print(f"Raiz: {raiz}")
print(a)
print(b)

print(f"err relativo: {err_relativo(a, b)}")
print("\n")

raiz = np.sqrt(5)
a = -1 * np.sqrt(5) * 0.999
b = np.sqrt(5) * 1.001

print(a)
print(b)

print(f"err relativo: {err_relativo(a, b)}")
print("\n")

a = -1 * np.sqrt(5) * 0.9999
b = np.sqrt(5) * 1.0001

print(a)
print(b)

print(f"err relativo: {err_relativo(a, b)}")
print("\n")

a = -1 * np.sqrt(5) * 0.995
b = np.sqrt(5) * 1.005

print(a)
print(b)

print(f"err relativo: {err_relativo(a, b)}")