import random
from organismos import Depredador, Presa, Planta

def inicializar_matriz( n: int, fila=0, col=0, matriz=None):
    if matriz is None:
        matriz = []
    if fila == n:
        return matriz
    if col == 0:
        matriz.append([])
    matriz[fila].append(None)
    if col == n - 1:
        return inicializar_matriz(fila + 1, 0, n, matriz)
    return inicializar_matriz(fila, col + 1, n, matriz)

def generar_posiciones_recursivo( n: int,i=0, j=0, acumulador=None):
    if acumulador is None:
        acumulador = []
    if i == n:
        return acumulador
    if j == n:
        return generar_posiciones_recursivo(i + 1, 0, n, acumulador)
    acumulador.append((i, j))
    return generar_posiciones_recursivo(i, j + 1, n, acumulador)

def colocar_organismos_recursivo(matriz, posiciones, clase, cantidad):
    if cantidad == 0 or not posiciones:
        return
    x, y = posiciones.pop()
    matriz[x][y] = clase()
    colocar_organismos_recursivo(matriz, posiciones, clase, cantidad - 1)

def crear_matriz(n: int, densidad_presas=0.15, densidad_depredadores=0.1, densidad_plantas=0.3):
    matriz = inicializar_matriz(n=n)
    posiciones = random.sample(generar_posiciones_recursivo(n=n), n * n)
    colocar_organismos_recursivo(matriz, posiciones, Presa, int(n * n * densidad_presas))
    colocar_organismos_recursivo(matriz, posiciones, Depredador, int(n * n * densidad_depredadores))
    colocar_organismos_recursivo(matriz, posiciones, Planta, int(n * n * densidad_plantas))
    return matriz

def imprimir_matriz(matriz):
    def imprimir_filas_recursivo(filas):
        if not filas:
            print()
            return
        print("[" + " ".join(str(c) if c else "." for c in filas[0]) + "]")
        imprimir_filas_recursivo(filas[1:])
    imprimir_filas_recursivo(matriz)
