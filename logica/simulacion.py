import random
from movimiento import mover_presas, mover_depredadores
from organismos import Planta
from ecosistema import imprimir_matriz

def regenerar_plantas(matriz, posiciones, cantidad):
    if cantidad == 0 or not posiciones:
        return
    x, y = posiciones.pop()
    matriz[x][y] = Planta()
    regenerar_plantas(matriz, posiciones, cantidad - 1)

def actualizar_ecosistema(matriz, ciclos, actual=0):
    if actual == ciclos:
        return

    posiciones = [(i, j) for i in range(len(matriz)) for j in range(len(matriz))]
    direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    random.shuffle(direcciones)

    mover_presas(matriz, posiciones, direcciones)
    mover_depredadores(matriz, posiciones, direcciones)
    regenerar_plantas(matriz, random.sample(posiciones, len(posiciones)), int(len(posiciones) * 0.05))

    imprimir_matriz(matriz)
    actualizar_ecosistema(matriz, ciclos, actual + 1)
