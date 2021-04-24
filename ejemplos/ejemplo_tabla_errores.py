import numpy as np

# ############# Definir el intervalo [a, b] y el número de iteraciones N
a = np.pi / 2
b = (3 * np.pi) / 2

n = 10

print("a", fx0)
print("b", np.pi)
print("c", (3 * np.pi) / 2)
print("d", (5 * np.pi) / 2)

# ############# Definir f(x) en este caso: f(x) = cos(x) - x
def f(x):
    return 3 * (np.cos(x) ** 2)


# ############# Encontrar la solución exacta primero
def sol_exacta(n):
    a = 0
    b = 2
    for i in range(n):
        Pn = (a + b) / 2
        fPn = f(Pn)

        # Definir el nuevo intervalo y volver a tomar el punto medio (empezar el loop)
        if f(a) * fPn < 0:
            a = a
            b = Pn
        else:
            a = Pn
            b = b
    return Pn


# La solución exacta será esta
P = sol_exacta(400)
print(f"Valor exacto: {P}")


# ############# Encontrar
# Error relativo y absoluto
# Encontrar cifras significativas |P-Pn| / |P| < 5x10^-t
for i in range(1, n + 1):
    Pn = (a + b) / 2
    fPn = f(Pn)

    # Error absoluto: |Valor medido - Valor exacto|
    # Error relativo = |Error absoluto| / Valor exacto

    err_absoluto = float("{0:.20f}".format(
        abs(P - Pn)  # Fórmula
    ))
    err_relativo = float("{0:.20f}".format(
        err_absoluto / abs(P)  # Fórmula
    ))

    t = 1 # Cifras significativas empezando en 1

    # Encontrar cifras significativas
    while True:
        cifras_sig_formula = 5 * pow(10, -(t+1)) # Se le suma 1 a t para comprobar la siguiente iteración
        if err_relativo < cifras_sig_formula:
            t += 1
        else:
            break

    # Imprimir resultado
    print(
        f"n: {i} | Pn: {Pn} | f(Pn): {fPn} | E. Absoluto: {err_absoluto} | E. Relativo: {err_relativo} | Cifras Sig: {t}")

    # Definir el nuevo intervalo y volver a tomar el punto medio
    if f(a) * fPn < 0:
        a = a
        b = Pn
    else:
        a = Pn
        b = b
