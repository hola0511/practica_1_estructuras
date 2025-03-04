from ecosistema import crear_matriz, imprimir_matriz
from simulacion import actualizar_ecosistema

if __name__ == "__main__":
    n = 5  # Tamaño de la matriz
    ciclos = 5  # Número de ciclos de simulación
    matriz = crear_matriz(n)

    imprimir_matriz(matriz)
    actualizar_ecosistema(matriz, ciclos)
