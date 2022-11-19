# PequeñoFermat.Py
# Lucas Berredo de la Colina - 9/11/22
# Uso del Pequeño Teorema de Fermat para comprobar si es primo o no
# Requisitos
import random

# Input del usuario
numero = int(input("\nNúmero natural mayor que 1 a comprobar\n"))
iteraciones = int(input("\n\n¿Cuántas veces se repite la prueba?\n"))

# Función principal
def isprime_fermat(n, iterations):
    b = 0
    for i in range(iterations):
        a = random.randint(2, n-1)
        if (a**(n-1) % n) == 0:         # Ligeramente reescrito para ser interpretado correctamente
            b = 1
    return b

# Conclusión
if isprime_fermat(numero, iteraciones) != 1:
    print("\nEl número es primo según el Pequeño Teorema de Fermat")
else:
    print("\nEl número no es primo según el Pequeño Teorema de Fermat")
