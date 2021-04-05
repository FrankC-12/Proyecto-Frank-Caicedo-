class Usuario():
    def __init__(self,nombre,contraseña,edad,avatar):
        self.nombre = nombre
        self.contraseña = contraseña
        self.edad = edad
        self.avatar = avatar
    def mostrar(self):
        print(f"Usuario: {self.nombre} \nContraseña: {self.contraseña} \nEdad: {self.edad} \nAvatar: {self.avatar}")