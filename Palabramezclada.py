import requests
import json
import random
from random import shuffle
response = requests.get("https://api-escapamet.vercel.app/")
data = json.loads(response.text)
def Palabra(inventarios):
    lista = [(data[4]["objects"][1]["game"]["questions"][0]["words"]), (data[4]["objects"][1]["game"]["questions"][1]["words"]), (data[4]["objects"][1]["game"]["questions"][2]["words"])]
    def selectRandom(lista):
        return random.choice(lista)
    palabras = selectRandom(lista)
    mezclada = []
    correctas = []
    while True:
        if palabras == (data[4]["objects"][1]["game"]["questions"][0]["words"]):
            for x in palabras:
                letras = []
                for y in x:
                    letras.append(y)
                    shuffle(letras)
                palabra = "".join(letras)
                mezclada.append(palabra)
            print(mezclada)
            print("Categoria de las palabras:")
            print(data[4]["objects"][1]["game"]["questions"][0]["category"])
            w = 0
            while w <= 4:
                respuesta = input("Respuesta: ")
                if respuesta in palabras:
                    print("Palabra correcta")
                    correctas.append(respuesta)
                    print(correctas)
                    w+=1
                else:
                    print("Palabra incorrecta")
                    if inventarios[0]["Vidas"] <= 0:
                        print("Has perdido")
                        exit()
                    else:
                        vidas = inventarios[0]["Vidas"] - 0.5
                        inventarios[0]["Vidas"] = vidas
                        print(f"Te quedan {vidas} vidas")
                        True

        elif palabras == (data[4]["objects"][1]["game"]["questions"][1]["words"]):
            for x in palabras:
                letras = []
                for y in x:
                    letras.append(y)
                    shuffle(letras)
                palabra = "".join(letras)
                mezclada.append(palabra)
            print(mezclada)
            print("Categoria de las palabras:")
            print(data[4]["objects"][1]["game"]["questions"][1]["category"])
            w = 0
            while w <= 4:
                respuesta = input("Respuesta: ")
                if respuesta in palabras:
                    print("Palabra correcta")
                    correctas.append(respuesta)
                    print(correctas)
                    w+=1
                else:
                    print("Palabra incorrecta")
                    if inventarios[0]["Vidas"] <= 0:
                        print("Has perdido")
                        exit()
                    else:
                        vidas = inventarios[0]["Vidas"] - 0.5
                        inventarios[0]["Vidas"] = vidas
                        print(f"Te quedan {vidas} vidas")
                        True
        else:
            for x in palabras:
                    letras = []
                    for y in x:
                        letras.append(y)
                        shuffle(letras)
                    palabra = "".join(letras)
                    mezclada.append(palabra)
            print(mezclada)
            print("Categoria de las palabras:")
            print(data[4]["objects"][1]["game"]["questions"][2]["category"])
            w = 0
            while w <= 4:
                
                respuesta = input("Respuesta: ").lower()
                if respuesta in palabras:
                    print("Palabra correcta")
                    correctas.append(respuesta)
                    print(correctas)
                    w+=1
                else:
                    print("Palabra incorrecta")
                    if inventarios[0]["Vidas"] <= 0:
                        print("Has perdido")
                        exit()
                    else:
                        vidas = inventarios[0]["Vidas"] - 0.5
                        inventarios[0]["Vidas"] = vidas
                        print(f"Te quedan {vidas} vidas")
                        True
        print("FELICIDADES HAS GANADO")
        break
