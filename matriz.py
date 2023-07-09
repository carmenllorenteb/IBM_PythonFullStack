#!/usr/bin/env python3

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


def suma_filas(matriz):
    """
    Sumamos las filas de la matriz dada 
    """
    suma = []

    for fila in matriz:
        suma.append(sum(fila))

    return suma

def suma_colums(matriz):
    """
    Sumamos las columnas de la matriz dada 
    """
    colums = []

    n = len(matriz)
    for j in range(n):
        suma = 0
        for i in range(n):
            suma += matriz[i][j]
        colums.append(suma)
    return colums


if __name__ == "__main__":
    
    # Add control de errores (excepciones si no se introduce el valor esperado)
    while True:
        try:
            cadena = input("Introduce el valor de N (tamaño matriz): ")
            N = int(cadena)

            if N < 1:
                raise ValueError("")

            break  # Salimos del bucle si la conversión es exitosa
        except ValueError:
            print("Esperaba un número entero positivo mayor que cero. Inténtalo de nuevo.")


    # Tamaño de la matriz (N):
    print(f"La matriz a crear será de {N}x{N}.")

    m = crea_matriz(N)

    # Imprimimos matriz:
    imprime_matriz(m)

    filas = []
    colums = []

    # Sumamos filas:
    filas = suma_filas(m)

    print(f"La suma de cada fila resulta en:\n")

    for n in filas:
        print(f"{n}")

    # Sumamos columnas:
    colums = suma_colums(m)

    print(f"\nLa suma de cada columna resulta en:\n")

    for n in colums:
        print(f"{n}")





