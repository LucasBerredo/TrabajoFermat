# MillerRabin.py
# Lucas Berredo de la Colina - 11/10/22
# Comprobación de primos por Miller-Rabin
# Requisitos
import random

# Input del usuario
numero = int(input("\nNúmero impar mayor que 2 a comprobar\n"))
iteraciones = int(input("\n\n¿Cuántas veces se repite la prueba?\n"))

# Función principal
def esprimo_MillerRabin(n, t):
    s, d = encuentra_s_y_d(n)
    for i in range(t):                         # La prueba se realiza t veces (t=times)
        a = random.randint(2, n-2)             # Normalmente se utilizaría un aleatorio entre 2 y n-1, pero por la función randint() incluye el término superior
        x = a**d % n
        if prueba_1(x) or prueba_2(n, s, x):
            return True
        else:
            return False

def prueba_1(x):                               # Este código podría llamarse en línea, pero el objetivo es legibilidad
    if x == 1:
        return True


def prueba_2(n, s, x):                         # Esta prueba es la más larga
    for i in range(s-1):
        if x == n - 1:
            return True
        x = x**2 % n                           # Nos ahorramos un else al poner esto. Sin él, no se repetiría la prueba y daría que ningún numero es primo 
    return False
        

def encuentra_s_y_d(n):                        # Esta función prueba 1 a 1 todas las combinaciones de s y d posibles. Dado el gran número, es más eficiente que un aleatorio
    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1                                # Este operador borra el último dígito binario. De esta forma se consigue lo mismo que un bucle for y -2**i 
        s += 1
    return s, d

# Conclusión
if esprimo_MillerRabin(numero, iteraciones) == 1:
    print("\nEl número", numero, "es primo según la prueba de Miller-Rabin")
else:
    print("\nEl número", numero, "no es primo según la prueba de Miller-Rabin")
