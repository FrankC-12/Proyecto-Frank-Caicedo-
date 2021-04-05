import random 
def HP(inventarios):
    pregunta_1 = "Nombre de la lechuza de Harry"
    pregunta_2 = "¿Quíen le dió a Harry la snitch dorada en la ultima película?"
    pregunta_3 = "Harry tiene los ojos de su...."
    pregunta_4 = "Nombre las tres reliquias de la muerte"
    preguntas = [pregunta_1, pregunta_2, pregunta_3, pregunta_4,]
    r_1 = "Hedwig"
    r_2 = "Ministro De Magia"
    r_3 = "Madre"
    r_4 = "Piedra De Resurrección, Varita De Saúco​ Y Capa De Invisibilidad"
    pregunta = random.choice(preguntas)
    while True:
        if pregunta == pregunta_1:
            print(pregunta)
            respuesta = input("Respuesta: ").title()
            if respuesta != r_1:
                print("Respuesta incorrecta")
                vidas = inventarios[0]["Vidas"] - 1
                inventarios[0]["Vidas"] <= vidas
                print(f"Te quedan {vidas} vidas")
                if inventarios[0]["Vidas"] == 0:
                    print("Has pérdido")
                    exit()
                else:
                    True
            else:
                print("Correcto")
                break
        elif pregunta == pregunta_2:
            print(pregunta)
            respuesta = input("Respuesta: ").title()
            if respuesta != r_2:
                print("Respuesta incorrecta")
                vidas = inventarios[0]["Vidas"] - 1
                inventarios[0]["Vidas"] <= vidas
                print(f"Te quedan {vidas} vidas")
                if inventarios[0]["Vidas"] == 0:
                    print("Has pérdido")
                    exit()
                else:
                    True
            else:
                print("Correcto")
                break
        elif pregunta == pregunta_3:
            print(pregunta)
            respuesta = input("Respuesta: ").title()
            if respuesta != r_3:
                print("Respuesta incorrecta")
                vidas = inventarios[0]["Vidas"] - 1
                inventarios[0]["Vidas"] = vidas
                print(f"Te quedan {vidas} vidas")
                if inventarios[0]["Vidas"] <= 0:
                    print("Has pérdido")
                    exit()
                else:
                    True
            else:
                print("Correcto")
                break
        else:
            print(pregunta)
            respuesta = input("Respuesta: ").title()
            if respuesta != r_4:
                print("Respuesta incorrecta")
                vidas = inventarios[0]["Vidas"] - 1
                inventarios[0]["Vidas"] = vidas
                print(f"Te quedan {vidas} vidas")
                if inventarios[0]["Vidas"] <= 0:
                    print("Has pérdido")
                    exit()
                else:
                    True
            else:
                print("Correcto")
                break

        
