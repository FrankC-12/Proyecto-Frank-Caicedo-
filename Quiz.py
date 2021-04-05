import random
import requests
import json
response = requests.get("https://api-escapamet.vercel.app/")
data = json.loads(response.text)
def Quiz(inventarios):
    preguntas = [(data[2]["objects"][1]["game"]["questions"][0]["question"]), (data[2]["objects"][1]["game"]["questions"][1]["question"]), (data[2]["objects"][1]["game"]["questions"][2]["question"])]
    def selectRandom(preguntas):
        return random.choice(preguntas)
    pregunta = selectRandom(preguntas)
    contador = 0
    while True:
        if pregunta == (data[2]["objects"][1]["game"]["questions"][0]["question"]):
            print(pregunta)
            A = data[2]["objects"][1]["game"]["questions"][0]["correct_answer"]
            B = data[2]["objects"][1]["game"]["questions"][0]["answer_2"]
            C = data[2]["objects"][1]["game"]["questions"][0]["answer_3"]
            D = data[2]["objects"][1]["game"]["questions"][0]["answer_4"]
            print(f"A.{A}\nB.{B}\nC.{C}\nD.{D}")
            seleccione = input("Introduzca respuesta: ").upper()
            while seleccione.isnumeric():
                print("Introduzca opción válida")
                seleccione = input("Introduzca respuesta: ").upper()
            if seleccione != "A":
                print("Respuesta incorrecta intente de nuevo")
                vidas = inventarios[0]["Vidas"] - 0.5
                inventarios[0]["Vidas"] = vidas
                print(f"Te quedan {vidas} vidas")
                if inventarios[0]["Vidas"] <= 0:
                    print("Te quedaste sin vidas")
                    exit()
                else:
                    pista = input("Usar pista: \n1.Sí \n2.No \n> ")
                    while (not pista.isnumeric()) or (int(pista) not in range(1,3)):
                        pista = input("Introduzca opción válida. Usar pista: \n1.Sí \n2.No \n> ")
                    if pista == "1":
                        if inventarios[0]["Pistas"] <= 0:
                            print("Ya no tienes pistas en tu inventario")
                        else:
                            if contador == 0:
                                print(data[2]["objects"][1]["game"]["questions"][0]["clue_1"])
                                pistas = inventarios[0]["Pistas"] - 1
                                inventarios[0]["Pistas"] = pistas 
                                print(f"Te quedan {pistas} pistas en tu inventario")
                                contador +=1
                            else:
                                print("Usaste todas las pistas")
                    else:
                        True
            else:
                print("FELICIDADES HAS GANADO !!!!!")
                print()
                break
        elif pregunta == (data[2]["objects"][1]["game"]["questions"][1]["question"]) :
            print(pregunta)
            A = data[2]["objects"][1]["game"]["questions"][1]["correct_answer"]
            B = data[2]["objects"][1]["game"]["questions"][1]["answer_2"]
            C = data[2]["objects"][1]["game"]["questions"][1]["answer_3"]
            D = data[2]["objects"][1]["game"]["questions"][1]["answer_4"]
            print(f"A.{A}\nB.{B}\nC.{C}\nD.{D}")
            seleccione = input("Introduzca respuesta: ").upper()
            while seleccione.isnumeric():
                print("Introduzca opción válida")
                seleccione = input("Introduzca respuesta: ").upper()
            if seleccione != "A":
                print("Respuesta incorrecta intente de nuevo")
                vidas = inventarios[0]["Vidas"] - 0.5
                inventarios[0]["Vidas"] = vidas
                print(f"Te quedan {vidas} vidas")
                if inventarios[0]["Vidas"] <= 0:
                    print("Te quedaste sin vidas")
                    exit()
                else:
                    pista = input("Usar pista: \n1.Sí \n2.No \n> ")
                    while (not pista.isnumeric()) or (int(pista) not in range(1,3)):
                        pista = input("Introduzca opción válida. Usar pista: \n1.Sí \n2.No \n> ")
                    if pista == "1":
                        if inventarios[0]["Pistas"] <= 0:
                            print("Ya no tienes pistas en tu inventario")
                        else:
                            if contador == 0:
                                print(data[2]["objects"][1]["game"]["questions"][1]["clue_1"])
                                pistas = inventarios[0]["Pistas"] - 1
                                inventarios[0]["Pistas"] = pistas 
                                print(f"Te quedan {pistas} pistas en tu inventario")
                                contador +=1
                            else:
                                print("Usaste todas las pistas")
                        print(pregunta)
                        seleccione = input("Introduzca respuesta: ").upper()
                    else:
                        True             
            else:
                print("FELICIDADES HAS GANADO !!!!!")
                print()
                break
        else:
            print(pregunta)
            A = data[2]["objects"][1]["game"]["questions"][2]["correct_answer"]
            B = data[2]["objects"][1]["game"]["questions"][2]["answer_2"]
            C = data[2]["objects"][1]["game"]["questions"][2]["answer_3"]
            D = data[2]["objects"][1]["game"]["questions"][2]["answer_4"]
            print(f"A.{A}\nB.{B}\nC.{C}\nD.{D}")
            seleccione = input("Introduzca respuesta: ").upper()
            while seleccione.isnumeric():
                print("Introduzca opción válida")
                seleccione = input("Introduzca respuesta: ").upper()
            if seleccione != "A":
                print("Respuesta incorrecta intente de nuevo")
                vidas = inventarios[0]["Vidas"] - 0.5
                inventarios[0]["Vidas"] = vidas
                print(f"Te quedan {vidas} vidas")
                if inventarios[0]["Vidas"] <= 0:
                    print("Te quedaste sin vidas")
                    exit()
                else:
                    pista = input("Usar pista: \n1.Sí \n2.No \n> ")
                    while (not pista.isnumeric()) or (int(pista) not in range(1,3)):
                        pista = input("Introduzca opción válida. Usar pista: \n1.Sí \n2.No \n> ")
                    if pista == "1":
                        if inventarios[0]["Pistas"] <= 0:
                            print("Ya no tienes pistas en tu inventario")
                        else: 
                            if contador == 0:
                                print(data[2]["objects"][1]["game"]["questions"][2]["clue_1"])
                                pistas = inventarios[0]["Pistas"] - 1
                                inventarios[0]["Pistas"] = pistas 
                                print(f"Te quedan {pistas} pistas en tu inventario")
                            else:
                                print("Usaste todas las pistas")
                        print(pregunta)
                        seleccione = input("Introduzca respuesta: ").upper()
                    else:
                        True
            else:
                print("FELICIDADES HAS GANADO !!!!!")
                print()
                break
        
        

