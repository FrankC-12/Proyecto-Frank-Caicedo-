# AQUÍ ESTAN TODAS LAS LIBRERIAS USADAS PARA EL PROYECTO
from Usuario import Usuario
from Partida import Partida 
from Logica import Logica
from Quiz import Quiz
from Memoria import memoria
from Ahorcado import jugar_al_ahorcado
from Derivadas import derivada
from Criptograma import Criptograma
from Booleana import booleana
from Adivinanzas import adivinanzas
from Escogeunnumero import Numero
from Palabramezclada import Palabra 
from Preguntaspython import python
from HP import HP
from Objeto import Objeto
from Juego import Juego
from Juego_1 import Juego_1
import operator
import requests
import json
import sys
from threading import Timer
import time
# AQUÍ TERMINA LAS LIBRERIAS 
response = requests.get("https://api-escapamet.vercel.app/")
data = json.loads(response.text)
#ESTA FUNCIÓN ES PARA EL REGISTRO DE USUARIO Y VERIFICACION DEL MISMO SI YA HAY UNO CREADO
def registro(usuarios):
    usuario = {}
    usuario["jugadores"] = []
    opcion = input("Indique opcion: \n1.Nuevo usuario \n2.Usuario existente \n> ")
    while (not opcion.isnumeric()) or (int(opcion) not in range(1,3)):
        opcion = input("Introduzca opcion válida: \n1.Nuevo usuario \n2.Usuario existente \n> ")
    if opcion == "1": 
        with open("usuarios.json" ) as file:
            dat = json.load(file)
            for x in dat:
                for y in x:
                    while True:
                        nombre = input("Indique nombre: ").title()
                        while nombre.isnumeric():
                            nombre = input("El nombre no puedo tener números: ")
                        if nombre == y["Nombre"]:
                            print(f"El nombre de usuario {nombre} ya existe. Por favor elija otro nombre")
                            True
                        else:
                            break
                

                 
        print("Nombre de usuario válido")
        contraseña = input("Indique contraseña: ")
        edad = input("Indique edad: ")
        while (not edad.isnumeric()) or (int(edad) < 0):
            edad = input("Indique una edad válida: ")
        print("1.Scharifker, 2.Eugenio Mendoza, 3.Pelusa, 4.Gandhi, 5.John Wick, 6.Jon Snow, 7.Daenerys Targaryen")
        avatar = input("Elija el número de avatar: ")
        while (not avatar.isnumeric()) or (int(avatar) not in range(1,8)):
            avatar = input("Elija un avatar válido: ")
        if avatar == "1":
            avatar = "Scharifker"
        elif avatar == "2":
            avatar = "Eugenio Mendoza"
        elif avatar == "3":
            avatar = "Pelusa"
        elif avatar == "4":
            avatar = "Gandhi"
        elif avatar == "5":
            avatar = "John Wick"
        elif avatar == "6":
            avatar = "Jonh Snow"
        else:
            avatar = "Daenerys Targeryen"
        
        u = Usuario(nombre,contraseña,edad,avatar)
        ju = {}
        ju["Nombre"] = nombre
        ju["Contraseña"] = contraseña
        ju["Edad"] = edad
        ju["Completo el juego"] = 0
        ju["Avatar"] = avatar
        ju["Tiempo"] = 0
        
        
        usuarios.append(ju)
        
        u.mostrar()
        usuario["jugadores"].append(ju)
        with open("usuarios.json", "a") as file:
            json.dump(usuario,file,indent=4)

                              
            
            

    else:
        with open("usuarios.json" ) as file:
            dat = json.load(file)
            for x in dat["jugadores"]:
                while True:
                    usuario = input("Introduzca nombre de usuario: ").title()
                    if usuario != x["Nombre"]:
                        print(f"El usuario {usuario} no existe en la base de datos")
                        True
                    else:
                        print(f"Bienvenido de nuevo {usuario}")
                        print("Por favor introduce tu contraseña")
                        contraseña = input("Contraseña: ")
                        while contraseña != x["Contraseña"]:
                            print("Contraseña incorrecta")
                            contraseña = input("Contraseña: ")
                        print("Contraseña correcta")
                        break
                
#HASTA AQUÍ LLEGA LA FUNCIÓN DEL USUARIO               
                
    
        
            
            
                
        
