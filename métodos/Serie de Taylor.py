import sympy as sp
import numpy as np

# Elegir cuantas cifras decimales mostrar en el resultado
digitos = 5

# ############# Definir f(x) y variables del problema
Xi = 0
h = 0.3


def f(x):
    return pow(np.e, -x**2)


# ############# Encontrar la N derivada
x = sp.Symbol('x')


def df(x, n):
    return sp.diff(f(x), x, n)


############# Factorial
def factorial(n):
    if n <= 0:
        return 1
    else:
        return n * factorial(n - 1)


############# PROBLEMA: Encontrar el valor de la función en Xi+1 = 1
# Este es el que se va a usar para encontrar el error de truncamiento más adelante

problema = round(f(1), digitos) # Redondear esta vaina a 5 cifras

def residuo(n, h):
    print("EL RESIDUO")
    derivada = df(x, n+1)
    print(n+1)
    print(derivada)
    fxn = sp.lambdify(x, derivada, 'numpy')
    res_1 = (fxn(h) / factorial(n+1)) * pow(h, n+1)
    return res_1


############# Taylor
def taylor(Xi, h, orden):
    total = 0
    for i in range(orden):
        derivada = df(x, i)
        fxn = sp.lambdify(x, derivada, 'numpy')

        if (i == 0):
            resultado = f(Xi)
        elif (i == 1):  # si sólo se multiplica por h
            resultado = fxn(Xi) * h  # La función derivada * h
        else:
            resultado = (fxn(Xi) * h ** i) / factorial(i)  # Aquí empieza a dividir por el factorial

        total += round(resultado, digitos)
        print(derivada)
        print("resultado", resultado)
        print("residuo", residuo(i, h))

        print(f"Valor aproximado FINAL: {round(total, digitos)} | Error Truncamiento FINAL: {round(problema - total, digitos)}")

    return total

# ******************** acá inicia todo ********************
# el orden es hasta cuál factor se quiere llegar. En este caso al orden 3 de la serie
# Xi y h el problema da los valores
taylor(Xi, h, 3)
