import random
from typing import Optional

from organismos import Organismo, Depredador, Presa, Planta

def inicializar_matriz( n: int, fila: int = 0, col: int = 0, matriz: Optional[list[list[Optional[Organismo]]]] = None) -> list[list[Optional[Organismo]]]:
    if matriz is None:
        matriz = []
    if fila == n:
        return matriz
    if col == 0:
        matriz.append([])
    matriz[fila].append(None)
    if col == n - 1:
        return inicializar_matriz(n, fila + 1, 0, matriz)
    return inicializar_matriz(n, fila, col + 1, matriz)

def generar_posiciones(n: int, i: int = 0, j: int = 0, acumulador: Optional[list[tuple[int, int]]] = None)-> list[tuple[int, int]]:
    if acumulador is None:
        acumulador = []
    if i == n:
        return acumulador
    if j == n:
        return generar_posiciones(n, i + 1, 0, acumulador)
    acumulador.append((i, j))
    return generar_posiciones(n, i, j + 1, acumulador)

def colocar_organismos(matriz: list[list[Optional[Organismo]]], posiciones, clase, cantidad: int) -> None:
    if cantidad == 0 or not posiciones:
        return
    x, y = posiciones.pop()
    matriz[x][y] = clase()
    colocar_organismos(matriz, posiciones, clase, cantidad - 1)

def crear_matriz(n: int, densidad_presas: float=0.15, densidad_depredadores: float=0.1, densidad_plantas: float=0.3) -> list[list[Optional[Organismo]]]:
    matriz = inicializar_matriz(n)
    posiciones = random.sample(generar_posiciones(n), n * n)
    colocar_organismos(matriz, posiciones, Presa, int(n * n * densidad_presas))
    colocar_organismos(matriz, posiciones, Depredador, int(n * n * densidad_depredadores))
    colocar_organismos(matriz, posiciones, Planta, int(n * n * densidad_plantas))
    return matriz

def imprimir_matriz(matriz: list[list[Optional[Organismo]]]) -> None:
    def imprimir_filas(filas: list[list[Optional[Organismo]]]) -> None:
        if not filas:
            print()
            return
        print("[" + " ".join(str(c) if c else "." for c in filas[0]) + "]")
        imprimir_filas(filas[1:])
    imprimir_filas(matriz)
