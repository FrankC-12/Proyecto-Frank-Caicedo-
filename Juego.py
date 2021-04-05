class Juego():
    def __init__(self,name,award,rules,requirement):
        self.name = name
        self.requirement = requirement
        self.rules = rules
        self.award = award 
    def mostrar(self):
        print(f"Nombre del juego: {self.name}\nReglas: {self.rules}\nPremio del juego: {self.award}\nRequerimiento: {self.requirement}")