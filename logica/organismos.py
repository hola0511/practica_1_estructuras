class Organismo:
    def __init__(self, tipo: str) -> None:
        self.tipo = tipo

    def __str__(self) -> str:
        return self.tipo

class Depredador(Organismo):
    def __init__(self) -> None:
        super().__init__("D")
        self.energia: int = 3

    def cazar(self) -> None:
        self.energia = min(self.energia + 2, 5)

    def sobrevivir(self) -> bool:
        self.energia -= 1
        return self.energia > 0

class Presa(Organismo):
    def __init__(self) -> None:
        super().__init__("P")
        self.reproduccion_probabilidad: float = 0.2

class Planta(Organismo):
    def __init__(self) -> None:
        super().__init__("*")