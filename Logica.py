import random
import requests
import json

response = requests.get("https://api-escapamet.vercel.app/")
data = json.loads(response.text)
def Logica(inventarios):
    preguntas = (data[2]["objects"][0]["game"]["questions"])
    def selectRandom(preguntas):
        return random.choice(preguntas)
    pregunta = selectRandom(preguntas)
    if pregunta == (data[2]["objects"][0]["game"]["questions"][0]):
        print(pregunta)
        r = 70
        while True:
            respuesta = input("Respuesta: ")
            while (not respuesta.isnumeric()):
                respuesta = input("Introduzca dato válido. Respuesta: ")
            if int(respuesta) != 70:
                print("Respuesta incorrecta")
                vidas = inventarios[0]["Vidas"] - 1
                inventarios[0]["Vidas"] = vidas
                print(f"Te quedan {vidas} vidas")
                if  inventarios[0]["Vidas"] <= 0:
                    print("Perdiste te quedaste sin vidas")
                    exit()
                else:
                    True 
            else:
                print(f"Respuesta correcta el resultado es {r}")
                print("FELICIDADES HAS GANADO!!!!!!")
                break
    elif pregunta == (data[2]["objects"][0]["game"]["questions"][1]):
        print(pregunta)
        r = 41
        while True:
            respuesta = input("Respuesta: ")
            while (not respuesta.isnumeric()):
                respuesta = input("Introduzca opción válida. Respuesta: ")
            if int(respuesta) != 41:
                print("Respuesta incorrecta")
                vidas = inventarios[0]["Vidas"] - 1
                inventarios[0]["Vidas"] = vidas
                print(f"Te quedan {vidas} vidas")
                if inventarios[0]["Vidas"] <= 0:
                    print("Te quedaste sin vidas")
                    exit()
                else:
                    True
            else:
                print(f"Respuesta correcta el resultado es {respuesta}")
                print("FELICIDADES HAS GANADO!!!!!!")
                break
    
