import random
import requests
import json
import string
lista = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
response = requests.get("https://api-escapamet.vercel.app/")
data = json.loads(response.text)
def Criptograma(inventarios):   
    x = (data[1]["objects"][2]["game"]["questions"])
    def selectRandom(preguntas):
        return random.choice(x)
    pregunta = selectRandom(x)
    while True: 
        if pregunta == (data[1]["objects"][2]["game"]["questions"][0]):
            print(f"{lista[24:27]+lista[0:24]}")
            cambio = 2 
            texto = "si te graduas pisas el samán"
            encriptar = ""
            for c in texto:
                if c.islower():
                    c_unicode = ord(c)
                    c_index = ord(c) - ord("a")
                    new_index = (c_index + cambio) % 26
                    new_unicode = new_index + ord("a")
                    new_character = chr(new_unicode)
                    encriptar = encriptar + new_character
                else:
                    encriptar += c
            print(f"Texto: {encriptar}")
            respuesta = input("Respuesta: ").lower()
            while respuesta.isnumeric() or respuesta != texto:
                print("Incorrecto")
                if inventarios[0]["Vidas"] <= 0:
                    print("Has perdido")
                    exit()
                else:
                    vidas = inventarios[0]["Vidas"] - 1
                    inventarios[0]["Vidas"] = vidas
                    print(f"Te quedan {vidas} vidas")
            print(f"Correcto la frase es {texto}")
        elif pregunta == (data[1]["objects"][2]["game"]["questions"][1]):
            print(f"{lista[21:27]+lista[0:21]}")
            cambio = 5
            texto ="si te graduas pisas el samán"
            encriptar = ""
            for c in texto:
                if c.islower():
                    c_unicode = ord(c)
                    c_index = ord(c) - ord("a")
                    new_index = (c_index + cambio) % 26
                    new_unicode = new_index + ord("a")
                    new_character = chr(new_unicode)
                    encriptar = encriptar + new_character
                else:
                    encriptar += c
            print(f"Texto: {encriptar}")
            respuesta = input("Respuesta: ").lower()
            while respuesta.isnumeric() or respuesta != texto:
                print("Incorrecto")
                if inventarios[0]["Vidas"] <= 0:
                    print("Has perdido")
                    exit()
                else:
                    vidas = inventarios[0]["Vidas"] - 1
                    inventarios[0]["Vidas"] = vidas
                    print(f"Te quedan {vidas} vidas")
            print(f"Correcto la frase es {texto}")
        else:
            print(f"{lista[20:27]+lista[0:20]}")
            cambio = 6
            texto = "si te graduas pisas el samán"
            encriptar = ""
            for c in texto:
                if c.islower():
                    c_unicode = ord(c)
                    c_index = ord(c) - ord("a")
                    new_index = (c_index + cambio) % 26
                    new_unicode = new_index + ord("a")
                    new_character = chr(new_unicode)
                    encriptar = encriptar + new_character
                else:
                    encriptar += c
            print(f"Texto: {encriptar}")

            respuesta = input("Respuesta: ").lower()
            while respuesta.isnumeric() or respuesta != texto:
                print("Incorrecto")
                if inventarios[0]["Vidas"] <= 0:
                    print("Has perdido")
                    exit()
                else:
                    vidas = inventarios[0]["Vidas"] - 1
                    inventarios[0]["Vidas"] = vidas
                    print(f"Te quedan {vidas} vidas")
                 
            print(f"Correcto la frase es {texto}")
        break


