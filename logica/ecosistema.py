import random
from organismos import Depredador, Presa, Planta


def crear_matriz(n, densidad_presas=0.1, densidad_depredadores=0.15, densidad_plantas=0.3):
    matriz = [[None for _ in range(n)] for _ in range(n)]

    def colocar_organismos_recursivo(posiciones, clase, cantidad):
        if cantidad == 0 or not posiciones:
            return
        x, y = posiciones.pop()
        matriz[x][y] = clase()
        colocar_organismos_recursivo(posiciones, clase, cantidad - 1)

    posiciones = random.sample([(i, j) for i in range(n) for j in range(n)], n * n)
    colocar_organismos_recursivo(posiciones, Presa, int(n * n * densidad_presas))
    colocar_organismos_recursivo(posiciones, Depredador, int(n * n * densidad_depredadores))
    colocar_organismos_recursivo(posiciones, Planta, int(n * n * densidad_plantas))

    return matriz


def imprimir_matriz(matriz):
    def imprimir_filas_recursivo(filas):
        if not filas:
            print()
            return
        print("[" + " ".join(str(c) if c else "." for c in filas[0]) + "]")
        imprimir_filas_recursivo(filas[1:])

    imprimir_filas_recursivo(matriz)
