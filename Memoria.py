import random
'''------------------TABLERO Fichas volteadas------------------------'''

 
 
'''------------------------INICIA EL JUEGO---------------------------'''
def memoria(inventarios):
    board=[]
    '''tablero con fichas volteadas'''
    for x in range(0,4): 
        board.append(["O"] * 4)
    

    '''Función que imprime  el tablero'''
    def print_board(board):
        for row in board:
            print(" ".join(row))
    



    '''---------------Creación tablero con las fichas--------------------'''

    '''elementos tablero con el que se manejará todo'''
    realboard=[]
    fila1=[]
    fila2=[]
    fila3=[]
    fila4=[]
    filas=[fila1,fila2,fila3,fila4]

    '''lista de las fichas(8 simbolos diferentes)'''
    listSymbols=[u'\u2603',u'\u2600', u'\u2602',u'\u262F',u'\u2660',u'\u262d', u'\u263e',u'\u2615',u'\u2603',u'\u2600', u'\u2602',u'\u262F',u'\u2660',u'\u262d', u'\u263e',u'\u2615'] 


    '''Se van llenando las filas con las fichas, dependiendo el rango'''
    for i in range(0,16):
        if(i<4):
            fila1.append(listSymbols[i])
        elif(i<8 and i>3):
            fila2.append(listSymbols[i])
        elif(i<12 and i>7):
            fila3.append(listSymbols[i])
        elif(i>11):
            fila4.append(listSymbols[i])

    '''una vez llenadas las filas se integran al tablero'''		
    for i in filas: 
        realboard.append(i) 
 
    intentosFallidos=0
    print_board(board)
    puntuacion=0
    lista=[0,1,2,3]
    while(True):
        try:
            #Se ingresan las coordenadas de las cartas elegidas
            #el rango va de 0 a 3
            print("Instrucciones"+"\n"+ "Las coordenadas van del 0 al 3"+"\n")
            carta1_row = int(input("Adivina la fila: "))
            carta1_col = int(input("Adivina la columna: "))
            carta2_row = int(input("Adivina la fila: "))
            carta2_col = int(input("Adivina la columna: "))
        
      
        
		
            #Verifica que no escojas la misma carta
            if(carta1_row==carta2_row and carta1_col==carta2_col):
                print("Debes escoger 2 cartas diferentes")
        
            #Verifica el rango del tablero, que sea valido	
            elif(carta1_row not in lista) or (carta1_col not in lista) or (carta2_row not in lista) or (carta2_col not in lista):
                print ("Oops, esta fuera del tablero.")
                    
            #Verifica que escojas cartas que no esten volteadas		
            elif(board[carta1_row][carta1_col]!="O" or board[carta2_row][carta2_col]!="O"):
                print("Esa carta ya esta descubierta")
        
            #Entra en esta condicional cuando son el mismo simbolo
            #se encontró un par
            #las casillas seleccionadas de board se hacen iguales a realboard
            elif (realboard[carta1_row][carta1_col]==realboard[carta2_row][carta2_col]):
                board[carta1_row][carta1_col]=realboard[carta1_row][carta1_col]
                board[carta2_row][carta2_col]=realboard[carta1_row][carta1_col]
                print("Encontraste un par!")
                print()	  
            
            #Las cartas tienen diferente simbolo
            #Aumenta el numero de intentosFallidos
            #se muestran las cartas elegidas, pero luego se vuelven a voltear 
            else:
                print ("No son iguales")
                vidas = inventarios[0]["Vidas"] - 0.25
                inventarios[0]["Vidas"] = vidas
                print(f"Te quedan {vidas} vidas")
                if inventarios[0]["Vidas"] <= 0:
                    print("Has pérdido")
                    exit()
                else:
                    board[carta1_row][carta1_col]=realboard[carta1_row][carta1_col]
                    board[carta2_row][carta2_col]=realboard[carta2_row][carta2_col] 
                    print_board(board)
                    print("Se voltean de nuevo las cartas")
                    board[carta1_row][carta1_col]="O"
                    board[carta2_row][carta2_col]="O" 
                    intentosFallidos+=1
                    contador = 0
                    while True:
                        pistas = input("Usar pista: \n1.Sí \n2.No: \n> ")
                        while not pistas.isnumeric() or int(pistas) not in range(1,3):
                            print("Introduzca opción válida")
                            pistas = input("Usar pista:\n1.Sí \n2.No: \n> ")
                        if pistas == "1":
                            if contador == 0:
                                pistas = inventarios[0]["Pistas"] - 1
                                inventarios[0]["Pistas"] = pistas
                                print(f"Te quedan {pistas} pistas en tu inventario")
                                print("Columna: 0, fila: 0\nColumna:2, fila:0")
                            else:
                                print("Ya usaste todas la pistas de este juego")
                                break
                        

                        
                        

                


                
            #Se rompe el ciclo cuando se tienen 3 intentos fallidos'''
            if(intentosFallidos==10):
                print("Fin del Juego")
                break
                
            #Se rompe el ciclo en caso de hallar todos los pares
            if(board==realboard):
                puntuacion=1
                print("Ganaste el Juego")
                break
                
            print_board(board)
        except:
            print("Introduzca dato válido")
	

	