import random
from organismos import Depredador, Presa, Planta


def crear_matriz(n, densidad_presas=0.1, densidad_depredadores=0.15, densidad_plantas=0.3):
    matriz = [[None for _ in range(n)] for _ in range(n)]

    def colocar_organismos(clase, densidad):
        total = int(n * n * densidad)
        posiciones = random.sample([(i, j) for i in range(n) for j in range(n)], total)
        for x, y in posiciones:
            matriz[x][y] = clase()

    colocar_organismos(Presa, densidad_presas)
    colocar_organismos(Depredador, densidad_depredadores)
    colocar_organismos(Planta, densidad_plantas)

    return matriz


def imprimir_matriz(matriz):
    for fila in matriz:
        print("[" + " ".join(str(c) if c else "." for c in fila) + "]")
    print()
