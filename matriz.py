import math

indice_ = [2,3,4,5]
lista = [2,3,4,5]
matriz  = []

def van(indice_):
    for x in range(0, len(indice_)):
        list_add = list()
        for y in range(0, len(indice_)):
            numero = indice_[x]
            potencia = int( math.pow(numero,y))
            list_add.append(potencia)
        matriz.append(list_add)

    for i in range(0, len(indice_)):
        print (matriz[i], "\n")

    return "matriz Vandermonde"




print(van(lista))
