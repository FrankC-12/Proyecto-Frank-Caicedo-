import random
import requests
import json
response = requests.get("https://api-escapamet.vercel.app/")
data = json.loads(response.text)
def python(inventarios):
    x = [(data[0]["objects"][1]["game"]["questions"][0]["question"]), (data[0]["objects"][1]["game"]["questions"][1]["question"])]
    def selectRandom(preguntas):
        return random.choice(x)
    pregunta = selectRandom(x)
    while True:
        if pregunta == (data[0]["objects"][1]["game"]["questions"][0]["question"]):
            print(pregunta)
            pregunta = "tengo en mi cuenta 50,00$"
            r_1 = "[int(temp)for temp in temp_string.split() if temp.isdigit()]"  
            r_2 = "int(pregunta.replace(pregunta, '50'))"
            
            respuesta = input("Introduzca respuesta: ")
            if respuesta == r_1 or respuesta == r_2 :
                print("Correcto")
                break
            else:
                print("Incorrecto")
                if inventarios[0]["Vidas"] <= 0:
                    print("Has pérdido")
                    exit()
                else:
                    vidas = inventarios[0]["Vidas"] - 0.5
                    inventarios[0]["Vidas"] = vidas
                    print(f"Te quedan {vidas} vidas")
                pista = input("Usar pista: \n1.Sí \n2.No \n> ")
                while not pista.isnumeric() or int(pista) not in range(1,3):
                    pista = input("Introduzca opción válida. \nUsar pista: \n1.Sí \n2.No \n> ")
                contador = 0
                if pista == "1":
                    if inventarios[0]["Pistas"] > 0:
                        pistas = inventarios[0]["Pistas"] - 1
                        inventarios[0]["Pistas"] = pistas
                        print(f"T equedan {pistas} pistas en tu inventario")
                        if contador == 0:
                            print(data[0]["objects"][1]["game"]["questions"][0]["clue_1"])
                            contador+=1
                        elif contador == 1:
                            print(data[0]["objects"][1]["game"]["questions"][0]["clue_2"])
                            contador+=1
                        elif contador == 2:
                            print(data[0]["objects"][1]["game"]["questions"][0]["clue_2"])
                            contador+=1
                        else:
                            print("Ya usaste todas las pistas de este juego")
                            True
                    else:
                        print("Ya no tienes pistas en tu inventario")
                        True
        else:
            print(pregunta)
            pregunta = "oidutse ne al ortem aireinegni ed sametsis"
            r_1 = ("s = slice(-36,-43,-1) s_1 = slice(-33,-35,-1) s_2 = slice(-24,-29,-1 s_3 = slice(-13,-23,-1) s_4= slice(-10,-12,-1) s_5 = slice(-30,-32,-1) s_6= slice(-1,-9,-1)")
            cadena = "oidutse ne al ortem aireinegni ed sametsis"
            s = slice(-36,-43,-1) 
            s_1 = slice(-33,-35,-1) 
            s_2 = slice(-24,-29,-1) 
            s_3 = slice(-13,-23,-1) 
            s_4= slice(-10,-12,-1) 
            s_5 = slice(-30,-32,-1) 
            s_6= slice(-1,-9,-1)
            cadena = (f"{cadena[s]} {cadena[s_1]} {cadena[s_5]} {cadena[s_2]} {cadena[s_3]} {cadena[s_4]} {cadena[s_6]}")
            respuesta = input("Introduzca respuesta: ")
            if respuesta == r_1:
                print(cadena)
                print("Correcto")
                break
            else:
                print("Incorrecto")
                if inventarios[0]["Vidas"] <= 0:
                    print("Has pérdido")
                    exit()
                else:
                    vidas = inventarios[0]["Vidas"] - 0.5
                    inventarios[0]["Vidas"] = vidas
                    print(f"Te quedan {vidas} vidas")
                pista = input("Usar pista: \n1.Sí \2.No \n> ")
                while not pista.isnumeric() or int(pista) not in range(1,3):
                    pista = input("Introduzca opción válida. \nUsar pista: \n1.Sí \2.No \n> ")
                contador = 0
                if pista == "1":
                    if inventarios[0]["Pistas"] > 0:
                        pistas = inventarios[0]["Pistas"] - 1
                        inventarios[0]["Pistas"] = pistas
                        print(f"T equedan {pistas} pistas en tu inventario")
                        if contador == 0:
                            print(data[0]["objects"][1]["game"]["questions"][1]["clue_1"])
                            contador+=1
                        else:
                            print("Ya usaste todas las pistas de este juego")
                            True
                    else:
                        print("Ya no tienes pistas en tu inventario")
                        True




        
