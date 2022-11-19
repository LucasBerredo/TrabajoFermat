# GeneradorEspiralFermat.py
# Lucas Berredo de la Colina - 9/11/22
# Generador-Ultimo-Teorema-Fermat.py
# Este programa sirve para calcular números que cumplen el Ultimo Teorema de Fermat y representarlos graficamente

# Requisitos: math, numpy, matplotlib
from math import sqrt, ceil, sin, cos
import matplotlib.pyplot as plt

# Generador de numeros
def UltimoTeorema(resultados=500, a=0.5, paso=0.1):
    # Inicializo valores
    theta = 0
    r1 = 0
    r2 = 0
    X1s = []
    Y1s = []
    X2s = []
    Y2s = []
    # Calculo valores en polares
    for i in range(resultados):
        theta = i*paso
        r1 = a**2+sqrt(theta)
        r2 = a**2-sqrt(theta)
        # Paso de polares a cartesianas
        x1 = r1*cos(theta)
        y1 = r1*sin(theta)
        x2 = r2*cos(theta)
        y2 = r2*sin(theta)
        # Añadimos a valores de retorno
        X1s.append(x1)
        Y1s.append(y1)
        X2s.append(x2)
        Y2s.append(y2)
    # Devolvemos valores
    return X1s, Y1s, X2s, Y2s

# Representacion grafica
X1s, Y1s, X2s, Y2s = UltimoTeorema()        # Introduciendo valores para las variables correspondientes, se puede cambiar el comportamiento
plt.plot(X1s, Y1s)
plt.plot(X2s, Y2s)
plt.title("Espiral de Fermat")
plt.show()
