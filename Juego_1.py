from Juego import Juego
class Juego_1(Juego):
    def __init__(self,name,award,rules,requirement,message_requirement):
        Juego.__init__(self, name, award, rules,requirement)
        self.message_requirement = message_requirement
    def mostrar(self):
        print(f"Nombre del juego = {self.name} \nPista para usar objeto: {self.message_requirement}")