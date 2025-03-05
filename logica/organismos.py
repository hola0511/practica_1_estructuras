class Organismo:
    def __init__(self, tipo):
        self.tipo = tipo

    def __str__(self):
        return self.tipo

class Depredador(Organismo):
    def __init__(self):
        super().__init__("D")
        self.energia = 3

    def cazar(self):
        self.energia = min(self.energia + 2, 5)

    def sobrevivir(self):
        self.energia -= 1
        return self.energia > 0

class Presa(Organismo):
    def __init__(self):
        super().__init__("P")
        self.reproduccion_probabilidad = 0.2

class Planta(Organismo):
    def __init__(self):
        super().__init__("*")