#ESTA FUNCION ES PARA LA PARTIDA DEL USUARIO EN CUANTO TIEMPO, VIDAS, PISTAS Y DIFICULTAD
def partida(usuarios):
    
    juego = input("\n1.Facil \n2.Medio \n3.Difícil \n> ")
    while (not juego.isnumeric()) or (int(juego) not in range(1,4)):
        juego = input("Seleccione una dificultad válida: \n1.Fácil \n2.Medio \n3.Difícil \n> ")
    if juego == "1":
        dificultad = "Fácil"
        vidas = 5
        pistas = 5
        tiempo = 15
    elif juego == "2":
        dificultad = "Medio"
        vidas = 3
        pistas = 3
        tiempo = 10
    else:
        dificultad = "Difícil"
        vidas = 1
        pistas = 2
        tiempo = 8
    inventario = {}
    inventario["Vidas"] = vidas
    inventario["Pistas"] = pistas
    inventario["Tiempo"] = tiempo
    
    inventario["Award"] = []
    inventarios.append(inventario)
    juego = Partida(dificultad,vidas,pistas,tiempo)
    juego.mostrar()
    aceptas = input("1.Sí \n2.No \n> ")
    while (not aceptas.isnumeric()) or int(aceptas) not in range(1,3):
        aceptas = input("Introduzca opción válida: \n1.Sí \n2.No \n> ")
    
    if aceptas == "1":
        print(f"Bienvenido gracias por tu disposición a ayudarnos a resolver este inconveniente, te encuentras actualmente ubicado en la biblioteca, revisa el menú de opciones para ver qué acciones puedes realizar. Recuerda que el tiempo corre más rápido que un trimestre en este reto.")
    else:
        print("Si tienes miedo pide tiempo")
        exit()
#HASTA AQUI LA FUNCIÓN DE PARTIDA

