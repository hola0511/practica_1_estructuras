import random
from organismos import Depredador, Presa

def mover_presas(matriz, posiciones, direcciones):
    if not posiciones:
        return
    x, y = posiciones[0]
    if isinstance(matriz[x][y], Presa):
        def mover_recursivo(dirs):
            if not dirs:
                return
            dx, dy = dirs[0]
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(matriz) and 0 <= ny < len(matriz) and matriz[nx][ny] is None:
                if random.random() < matriz[x][y].reproduccion_probabilidad:
                    matriz[nx][ny] = Presa()
                return
            mover_recursivo(dirs[1:])
        mover_recursivo(direcciones)
    mover_presas(matriz, posiciones[1:], direcciones)

def mover_depredadores(matriz, posiciones, direcciones):
    if not posiciones:
        return
    x, y = posiciones[0]
    if isinstance(matriz[x][y], Depredador):
        depredador = matriz[x][y]
        def mover_recursivo(dirs):
            if not dirs:
                return
            dx, dy = dirs[0]
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(matriz) and 0 <= ny < len(matriz):
                if isinstance(matriz[nx][ny], Presa):
                    matriz[nx][ny] = depredador
                    depredador.cazar()
                    matriz[x][y] = None
                    return
                elif matriz[nx][ny] is None:
                    matriz[nx][ny] = depredador
                    matriz[x][y] = None
                    return
            mover_recursivo(dirs[1:])
        mover_recursivo(direcciones)
        if not depredador.sobrevivir():
            matriz[x][y] = None
    mover_depredadores(matriz, posiciones[1:], direcciones)
