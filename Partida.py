class Partida():
    def __init__(self,dificultad,vidas,pistas,tiempo):
        self.dificultad = dificultad
        self.vidas = vidas
        self.pistas = pistas
        self.tiempo = tiempo
    def mostrar(self):
        print(f"Usted seleccionó la dificultad {self.dificultad} con {self.vidas} vidas, con {self.pistas} pistas y {self.tiempo}")
        print()
        print(f"Hoy 5 de marzo de 2021, la Universidad sigue en cuarentena (esto no es novedad), lo que sí es novedad es que se robaron un Disco Duro de la Universidad del cuarto de redes que tiene toda la información de SAP de estudiantes, pagos y  asignaturas. Necesitamos que nos ayudes a recuperar el disco, para eso tienes {self.tiempo} minutos, antes de que el servidor se caiga y no se pueda hacer más nada. ¿Aceptas el reto?")

