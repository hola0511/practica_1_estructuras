import random
from organismos import Depredador, Presa


def mover_presas(matriz, x, y):
    if not isinstance(matriz[x][y], Presa):
        return

    direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    random.shuffle(direcciones)

    for dx, dy in direcciones:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(matriz) and 0 <= ny < len(matriz) and matriz[nx][ny] is None:
            if random.random() < matriz[x][y].reproduccion_probabilidad:
                matriz[nx][ny] = Presa()
            return


def mover_depredadores(matriz, x, y):
    if not isinstance(matriz[x][y], Depredador):
        return
    depredador = matriz[x][y]

    direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    random.shuffle(direcciones)

    for dx, dy in direcciones:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(matriz) and 0 <= ny < len(matriz):
            if isinstance(matriz[nx][ny], Presa):
                matriz[nx][ny] = depredador  # Caza la presa
                depredador.cazar()
                matriz[x][y] = None
                return
            elif matriz[nx][ny] is None:
                matriz[nx][ny] = depredador
                matriz[x][y] = None
                return

    if not depredador.sobrevivir():
        matriz[x][y] = None  # Depredador muere si no caza
