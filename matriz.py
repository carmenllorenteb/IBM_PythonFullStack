#!/usr/bim/env python3

import random


def crea_matriz(n):
    """
    Genera una matriz cuadrada de tamaño NxN y la rellena con números aleatorios entre 0 y 9.
    """
    matriz = []
    for _ in range(n):
        fila = []
        for _ in range(n):
            fila.append(random.randint(0, 9))
        matriz.append(fila)
    return matriz

def imprime_matriz(matriz):
    """
    Imprime la matriz pasada como argumento de forma clásica
    """

    for fila in matriz:
        print("|", end='')
        for item in fila:
            print(f" {item} ", end='')
        print("|")


if __name__ == "__main__":
    
    # Add control de errores (excepciones si no se introduce el valor esperado)
    while True:
        try:
            cadena = input("Introduce un número: ")
            N = int(cadena)
            break  # Salimos del bucle si la conversión es exitosa
        except ValueError:
            print("Esperaba un número entero. Inténtalo de nuevo.")


    # Tamaño de la matriz (N):
    print(f"La matriz a crear será de {N}x{N}.")

    m = crea_matriz(N)

    imprime_matriz(m)