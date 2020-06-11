"""
Un grafo consta de vértices que pueden represenarse mediante circulos y arcos
que los conectan. Esta conectividad puede describirse mediante una matriz en la
que el valor 1 indica que existe un arco en esa dirección, mientras que el valor0
indica que no existe el arco con esa dirección, como se muestra en el ejemplo.


Escriba un programa para almacenar 0 ó 1 aleatoriamente en una matriz nxn, siendo
n un dato que debe leerse inicialmente. Dentro del programa llene la diagonal con 1's para
indicar que cada nodo está conectado consigo mismo. El programa examinar las filas
para determinar.

    a) Cual nodo no tiene conecciones con todos los otros nodos(no tiene arcos)
    b) Cual es el nodo que tiene más conecciones con otros nodos.
"""
import random


random_list = [0,1] # una lista de valores para utilzarla al momento de querer instanciar va,lores al azar

while(True):
    try:
        numero_matriz =  int(input("indique la dimensión de la matriz: "))
        break
    except:
        print("Valor no corresponde a un valor numerico")
        

matriz = [] # aqui declarams nuestra matriz

# Mediante esta lista vamos a agregar las conexiones que tienen por nodos
lista_nodos = list()



for i in range(0,numero_matriz):
    lista_add = list()
    for j in range(0,numero_matriz):
        numero_azar = random_list[random.randint(0,1)]
        lista_add.append(numero_azar)
        #print(i,j)
    matriz.append(lista_add)

for x in matriz:
    print(x,"\n")


for y in range(0,numero_matriz):
    for z in range(0, numero_matriz):
        if(y==z):
            matriz[y][z] = 1

print("matriz cambiada por el algoritmo \n")
for x in matriz:
    print(x,"\n")

print(" ---------------------------------------------------------") 
print("-----------------------------------------------------------")    
for a in range(0, numero_matriz):
    contador_nodo = 0
    for b in range(0, numero_matriz):
        if(matriz[a][b] == 1):
            print("El nodo %s está conectado con el nodo %s"%(a+1,b+1))
            contador_nodo = contador_nodo + 1
    lista_nodos.append(contador_nodo)

lista_ordenada = sorted(lista_nodos)
indice = lista_nodos.index(lista_ordenada[numero_matriz-1])


print(" ---------------------------------------------------------") 
print("-----------------------------------------------------------") 
print("\n")
print("El nodo %s fue el que  conexiones y fueron: %s"%(indice+1,lista_ordenada[numero_matriz-1]))
print("\n")
print(" ---------------------------------------------------------") 
print("-----------------------------------------------------------")
print("\n")
for x in matriz:
    print(x,"\n")