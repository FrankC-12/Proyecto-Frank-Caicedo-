from sympy import Symbol
from scipy.misc import derivative
from sympy import cos, sin, tan
from math import pi
from random import randint
import requests
import json
import random
response = requests.get("https://api-escapamet.vercel.app/")
data = json.loads(response.text)
def derivada(inventarios):
    derivadas = [data[1]["objects"][1]["game"]["questions"][0]["question"],data[1]["objects"][1]["game"]["questions"][1]["question"],data[1]["objects"][1]["game"]["questions"][2]["question"] ]
    derivada = random.choice(derivadas)
    x = Symbol("x")
    if derivada == data[1]["objects"][1]["game"]["questions"][0]["question"]:
        print(derivada)
        f = lambda x: (sin(x)/2)
        z = (round((derivative(f,pi,dx=1e-9))))
        print("Redondee su respuesta a número entero")
        while True:
            respuesta = input("Respuesta: ")
            if int(respuesta) == z:
                print(f"Respuesta correcta el resultado es {z}")
                break
            else:
                print("Respuesta incorrecta")
                vidas = inventarios[0]["Vidas"] - 0.25
                inventarios[0]["Vidas"] = vidas
                print(f"Te quedan {vidas} vidas en tu inventario")
                print("Respuesta incorrecta")
                vidas = inventarios[0]["Vidas"] - 0.25
                inventarios[0]["Vidas"] = vidas
                print(f"Te quedan {vidas} vidas en tu inventario")
                if inventarios[0]["Vidas"] <= 0:
                    print("Has pérdido")
                    exit()
                else:
                    True
    elif derivada == data[1]["objects"][1]["game"]["questions"][1]["question"]:
        print(derivada)
        f = lambda x: ((cos(x))/2 - (tan(x))/5)
        z = (round((derivative(f,pi,dx=1e-8))))
        print("Redondee su respuesta a número entero")
        while True:
            respuesta = input("Respuesta: ")
            if int(respuesta) == z:
                print(f"Respuesta correcta el resultado es {z}")
                break
            else:
                print("Respuesta incorrecta")
                vidas = inventarios[0]["Vidas"] - 0.25
                inventarios[0]["Vidas"] = vidas
                print(f"Te quedan {vidas} vidas en tu inventario")
                if inventarios[0]["Vidas"] <= 0:
                    print("Has pérdido")
                    exit()
                else:
                    True

    else:
        print(derivada)
        f = lambda x: (sin(x)/5 - tan(x))
        z = (round((derivative(f,pi/3,dx=1e-8))))
        print("Redondee su respuesta a número entero")
        while True:
            respuesta = input("Respuesta: ")
            if int(respuesta) == z:
                print(f"Respuesta correcta el resultado es {z}")
                break
            else:
                print("Respuesta incorrecta")
                vidas = inventarios[0]["Vidas"] - 0.25
                inventarios[0]["Vidas"] = vidas
                print(f"Te quedan {vidas} vidas en tu inventario")
                print("Respuesta incorrecta")
                vidas = inventarios[0]["Vidas"] - 0.25
                inventarios[0]["Vidas"] = vidas
                print(f"Te quedan {vidas} vidas en tu inventario")
                if inventarios[0]["Vidas"] <= 0:
                    print("Has pérdido")
                    exit()
                else:
                    True
