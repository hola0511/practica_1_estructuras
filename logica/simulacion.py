from movimiento import mover_presas, mover_depredadores
from organismos import Depredador, Presa, Planta
from ecosistema import imprimir_matriz
import random


def regenerar_plantas(matriz, tasa=0.05):
    n = len(matriz)
    posiciones_vacias = [(i, j) for i in range(n) for j in range(n) if matriz[i][j] is None]
    random.shuffle(posiciones_vacias)
    for i in range(int(len(posiciones_vacias) * tasa)):
        x, y = posiciones_vacias[i]
        matriz[x][y] = Planta()


def actualizar_ecosistema(matriz, ciclos, actual=0):
    if actual == ciclos:
        return

    n = len(matriz)
    for x in range(n):
        for y in range(n):
            if isinstance(matriz[x][y], Presa):
                mover_presas(matriz, x, y)
            elif isinstance(matriz[x][y], Depredador):
                mover_depredadores(matriz, x, y)

    regenerar_plantas(matriz)
    imprimir_matriz(matriz)
    actualizar_ecosistema(matriz, ciclos, actual + 1)
