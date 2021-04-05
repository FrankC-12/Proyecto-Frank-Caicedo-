import random
import requests
import json
response = requests.get("https://api-escapamet.vercel.app/")
data = json.loads(response.text)
def adivinanzas(inventarios):
    preguntas = [(data[0]["objects"][2]["game"]["questions"][0]["question"]), (data[0]["objects"][2]["game"]["questions"][1]["question"]), (data[0]["objects"][2]["game"]["questions"][2]["question"])]
    adivinanza = random.choice(preguntas)
    contador = 0
    while True:
        if adivinanza == data[0]["objects"][2]["game"]["questions"][0]["question"]:
            print(adivinanza)
            respuesta = input("Respuesta: ")
            if respuesta in (data[0]["objects"][2]["game"]["questions"][0]["answers"]):
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
                    if inventarios[0]["Pistas"] <= 0:
                        print("Ya no tienes pistas en tu inventario")
                    else:
                        pista = input("Usar pista: \n1.Sí \n2.No \n> ")
                        while (not pista.isnumeric()) or (int(pista) not in range(1,3)):
                            pista = input("Introduzca opción válida. Usar pista: \n1.Sí \n2.No \n> ")
                        if pista == "1":
                            pistas = inventarios[0]["Pistas"] - 1
                            inventarios[0]["Pistas"] = pistas
                            print(f"Te quedan {pistas} pistas en tu inventario")
                            if contador == 0:
                                print(data[0]["objects"][2]["game"]["questions"][0]["clue_1"])
                                contador +=1
                            elif contador == 1:
                                print(data[0]["objects"][2]["game"]["questions"][0]["clue_2"])
                                contador += 1
                            elif contador == 2:
                                print(data[0]["objects"][2]["game"]["questions"][0]["clue_3"])
                                contador +=1
                            else:
                                print("Usaste todas las pistas")
                        else:
                            True

        elif adivinanza == data[0]["objects"][2]["game"]["questions"][1]["question"]:
            print(adivinanza)
            respuesta = input("Respuesta: ")
            if respuesta in (data[0]["objects"][2]["game"]["questions"][1]["answers"]):
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
                    if inventarios[0]["Pistas"] <= 0:
                        print("Ya no tienes pistas en tu inventario")
                    else:
                        pista = input("Usar pista: \n1.Sí \n2.No \n> ")
                        while (not pista.isnumeric()) or (int(pista) not in range(1,3)):
                            pista = input("Introduzca opción válida. Usar pista: \n1.Sí \n2.No \n> ")
                        if pista == "1":
                            pistas = inventarios[0]["Pistas"] - 1
                            inventarios[0]["Pistas"] = pistas
                            print(f"Te quedan {pistas} pistas en tu inventario")
                            if contador == 0:
                                print(data[0]["objects"][2]["game"]["questions"][0]["clue_1"])
                                contador +=1
                            elif contador == 1:
                                print(data[0]["objects"][2]["game"]["questions"][0]["clue_2"])
                                contador += 1
                            elif contador == 2:
                                print(data[0]["objects"][2]["game"]["questions"][0]["clue_3"])
                                contador +=1
                            else:
                                print("Usaste todas las pistas")
                        else:
                            True
        elif adivinanza == data[0]["objects"][2]["game"]["questions"][2]["question"]:
            print(adivinanza)
            respuesta = input("Respuesta: ")
            if respuesta in (data[0]["objects"][2]["game"]["questions"][2]["answers"]):
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
                    if inventarios[0]["Pistas"] <= 0:
                        print("Ya no tienes pistas en tu inventario")
                    else:
                        pista = input("Usar pista: \n1.Sí \n2.No \n> ")
                        

                        while (not pista.isnumeric()) or (int(pista) not in range(1,3)):
                            pista = input("Introduzca opción válida. Usar pista: \n1.Sí \n2.No \n> ")
                        if pista == "1":
                            pistas = inventarios[0]["Pistas"] - 1
                            inventarios[0]["Pistas"] = pistas
                            print(f"Te quedan {pistas} pistas en tu inventario")
                            if contador == 0:
                                print(data[0]["objects"][2]["game"]["questions"][0]["clue_1"])
                                contador +=1
                            elif contador == 1:
                                print(data[0]["objects"][2]["game"]["questions"][0]["clue_2"])
                                contador += 1
                            elif contador == 2:
                                print(data[0]["objects"][2]["game"]["questions"][0]["clue_3"])
                                contador +=1
                            else:
                                print("Usaste todas las pistas")
                        else:
                            True
    