#ESTA FUNCIÓN CONTIENE EL JUEGO CON SUS RESPECTIVO CUARTOS, OBJETOS Y JUEGOS EN CADA CUARTO
inventarios = []
def juegos(inventarios,usuarios):
    print(inventarios[0]["Tiempo"])
    time_1 = 60*inventarios[0]["Tiempo"]
    inicio = time.time()
    def timeout():
        print("Se termino el tiempo")
        sys.exit() 
    t = Timer(time_1, timeout)
    t.start()
    print(f"Ok estás ubicado en estos momentos en la Universidad Metropolitana ")
    while True:
        cuarto = input("A donde quieres ir:\n1.Plaza rectorado \n2.Biblioteca \n3.Pasillo de laboratorios \n4.Laboratorios SL001\n5.Cuarto de servidores \n> ")
        while (not cuarto.isnumeric()) or (int(cuarto) not in range(1,6)):
            cuarto = input("opcion invalida:\n1.Plaza Rectorado \n2.Biblioteca \n3.Pasillo de laboratorios \n4.Laboratorios SL001\n5.Cuarto de servidores \n> ")
        if cuarto == "1":
            print(f"Ok estás ubicado en la plaza del rectorado, puedes explorar un poco a ver que encuentras")
            while True:
                salir = input("1.Ir a otro lugar \n2.Seguir en el cuarto \n> ")
                if salir == "1":
                    break
                else:
                    direccion = input("1.Centro \n2.Izquierda \n3.Derecha \n> ")
                    while (not direccion.isnumeric()) or (int(direccion) not in range(1,4)):
                        direccion = input("Introduzca opcion válida: \n1.Centro \n2.Izquierda \n3.Derecha")
                    if direccion == "1":
                        if (data[2]["objects"][0]["game"]["award"]) in inventarios[0]["Award"]:
                            print("Ya interactuaste con todos los objetos en esta posición")
                            True
                        else:
                            if (data[4]["objects"][2]["game"]["award"]) in inventarios[0]["Award"] and (data[1]["objects"][2]["game"]["award"]) in inventarios[0]["Award"]:
                                name = (data[2]["objects"][0]["name"])
                                saman = Objeto(name)
                                saman.mostrar()
                                print("Al parecer hay un juego, si lográs ganar habra un premio, si pierdes eres muy malo XD")
                                name = (data[2]["objects"][0]["game"]["name"])
                                award = (data[2]["objects"][0]["game"]["award"])
                                rules = (data[2]["objects"][0]["game"]["rules"])
                                requirement = (data[2]["objects"][0]["game"]["requirement"])
                                message_requeriment = (data[2]["objects"][0]["game"]["requirement"])
                                empezar = input("Empezar Juego: \n1.Sí \n2.No \n> ")
                                if empezar == "1":
                                    logica = Juego_1(name, requirement, award, rules,message_requirement)
                                    logica.mostrar()
                                    Logica(inventarios)
                                    print("Tu inventario se ha actualizado")
                                    inventarios[0]["Award"].append(award)
                                    print(inventarios)
                                    salir = input("Ir a otro lugar del mapa: \n1.Sí\n2.No: \n> ")
                                    while not salir.isnumeric() or int(salir) not in range(1,3):
                                        print("Introduzca opción válida")
                                        salir = input("Ir a otro lugar del mapa: 1.Sí\n2.No: \n> ")
                                    if salir == "1":
                                        break
                                    else:
                                        True
                                else:
                                    True
                            else:
                                name = (data[2]["objects"][0]["game"]["name"])
                                award = (data[2]["objects"][0]["game"]["award"])
                                rules = (data[2]["objects"][0]["game"]["rules"])
                                requirement = (data[2]["objects"][0]["game"]["requirement"])
                                message_requirement = (data[2]["objects"][0]["game"]["message_requirement"])
                                logica = Juego_1(name, award, rules, requirement, message_requirement)
                                logica.mostrar()
                                print("Además por no tener eso pisaste el Samán y pierdes una vida")
                                vidas = inventarios[0]["Vidas"] - 1
                                inventarios[0]["Vidas"] = vidas
                                print(f"Te quedan {vidas} vidas")
                                True
                    elif direccion == "2":
                        if (data[2]["objects"][1]["game"]["award"]) in inventarios[0]["Award"]:
                            print("Ya has interactuaste con todos los objetos en esta posición")
                            True
                        else:
                            name = (data[2]["objects"][1]["name"])
                            banco_1 = Objeto(name)
                            banco_1.mostrar()
                            print("Al paracer este objeto te conduce a otro juego")
                            name = (data[2]["objects"][1]["game"]["name"])
                            award = (data[2]["objects"][1]["game"]["award"])
                            rules = (data[2]["objects"][1]["game"]["rules"])
                            requirement = (data[2]["objects"][1]["game"]["requirement"])
                            empezar = input("Empezar Juego: \n1.Sí \n2.No \n> ")
                            if empezar == "1":
                                quiz = Juego(name,requirement,award,rules)
                                quiz.mostrar()
                                Quiz(inventarios)
                                inventarios[0]["Award"].append(award)
                                print("Tu inventario se ha actualizado")
                                print(inventarios)
                                salir = input("Ir a otro lugar del mapa: \n1.Sí\n2.No: \n> ")
                                while not salir.isnumeric() or int(salir) not in range(1,3):
                                    print("Introduzca opción válida")
                                    salir = input("Ir a otro lugar del mapa: \n1.Sí\n2.No: \n> ")
                                if salir == "1":
                                    break
                                else:
                                    True
                            else:
                                True
                    else:
                        if (data[2]["objects"][2]["game"]["award"]) in inventarios[0]["Award"]:
                            print("Ya has interactuaste con todos los objetos en esta posición")
                            True
                        else:
                            name = (data[2]["objects"][2]["name"])
                            banco_2 = Objeto(name)
                            banco_2.mostrar()
                            print("Al paracer este objeto te conduce a otro juego")
                            name = (data[2]["objects"][2]["game"]["name"])
                            award = (data[2]["objects"][2]["game"]["award"])
                            rules = (data[2]["objects"][2]["game"]["rules"])
                            requirement = (data[2]["objects"][2]["game"]["requirement"])
                            
                            empezar = input("Empezar Juego: \n1.Sí \n2.No \n> ")
                            if empezar == "1":
                                memorias = Juego(name,requirement,award,rules)
                                memorias.mostrar()
                                memoria(inventarios)
                                inventarios[0]["Award"].append(award)
                                print("Tu inventario se ha actualizado")
                                print(inventarios)
                                salir = input("Ir a otro lugar del mapa: \n1.Sí\n2.No: \n> ")
                                while not salir.isnumeric() or int(salir) not in range(1,3):
                                    print("Introduzca opción válida")
                                    salir = input("Ir a otro lugar del mapa: \n1.Sí\n2.No: \n> ")
                                if salir == "1":
                                    break
                                else:
                                    True
                            else:
                                True
        elif cuarto == "2":
            
            print(f"Bienvenido a la biblioteca de la Universidad Metropolitana, puedes explorarla y ver que consigues")
            while True:
                salir = input("1.Ir a otro lugar \n2.Seguir en el cuarto \n> ")
                if salir == "1":
                    break
                else:
                    direccion = input("1.Centro \n2.Izquierda \n3.Derecha \n> ")
                    while (not direccion.isnumeric()) or (int(direccion) not in range(1,4)):
                        direccion = input("Introduzca opcion válida: \n1.Centro \n2.Izquierda \n3.Derecha")
                    if direccion == "1":
                        if (data[1]["objects"][0]["game"]["award"]) in inventarios[0]["Award"]:
                            print("Ya interactuaste con todos los objetos en esta posición")
                        else:
                            name = (data[1]["objects"][0]["name"])
                            mueble = Objeto(name)
                            mueble.mostrar()
                            print("Al parecer hay un juego, si lográs ganar habra un premio, si pierdes eres muy malo XD")
                            name = (data[1]["objects"][0]["game"]["name"])
                            award = (data[1]["objects"][0]["game"]["award"])
                            rules = (data[1]["objects"][0]["game"]["rules"])
                            requirement = (data[1]["objects"][0]["game"]["requirement"])
                            
                            empezar = input("Empezar Juego: \n1.Sí \n2.No \n> ")
                            if empezar == "1":
                                Ahorcado = Juego(name, requirement, award, rules)
                                Ahorcado.mostrar()
                                jugar_al_ahorcado(inventarios)
                                inventarios[0]["Award"].append(award)
                                print("Tu inventario se ha actualizado")
                                print(inventarios)
                                salir = input("Ir a otro lugar del mapa: \n1.Sí\n2.No: \n> ")
                                while not salir.isnumeric() or int(salir) not in range(1,3):
                                    print("Introduzca opción válida")
                                    salir = input("Ir a otro lugar del mapa: \n1.Sí\n2.No: \n> ")
                                if salir == "1":
                                    break
                                else:
                                    True
                            else:
                                True
                    elif direccion == "2":
                        if (data[1]["objects"][1]["game"]["award"]) in inventarios[0]["Award"]:
                            print("Ya interactuaste con todos los objetos en esta posición")
                            True
                        else:
                            if (data[2]["objects"][1]["game"]["award"]) in inventarios[0]["Award"]:
                                name = (data[1]["objects"][1]["name"])
                                mueble_1 = Objeto(name)
                                mueble_1.mostrar()
                                print("Al parecer hay un juego, si lográs ganar habra un premio, si pierdes eres muy malo XD")
                                name = (data[1]["objects"][1]["game"]["name"])
                                award = (data[1]["objects"][1]["game"]["award"])
                                rules = (data[1]["objects"][1]["game"]["rules"])
                                requirement = (data[1]["objects"][1]["game"]["requirement"])
                                message_requirement = (data[1]["objects"][1]["game"]["message_requirement"])
                                empezar = input("Empezar Juego: \n1.Sí \n2.No \n> ")
                                if empezar == "1":
                                    derivadas = Juego_1(name, requirement, award, rules,message_requirement)
                                    derivadas.mostrar()
                                    derivada(inventarios)
                                    vidas = inventarios[0]["Vidas"] + 1 
                                    inventarios[0]["Vidas"] = vidas
                                    print("Has ganado una vida extra")
                                    print(f"Ahora tienes {vidas} vidas")
                                    print(inventarios)
                                    salir = input("Ir a otro lugar del mapa: \n1.Sí\n2.No: \n> ")
                                    while not salir.isnumeric() or int(salir) not in range(1,3):
                                        print("Introduzca opción válida")
                                        salir = input("Ir a otro lugar del mapa: \n1.Sí\n2.No: \n> ")
                                    if salir == "1":
                                        break
                                    else:
                                        True
                                else:
                                    True
                            else:
                                name = (data[1]["objects"][1]["game"]["name"])
                                award = (data[1]["objects"][1]["game"]["award"])
                                rules = (data[1]["objects"][1]["game"]["rules"])
                                requirement = (data[1]["objects"][1]["game"]["requirement"])
                                message_requirement = (data[1]["objects"][1]["game"]["message_requirement"])
                                derivadas = Juego_1(name, requirement, award, rules,message_requirement)
                                derivadas.mostrar()
                                True
                    else:
                        if (data[1]["objects"][2]["game"]["award"]) in inventarios[0]["Award"]:
                            print("Ya interactuaste con todos los objetos en esta posición")
                            True
                        else:
                            if (data[0]["objects"][2]["game"]["award"]) in inventarios[0]["Award"]:
                                name = (data[1]["objects"][2]["name"])
                                mueble_2 = Objeto(name)
                                mueble_2.mostrar()
                                print("Al parecer hay un juego, si lográs ganar habra un premio, si pierdes eres muy malo XD")
                                name = (data[1]["objects"][2]["game"]["name"])
                                award = (data[1]["objects"][2]["game"]["award"])
                                rules = (data[1]["objects"][2]["game"]["rules"])
                                requirement = (data[1]["objects"][2]["game"]["requirement"])
                                message_requirement = (data[1]["objects"][2]["game"]["message_requirement"])
                                empezar = input("Empezar Juego: \n1.Sí \n2.No \n> ")
                                if empezar == "1":
                                    criptograma = Juego_1(name, requirement, award, rules,message_requirement)
                                    criptograma.mostrar()
                                    Criptograma(inventarios)
                                    inventarios[0]["Award"].append(award)
                                    print("Tu inventario se ha actualizado")
                                    print(inventarios)
                                    salir = input("Ir a otro lugar del mapa: \n1.Sí\n2.No: \n> ")
                                    while not salir.isnumeric() or int(salir) not in range(1,3):
                                        print("Introduzca opción válida")
                                        salir = input("Ir a otro lugar del mapa: \n1.Sí\n2.No: \n> ")
                                    if salir == "1":
                                        break
                                    else:
                                        True
                                else:
                                    True
                            else:
                                name = (data[1]["objects"][2]["game"]["name"])
                                award = (data[1]["objects"][2]["game"]["award"])
                                rules = (data[1]["objects"][2]["game"]["rules"])
                                requirement = (data[1]["objects"][2]["game"]["requirement"])
                                message_requirement = (data[1]["objects"][2]["game"]["message_requirement"])
                                criptograma = Juego_1(name, requirement, award, rules,message_requirement)
                                criptograma.mostrar()
                                True

        elif cuarto == "3":
            
            print("Estás ubicado en el pasillo de laboratorios, puedes explorarla y ver que consigues")
            while True:
                salir = input("1.Ir a otro lugar \n2.Seguir en el cuarto \n> ")
                if salir == "1":
                    break
                else:
                    direccion = input("1.Centro\n> ")
                    while (not direccion.isnumeric()) or (int(direccion) not in range(1,2)):
                        direccion = input("Introduzca opcion válida: \n1.Centro\n> ")
                    if (data[2]["objects"][2]["game"]["award"]) in inventarios[0]["Award"]:
                        if direccion == "1":
                            if (data[3]["objects"][0]["game"]["award"]) in inventarios[0]["Award"]:
                                print("Ya interactuaste con todos los objetos en esta posición")
                            else:
                                if (data[2]["objects"][2]["game"]["award"]) in inventarios[0]["Award"]:
                                    martillo = (input("Rompe el candado con el martillo para abrir la puerta: \n1.Romper \n> "))
                                    while not martillo.isnumeric() or int(martillo) not in range(1,2):
                                        print(f"{avatar} ¿Qué esperas ROMPE el candado?")
                                        martillo = (input("Rompe el candado con el martillo para abrir la puerta: \n1.Romper \n> "))
                                    name = (data[3]["objects"][0]["name"])
                                    puerta = Objeto(name) 
                                    puerta.mostrar()
                                    print("Al parecer hay un juego, si lográs ganar habra un premio, si pierdes eres muy malo XD")
                                    name = (data[3]["objects"][0]["game"]["name"])
                                    award = (data[3]["objects"][0]["game"]["award"])
                                    rules = (data[3]["objects"][0]["game"]["rules"])
                                    requirement = (data[3]["objects"][0]["game"]["requirement"])
                                    message_requirement = (data[3]["objects"][0]["game"]["message_requirement"])
                                    empezar = input("Empezar Juego: \n1.Sí \n2.No \n> ")
                                    if empezar == "1":
                                        logica_booleana = Juego_1(name, requirement, award, rules,message_requirement)
                                        logica_booleana.mostrar()
                                        booleana(inventarios)
                                        inventarios[0]["Award"].append(award)
                                        print("Tu inventario se ha actualizado")
                                        print(inventarios)
                                        salir = input("Ir a otro lugar del mapa: \n1.Sí\n2.No: \n> ")
                                        while not salir.isnumeric() or int(salir) not in range(1,3):
                                            print("Introduzca opción válida")
                                            salir = input("Ir a otro lugar del mapa: \n1.Sí\n2.No: \n> ")
                                        if salir == "1":
                                            break
                                        else:
                                            True
                                    else:
                                        True
                                else:
                                    name = (data[3]["objects"][0]["game"]["name"])
                                    award = (data[3]["objects"][0]["game"]["award"])
                                    rules = (data[3]["objects"][0]["game"]["rules"])
                                    requirement = (data[3]["objects"][0]["game"]["requirement"])
                                    message_requirement = (data[3]["objects"][0]["game"]["message_requirement"])
                                    logica_booleana = Juego_1(name, requirement, award, rules,message_requirement)
                                    logica_booleana.mostrar()
                                    True
        elif cuarto == "4":
            
            print(f"Estás en laboratorio SL001, puedes explorarla y ver que consigues")
            while True:
                salir = input("1.Ir a otro lugar \n2.Seguir en el cuarto \n> ")
                if salir == "1":
                    break
                else:
                    direccion = input("1.Centro \n2.Izquierda \n3.Derecha\n> ")
                    while (not direccion.isnumeric()) or (int(direccion) not in range(1,4)):
                        direccion = input("Introduzca opcion válida: \n1.Centro \n2.Izquierda \n3.Derecha\n> ")
                    if direccion == "1":
                        if (data[0]["objects"][0]["game"]["award"]) in inventarios[0]["Award"]:
                            print("Ya interactuaste con todos los objetos en esta posición")
                            True
                        else:
                            name = (data[0]["objects"][0]["name"])
                            pizarra = Objeto(name)
                            pizarra.mostrar()
                            print("Al parecer hay un juego, si lográs ganar habra un premio, si pierdes eres muy malo XD")
                            name = (data[0]["objects"][0]["game"]["name"])
                            award = (data[0]["objects"][0]["game"]["award"])
                            rules = (data[0]["objects"][0]["game"]["rules"])
                            requirement = (data[0]["objects"][0]["game"]["requirement"])
                            empezar = input("Empezar Juego: \n1.Sí \n2.No \n> ")
                            if empezar == "1":
                                pass
                                salir = input("Ir a otro lugar del mapa: \n1.Sí\n2.No: \n> ")
                                if salir == "1":
                                    break
                                else:
                                    True
                            else:
                                True
                    elif direccion == "2":
                        if (data[0]["objects"][1]["game"]["award"]) in inventarios[0]["Award"]:
                            print("Ya interactuaste con todos los objetos en esta posición")
                            True
                        else:
                            if "cable HDMI" in inventarios[0]["Award"]:
                                name = (data[0]["objects"][0]["name"])
                                compu_1 = Objeto(name)
                                compu_1.mostrar()
                                print("Al parecer hay un juego, si lográs ganar habra un premio, si pierdes eres muy malo XD")
                                name = (data[0]["objects"][1]["game"]["name"])
                                award = (data[0]["objects"][1]["game"]["award"])
                                rules = (data[0]["objects"][1]["game"]["rules"])
                                requirement = (data[0]["objects"][1]["game"]["requirement"])
                                message_requirement = (data[0]["objects"][1]["game"]["message_requirement"])
                                empezar = input("Empezar Juego: \n1.Sí \n2.No \n> ")
                                if empezar == "1":
                                    Python = Juego_1(name, requirement, award, rules,message_requirement)
                                    Python.mostrar()
                                    python(inventarios)
                                    inventarios[0]["Award"].append(award)
                                    print("Tu inventario se ha actualizado")
                                    print(inventarios)
                                    salir = input("Ir a otro lugar del mapa: \n1.Sí\n2.No: \n> ")
                                    while not salir.isnumeric() or int(salir) not in range(1,3):
                                        print("Introduzca opción válida")
                                        salir = input("Ir a otro lugar del mapa: \n1.Sí\n2.No: \n> ")
                                    if salir == "1":
                                        break
                                    else:
                                        True
                                else:
                                    True
                            else:
                                name = (data[0]["objects"][1]["game"]["name"])
                                award = (data[0]["objects"][1]["game"]["award"])
                                rules = (data[0]["objects"][1]["game"]["rules"])
                                requirement = (data[0]["objects"][1]["game"]["requirement"])
                                message_requirement = (data[0]["objects"][1]["game"]["message_requirement"])
                                Python = Juego_1(name, requirement, award, rules,message_requirement)
                                Python.mostrar()
                                True
                    else:
                        if  (data[0]["objects"][2]["game"]["award"]) in inventarios[0]["Award"]:
                            print("Ya interactuaste con todos los objetos en esta posición")
                            True
                        else:
                            if "9531234" in inventarios[0]["Award"]:
                                introduzca = input("Introduzca contraseña: ")
                                while not introduzca.isnumeric():
                                    print("Introduzca datos válidos")
                                if introduzca == "9531234": 
                                    name = (data[0]["objects"][2]["name"])
                                    pizarra = Objeto(name)
                                    pizarra.mostrar()
                                    print("Al parecer hay un juego, si lográs ganar habra un premio, si pierdes eres muy malo XD")
                                    name = (data[0]["objects"][2]["game"]["name"])
                                    award = (data[0]["objects"][2]["game"]["award"])
                                    rules = (data[0]["objects"][2]["game"]["rules"])
                                    requirement = (data[0]["objects"][2]["game"]["requirement"])
                                    message_requirement = (data[0]["objects"][2]["game"]["message_requirement"])
                                    empezar = input("Empezar Juego: \n1.Sí \n2.No \n> ")
                                    if empezar == "1":
                                        adivinanza = Juego_1(name, requirement, award, rules, message_requirement)
                                        adivinanza.mostrar()
                                        adivinanzas(inventarios)
                                        inventarios[0]["Award"].append(award)
                                        print("Tu inventario se ha actualizado")
                                        print(inventarios)
                                        salir = input("Ir a otro lugar del mapa: \n1.Sí\n2.No: \n> ")
                                        while not salir.isnumeric() or int(salir) not in range(1,3):
                                            print("Introduzca opción válida")
                                            salir = input("Ir a otro lugar del mapa: \n1.Sí\n2.No: \n> ")
                                        if salir == "1":
                                            break
                                        else:
                                            True
                                    else:
                                        True
                                else:
                                    print("Incorrecto intente de nuevo")
                                    True
                            else:
                                name = (data[0]["objects"][2]["game"]["name"])
                                award = (data[0]["objects"][2]["game"]["award"])
                                rules = (data[0]["objects"][2]["game"]["rules"])
                                requirement = (data[0]["objects"][2]["game"]["requirement"])
                                message_requirement = (data[0]["objects"][2]["game"]["message_requirement"])
                                adivinanza = Juego_1(name, requirement, award, rules, message_requirement)
                                adivinanza.mostrar()
                                True
        else:
            print(f"Estás en cuarto de servidores, puedes explorar y ver que consigues")
            while True:
                salir = input("1.Ir a otro lugar \n2.Seguir en el cuarto \n> ")
                if salir == "1":
                    break
                else:
                    direccion = input("1.Centro \n2.Izquierda \n3.Derecha\n> ")
                    while (not direccion.isnumeric()) or (int(direccion) not in range(1,4)):
                        direccion = input("Introduzca opcion válida: \n1.Centro \n2.Izquierda \n3.Derecha\n> ")
                    if direccion == "1":
                        if (data[0]["objects"][1]["game"]["award"]) in inventarios[0]["Award"] and (data[2]["objects"][0]["game"]["award"]) in inventarios[0]["Award"] :
                            name = (data[4]["objects"][0]["name"])
                            puerta = Objeto(name)
                            puerta.mostrar()
                            print("Al parecer hay un juego, si lográs ganar habra un premio, si pierdes eres muy malo XD")
                            name = (data[4]["objects"][0]["game"]["name"])
                            award = (data[4]["objects"][0]["game"]["award"])
                            rules = (data[4]["objects"][0]["game"]["rules"])
                            requirement = (data[4]["objects"][0]["game"]["requirement"])
                            
                            empezar = input("Empezar Juego: \n1.Sí \n2.No \n> ")
                            if empezar == "1":
                                hp = Juego(name, requirement, award, rules)
                                hp.mostrar()
                                HP(inventarios)   
                                s = True
                                fin = time.time()
                                tiempo_total = fin-inicio
                                t= time_1 - tiempo_total
                                inventarios[0]["Award"].append(award)
                                print("Tu inventario se ha actualizado")
                                print(inventarios)
                                print("FELICIDADES HAS GANADO EL JUEGO")
                                with open("usuarios.json") as file:
                                    dat = json.load(file)
                                    dat["jugadores"][0]["Tiempo"] = t
                                    dat["jugadores"][0]["Completo el juego"] = s
                                exit()
                                salir = input("Ir a otro lugar del mapa: \n1.Sí\n2.No: \n> ")
                                while not salir.isnumeric() or int(salir) not in range(1,3):
                                    print("Introduzca opción válida")
                                    salir = input("Ir a otro lugar del mapa: \n1.Sí\n2.No: \n> ")
                                if salir == "1":
                                    break
                                else:
                                    True
                            else:
                                True
                        else:
                            print("Necesitas un carnet y un disco duro para usar este objeto")
                            True
                    elif direccion == "2":
                        if "9531234" in inventarios[0]["Award"]:
                            print("Ya interactuaste con todos los objetos en esta posición")
                            True
                        else:
                            name = (data[4]["objects"][1]["name"])
                            rack = Objeto(name)
                            rack.mostrar()
                            print("Al parecer hay un juego, si lográs ganar habra un premio, si pierdes eres muy malo XD")
                            name = (data[4]["objects"][1]["game"]["name"])
                            award = "9531234"
                            rules = (data[4]["objects"][1]["game"]["rules"])
                            requirement = (data[4]["objects"][1]["game"]["requirement"])
                            empezar = input("Empezar Juego: \n1.Sí \n2.No \n> ")
                            if empezar == "1":
                                palabra = Juego(name, requirement, award, rules)
                                palabra.mostrar()
                                Palabra(inventarios)
                                inventarios[0]["Award"].append(award)
                                print("Tu inventario se ha actualizado")
                                print(inventarios)
                                salir = input("Ir a otro lugar del mapa: \n1.Sí\n2.No: \n> ")
                                while not salir.isnumeric() or int(salir) not in range(1,3):
                                    print("Introduzca opción válida")
                                    salir = input("Ir a otro lugar del mapa: \n1.Sí\n2.No: \n> ")
                                if salir == "1":
                                    break
                                else:
                                    True
                            else:
                                True
                    else:
                        if (data[4]["objects"][2]["game"]["award"]) in inventarios[0]["Award"]:
                            print("Ya interactuaste con todos los objetos en esta posición")
                            True
                        else:
                            name = (data[4]["objects"][2]["name"])
                            papelera = Objeto(name)
                            papelera.mostrar()
                            print("Al parecer hay un juego, si lográs ganar habra un premio, si pierdes eres muy malo XD")
                            name = (data[4]["objects"][2]["game"]["name"])
                            award = (data[4]["objects"][2]["game"]["award"])
                            rules = (data[4]["objects"][2]["game"]["rules"])
                            requirement = (data[4]["objects"][2]["game"]["requirement"])
                            empezar = input("Empezar Juego: \n1.Sí \n2.No \n> ")
                            if empezar == "1":
                                numero = Juego(name, requirement, award, rules)
                                numero.mostrar()
                                Numero(inventarios)
                                inventarios[0]["Award"].append(award)
                                print("Tu inventario se ha actualizado")
                                print(inventarios)
                                salir = input("Ir a otro lugar del mapa: \n1.Sí\n2.No: \n> ")
                                while not salir.isnumeric() or int(salir) not in range(1,3):
                                    print("Introduzca opción válida")
                                    salir = input("Ir a otro lugar del mapa: \n1.Sí\n2.No: \n> ")
                                if salir == "1":
                                    break
                                else:
                                    True
#ESTA FUNCIÓN MUESTRA LOS USUARIOS REGISTRADOS EN EL PROGRAMA        
def ver_usuarios():
    with open("usuarios.json") as file:
            data = json.load(file)
            for x in data:
                nombre = x["Nombre"]
                avatar =  x["Avatar"]
                print(f"\nNombre: {nombre} - Avatar: {avatar}")
#HASTA AQUÍ LLEGA
 


usuarios = []                      
def main():
    while True:
        print("Bienvenido a Escapamet")
        print()
        opcion = input("1.Nueva partida \n2.Ver usuarios \n3.Salir  \n> ")
        while (not opcion.isnumeric()) or (int(opcion) not in range(1,4)):
            opcion = input("Introduzca opción valida: ")
        if opcion == "1":
            registro(usuarios)
            inicio = input("Empezar partida: \n1.Sí \n2.No \n> ")
            if inicio == "1":
                partida(usuarios)
                juegos(inventarios,usuarios)
            else:
                True
        elif opcion == "2":
            ver_usuarios()
        else:
            print("Gracias hasta pronto")
            exit()
main()