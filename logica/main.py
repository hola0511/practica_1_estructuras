from ecosistema import crear_matriz, imprimir_matriz
from simulacion import actualizar_ecosistema

if __name__ == "__main__":
    n = 5
    ciclos = 8
    matriz = crear_matriz(n)
    actualizar_ecosistema(matriz, ciclos)
