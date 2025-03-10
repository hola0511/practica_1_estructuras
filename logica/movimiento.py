import random
from typing import Optional
from organismos import Organismo, Depredador, Presa

def mover_presas(matriz: list[list[Optional[Organismo]]], posiciones: list[tuple[int, int]], direcciones: list[tuple[int, int]]) -> None:
    if not posiciones:
        return
    x, y = posiciones[0]
    if isinstance(matriz[x][y], Presa):
        def mover(dirs: list[tuple[int, int]]) -> None:
            if not dirs:
                return
            dx, dy = dirs[0]
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(matriz) and 0 <= ny < len(matriz) and matriz[nx][ny] is None:
                if random.random() < matriz[x][y].reproduccion_probabilidad:
                    matriz[nx][ny] = Presa()
                return
            mover(dirs[1:])
        mover(direcciones)
    mover_presas(matriz, posiciones[1:], direcciones)

def mover_depredadores(matriz: list[list[Optional[Organismo]]], posiciones: list[tuple[int, int]], direcciones: list[tuple[int, int]]) -> None:
    if not posiciones:
        return
    x, y = posiciones[0]
    if isinstance(matriz[x][y], Depredador):
        depredador = matriz[x][y]
        def mover(dirs: list[tuple[int, int]]) -> None:
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
            mover(dirs[1:])
        mover(direcciones)
        if not depredador.sobrevivir():
            matriz[x][y] = None
    mover_depredadores(matriz, posiciones[1:], direcciones)
