"""
Escriba un progrrama que reciba una matriz cuadrada de NxN,
intercambie las filas desde arriba hacia abajo de tal manera
que el elemento de mayor magnitud de cada columna se ubique
en la diagonal y sustituya con ceros el resto de la fila hacia la derecha

"""
import random  # con esta libreria podremos definir números al momento de querer números al azar
# de aqui sacaremos los números para crar arreglos al azar
random_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]








# la dimension nxn de la matriz
numero_matriz = int(input("Indique la dimension quiere que sea la matriz: "))
matriz_1 = []  # declaramos la matriz principal

for i in range(1, numero_matriz+1):
    # mediante esta instancia crearemos una lista vacia por cada vez que el bucle for
    list_add_ = list()
    # haga un recorrido para así poder agregar un nuevo elemento
    counter_ = 0  # Con este contador nos aseguramos de que se creen de manera correcta las dimensiones de la matriz
    while(counter_ < numero_matriz):

        # este metodo de la libreria random es para elegir de la lsta random
        numeros_azar = random_list[random.randint(0, 8)]
        # elementos al azar del 0 al 9 para elegir uno y despues mediante la opcion append agreggar a la lista list_add_
        # y así poder crear un nuevo arreglo cada vez que el bucle haga su recorrido

        list_add_.append(numeros_azar)  # aqui solo agregamos como ya mecioné arriba
        counter_ = counter_+1  # solo hacemos que el contador empiece

    # aaqui agrega a la lista de listas para que cree una lista de listas o sea una matriz
    matriz_1.append(list_add_)
print("matiz original \n")
for x in range(0,numero_matriz):
    print(matriz_1[x],"\n")





#print("|",matriz_1[0][0]," , ",matriz_1[0][1]," , ",matriz_1[0][2],"|")
#print("|",matriz_1[1][0]," , ",matriz_1[1][1]," , ",matriz_1[1][2],"|")
#print("|",matriz_1[2][0]," , ",matriz_1[2][1]," , ",matriz_1[2][2],"|")
for j in range(0, numero_matriz):
    
    counter_2 = 0
    #print("asi queda la matriz fila", j+1,":", matriz_1[j])
    
    lista_agregar_columnas = [] # mediante esta variable de tipo lista
    # solo agregaremos valores para determinar cual es el elemento mayor de cada columna, más abajo los definiremos

    while(counter_2 < numero_matriz):
        
        lista_agregar_columnas.append(matriz_1[counter_2][j])
        
        counter_2 = counter_2 +1
    

    lista_ordenada = sorted(lista_agregar_columnas)
    elemento_mayor = lista_ordenada[numero_matriz-1]
    indice_para_mover_matriz = lista_agregar_columnas.index(elemento_mayor)
    #print("elemento_mayor",elemento_mayor)
    #print("asi queda la matriz::::: ",j, matriz_1)
    matriz_1.insert(j,matriz_1.pop(indice_para_mover_matriz))
    print(matriz_1[j])
    aux = j+1
    while(aux < numero_matriz):
        matriz_1[j][j] = elemento_mayor
        matriz_1[j][aux] = 0
        aux = aux + 1
        
    print(matriz_1[j])
    lista_agregar_columnas = []
    
        
    #print("asi queda la matriz::::: ",j, matriz_1)
    if(j == numero_matriz-2):
        break
    #print("el elemento mayor de la columna es: ",lista_ordenada[numero_matriz-1])



print("matiz despues del algoritmo \n")
for x in range(0,numero_matriz):
    print(matriz_1[x],"\n")

