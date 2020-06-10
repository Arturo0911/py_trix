import random

lista = ["Vue.js", "Angular.js", "React.js"]
lista_=[0,1,2]

for x in range(0, len(lista)):
    random_number = lista_[random.randint(0,2)]
    print(lista[random_number])
