#!/usr/bim/env python3

import random

# Add control de errores (excepciones si no se introduce el valor esperado)
while True:
    try:
        cadena = input("Introduce un número: ")
        N = int(cadena)
        break  # Salimos del bucle si la conversión es exitosa
    except ValueError:
        print("Esperaba un número entero. Inténtalo de nuevo.")


# tamaño de la matriz (N):
print(f"La matriz a crear será de {N}x{N}.")




print(f"Un valor aleatorio entre 0 y 9: {random.randint(0,9)}")