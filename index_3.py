import random

"""
Lea una matriz  NxM. Para cada fila, muestre el producto de los elementos cuyo valor es un número par
"""
random_list = list()
for k in range(0,10):
    random_list.append(k)



matriz = [[3,4,7],[8,4,10],[17,5,1],[12,2,7]] # esta es una matriz de prueba
matriz_final = [] # con esta matriz vamos a trabajar
print("la matriz original es= \n")

primer_numero_random = random_list[random.randint(3,9)]
segudo_numero_random = random_list[random.randint(3,9)]

print("vamos a crear una matriz de %sx%s"%((primer_numero_random+1),segudo_numero_random))
# aqui vamos a crear una matriz de NxM

for x in range (0,primer_numero_random+1):
    lista_add = list()
    contador_1 = 0
    while(contador_1 <segudo_numero_random):
        lista_add.append(random_list[random.randint(0,9)])
        contador_1 = contador_1 + 1

    matriz_final.append(lista_add)

print("\n")
for l in range( 0, len(matriz_final)):
    print(matriz_final[l],"\n")



print("\n")



for i in range(0, len(matriz_final)):
    print(matriz_final[i],"\n")
    producto = 1
    for j in matriz_final[i]:
        if(j%2 ==0 and j!=0):
            #print("El numero %s es par "%j)
            producto = producto * j
    if(producto>1):
        print("el producto de la fila %s de numeros pares es %s"%(i+1,producto))
        print("------------------------------------")
