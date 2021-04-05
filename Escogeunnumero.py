import random
def Numero(inventarios): 
    numeros = []
    for x in range(1,16):
        numeros.append(x)
    def selectRandom(numeros):
        return random.choice(numeros)
    numero = selectRandom(numeros)
    contador = 0
    r = 0
    numeros_malos = []
    while True:
        intento = input("Adivina el número del 1 al 15: ")
        while (not intento.isnumeric()) or (int(intento) not in range(1,16)):
            intento = input("Introduzca opción válida. \nAdivina el número del 1 al 15: ")
        if int(intento) == numero:
            print(f"Correcto el numero es {numero}")
            break
        else:
            print("Incorrecto ese no es el número")
            numeros_malos.append(intento)
            print(numeros_malos)
            r += 1
            if r == 3:
                vidas = inventarios[0]["Vidas"] - 0.25
                inventarios[0]["Vidas"] = vidas
                print(f"Te quedan {vidas} vidas")
            if inventarios[0]["Vidas"] <= 0:
                print("Has perdido")
                exit()
            else:
                pista = input("Usar pista: \n1.Sí \n2.No \n> ")
                while (not pista.isnumeric()) or (int(pista) not in range(1,3)):
                    pista = input("Introduzca opción válida. \nUsar pista: \n1.Sí \n2.No \n> ")
                if pista == "1":
                    if inventarios[0]["Pistas"] <0:
                        print("Ya no tienes pistas en tu inventario")
                        True
                    else:
                        pistas = inventarios[0]["Pistas"] - 1
                        inventarios[0]["Pistas"] = pistas
                        print(f"Te quedan {pistas} pistas en tu inventario")
                        if contador == 0:
                            if int(intento) > int(numero):
                                if (int(intento) - 1) == int(numero):
                                    print("Estás cerca un poco abajo")
                                else:
                                    print("Estás muy arriba")
                            elif int(intento) < int(numero):
                                if (int(intento) + 1) == int(numero):
                                    print("Estás cerca un poco arriba")
                                else: 
                                    print("Estás muy abajo")
                        else:
                            print("Usaste todas las pistas")
                else:
                    True
        
    