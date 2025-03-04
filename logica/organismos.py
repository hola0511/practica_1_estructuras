class Organismo:
    def __init__(self, tipo):
        self.tipo = tipo

    def __str__(self):
        return self.tipo

class Depredador(Organismo):
    def __init__(self):
        super().__init__("D")
        self.energia = 3  # Depredador muere si su energía llega a 0

    def cazar(self):
        self.energia = min(self.energia + 2, 5)  # Gana energía al cazar

    def sobrevivir(self):
        self.energia -= 1
        return self.energia > 0

class Presa(Organismo):
    def __init__(self):
        self.reproduccion_probabilidad = 0.3
        super().__init__("P")

class Planta(Organismo):
    def __init__(self):
        super().__init__("*")
