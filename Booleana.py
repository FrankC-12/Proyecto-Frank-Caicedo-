import random
import requests
import json
def booleana(inventarios):
    response = requests.get("https://api-escapamet.vercel.app/")
    data = json.loads(response.text)
    preguntas = [data[3]["objects"][0]["game"]["questions"][0]["question"], data[3]["objects"][0]["game"]["questions"][1]["question"] ]
    def selectRandom(preguntas):
        return random.choice(preguntas)
    pregunta = selectRandom(preguntas)
    while True:
        if pregunta == data[3]["objects"][0]["game"]["questions"][0]["question"]:
            print(pregunta)
            respuesta = input("Respuesta: ").title()
            while respuesta.isnumeric():
                respuesta = input("Introduzca dato válido.\nRespuesta: ").title()
            if respuesta == "False":
                print("Respuesta correcta") 
                break
            else:
                print("Respuesta incorrecta")
                vidas = inventarios[0]["Vidas"] - 0.5
                inventarios[0]["Vidas"] = vidas
                print(f"Te quedan {vidas} vidas")
                if inventarios[0]["Vidas"] <= 0:
                    print("Has pérdido")
                    exit()
                else:
                    True
        else:
            print(pregunta)
            respuesta = input("Respuesta: ").title()
            while respuesta.isnumeric():
                respuesta = input("Introduzca dato válido.\nRespuesta: ").title()
            if respuesta == "True":
                print("Respuesta correcta") 
                break
            else:
                print("Respuesta incorrecta")
                vidas = inventarios[0]["Vidas"] - 0.5
                inventarios[0]["Vidas"] = vidas
                print(f"Te quedan {vidas} vidas")
                if inventarios[0]["Vidas"] <= 0:
                    print("Has pérdido")
                    exit()
                else:
                    True