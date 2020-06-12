import random
import time


# variables
game_matrix =[]
user_1 = str
turnos = 0




def crate_game():
    print("----------------------------------------")
    print("----- WELCOME TO TIC TAC TOE GAME -----")
    print("---------------------------------------- \n")

    
    for i in range(0,3):
        list_add = list()
        for j in range(0,3):
            list_add.append("")
        game_matrix.append(list_add)

def show_matrix():
    for x in game_matrix:
        print(x, "\n") 


def presentation_win(usuario):
    print("         ****************************************************************************************************")
    time.sleep(0.5)
    print("         ****************************************************************************************************")
    time.sleep(0.5)
    print("         ****************************************************************************************************")
    time.sleep(3)
    print("                              YOU WIN %s "%usuario)
    print("         ****************************************************************************************************")
    print("         ****************************************************************************************************")
    print("         ****************************************************************************************************")











crate_game()
#for x in game_matrix:
#    print(x, "\n")  

user_1 = input("ingrese el primer usuario: ")

while (True):
    show_matrix()
    try:
        
        while(True):
            fila = int(input("ingrese la fila: "))
            columna = int(input("ingrese la columna: "))
            if((fila > 4 or columna > 4) or (fila <= 0 or columna <= 0)):
                print(" fila o columna inexistente ")
            else:
                break

        
        game_matrix[fila-1][columna-1] = "x"
        if(game_matrix[0][0]=="x" and game_matrix[0][1]=="x" and game_matrix[0][2]=="x"):
            print("Ganaste el juego %s" %user_1)
            show_matrix()
            presentation_win(user_1)
            break

        elif(game_matrix[0][0]=="x" and game_matrix[1][1]=="x" and game_matrix[2][2]=="x"):
            print("Ganaste el juego %s" %user_1)
            show_matrix()
            presentation_win(user_1)
            break

        elif(game_matrix[1][0]=="x" and game_matrix[1][1]=="x" and game_matrix[1][2]=="x"):
            print("ganaste el juego 2")
            show_matrix()
            presentation_win(user_1)
            break

        elif(game_matrix[2][0]=="x" and game_matrix[2][1]=="x" and game_matrix[2][2]=="x"):
            print("ganaste el juego 3 ")
            show_matrix()
            presentation_win(user_1)
            break


        elif(game_matrix[0][1]=="x" and game_matrix[1][1]=="x" and game_matrix[1][2]=="x"):
            print("ganaste el juego 4 ")
            show_matrix()
            presentation_win(user_1)
            break

        elif(game_matrix[0][2]=="x" and game_matrix[1][1]=="x" and game_matrix[2][0]=="x"):
            print("ganaste el juego 5 ")
            show_matrix()
            presentation_win(user_1)
            break

        elif(game_matrix[0][2]=="x" and game_matrix[1][2]=="x" and game_matrix[2][2]=="x"):
            print("ganaste el juego 6 ")
            show_matrix()
            presentation_win(user_1)
            break
        else:
            print("aun falta por acabar el juego")        
            
    except:
        print("error al marcar fila o columna")

    


