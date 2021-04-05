import requests
import json
import random
response = requests.get("https://api-escapamet.vercel.app/")
data = json.loads(response.text)
diccionario = ["pisicina", "metromix", "rectorado"]
inventarios = []

escenario = \
    '''   
~~~~~~~~~|~
        |
0123456 J    
~~~~~~~~~~~   
'''
simbolos = '><(((º>'
# paso 1
def inicializar_juego(diccionario):
    palabra = random.choice(diccionario).lower()
    tablero = ['_'] * len(palabra)
    return tablero, palabra, []
# paso 2
def mostrar_escenario(errores):
    escena = escenario
    for i in range(0, len(simbolos)):
        simbolo = simbolos[i] if i < errores else ' '
        escena = escena.replace(str(i), simbolo)
    print(escena)
# paso 3
def mostrar_tablero(tablero, letras_erroneas):
    for casilla in tablero:
        print(casilla, end=' ')
    print()
    print()
    if len(letras_erroneas) > 0:
        print('Letras erróneas:', *letras_erroneas)
        print()
# paso 4
def pedir_letra(tablero, letras_erroneas):
    valida = False
    while not valida:
        letra = input('Introduce una letra (a-z): ').lower()
        valida = 'a' <= letra <= 'z' and len(letra) == 1 # es una letra
        if not valida:
            print('Error, la letra tiene que estar entre a y z.')
        else:
            valida = letra not in tablero + letras_erroneas
            if not valida:
                print('Letra repetida, prueba con otra.')
    return letra

# paso 5
def procesar_letra(letra, palabra, tablero, letras_erroneas):
    if letra in palabra:
        print('¡Genial! Has acertado una letra.')
        actualizar_tablero(letra, palabra, tablero)
    else:
        print('¡Oh! Has fallado.')
        


# paso 5 (auxiliar)
def actualizar_tablero(letra, palabra, tablero):
    for indice, letra_palabra in enumerate(palabra):
        if letra == letra_palabra:
            tablero[indice] = letra

# paso 6
def comprobar_palabra(tablero):
    return '_' not in tablero

# bucle principal de juego
def jugar_al_ahorcado(inventarios):
    palabra_1 = (data[1]["objects"][0]["game"]["questions"][0]["answer"]).lower()
    palabra_2 = (data[1]["objects"][0]["game"]["questions"][1]["answer"]).lower()
    palabra_3 = (data[1]["objects"][0]["game"]["questions"][2]["answer"]).lower()
    diccionario = [palabra_1, palabra_2, palabra_3]
    palabra = random.choice(diccionario).lower()
    tablero = ['_'] * len(palabra)
    tablero, palabra, letras_erroneas = inicializar_juego(diccionario)
    contador = 0
    while len(letras_erroneas) < len(simbolos):  # pasos 7 y 8
        mostrar_escenario(len(letras_erroneas))  # paso 2
        mostrar_tablero(tablero, letras_erroneas)
        # paso 3
        
        letra = pedir_letra(tablero, letras_erroneas).lower()  # paso 4
        procesar_letra(letra, palabra, tablero, letras_erroneas)
        if letra not in palabra:
            if inventarios[0]["Vidas"] <= 0:
                print("Lo siento has perdido")
                exit()
            else:
                vidas = inventarios[0]["Vidas"] - 0.25
                inventarios[0]["Vidas"] = vidas
                print(f"Te quedan {vidas} vidas")  
        pista = input("Usar pista: \n1.Sí \n2.No \n> ")
        while (not pista.isnumeric()) or (int(pista) not in range(1,3)):
            pista = input("Introduzca opción válida. \nUsar pista: \n1.Sí \n2.No \n> ")
        if pista == "1":
            if inventarios[0]["Pistas"] > 0:
                if palabra == "metromix":
                    if contador == 0:
                        print(data[1]["objects"][0]["game"]["questions"][0]["clue_1"])
                        pistas = inventarios[0]["Pistas"] - 1
                        inventarios[0]["Pistas"] = pistas
                        print(f"Te quedan {pistas} pistas en tu inventario")
                        contador +=1
                    elif contador == 1:
                        print(data[1]["objects"][0]["game"]["questions"][0]["clue_2"])
                        pistas = inventarios[0]["Pistas"] - 1
                        inventarios[0]["Pistas"] = pistas
                        contador +=1
                    elif contador == 2:
                        print(data[1]["objects"][0]["game"]["questions"][0]["clue_3"])
                        pistas = inventarios[0]["Pistas"] - 1
                        inventarios[0]["Pistas"] = pistas
                        print(f"Te quedan {pistas} pistas en tu inventario")
                        contador +=1
                    else:
                        print("Usaste todas las pistas")
                elif palabra == "rectorado":
                    if contador == 0:
                        print(data[1]["objects"][0]["game"]["questions"][2]["clue_1"])
                        pistas = inventarios[0]["Pistas"] - 1
                        inventarios[0]["Pistas"] = pistas
                        print(f"Te quedan {pistas} pistas en tu inventario")
                        contador +=1
                    elif contador == 1:
                        print(data[1]["objects"][0]["game"]["questions"][2]["clue_2"])
                        pistas = inventarios[0]["Pistas"] - 1
                        inventarios[0]["Pistas"] = pistas
                        print(f"Te quedan {pistas} pistas en tu inventario")
                        contador +=1
                    elif contador == 2:
                        print(data[1]["objects"][0]["game"]["questions"][2]["clue_3"])
                        pistas = inventarios[0]["Pistas"] - 1
                        inventarios[0]["Pistas"] = pistas
                        print(f"Te quedan {pistas} pistas en tu inventario")
                        contador +=1
                    else:
                        print("Usaste todas las pistas")
                elif palabra == "piscina":
                    if contador == 0:
                        print(data[1]["objects"][0]["game"]["questions"][1]["clue_1"])
                        pistas = inventarios[0]["Pistas"] - 1
                        inventarios[0]["Pistas"] = pistas
                        print(f"Te quedan {pistas} pistas en tu inventario")
                        contador +=1
                    elif contador == 1:
                        print(data[1]["objects"][0]["game"]["questions"][1]["clue_2"])
                        pistas = inventarios[0]["Pistas"] - 1
                        inventarios[0]["Pistas"] = pistas
                        print(f"Te quedan {pistas} pistas en tu inventario")
                        contador +=1
                    elif contador == 2:
                        print(data[1]["objects"][0]["game"]["questions"][1]["clue_3"])
                        pistas = inventarios[0]["Pistas"] - 1
                        inventarios[0]["Pistas"] = pistas
                        print(f"Te quedan {pistas} pistas en tu inventario")
                        contador +=1
                    else:
                        print("Usaste todas las pistas")
            else:
                print("Ya usaste todas tus pistas del inventario")
        
        


            
        # paso 5
        if comprobar_palabra(tablero):  # paso 6
            print('¡Enhorabuena, lo has logrado!')
            break
    else:
        print(f'¡Lo siento! ¡Has perdido! La palabra a adivinar era {palabra}.')
        mostrar_escenario(len(letras_erroneas))  # paso 7

    mostrar_tablero(tablero, letras_erroneas)
            
            