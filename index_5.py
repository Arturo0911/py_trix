"""
Escriba un programa para controla el uso de camiones de una empresa. Cada
camión tiene un código. Ingrese como dato inicial la lisa d elos códigos de
los camiones. Programe una aplicación con las siguientes opciones:
            1. Salida de un camión.
            2. Devolución de un camión.
            3. Disponnibilidad de un camión.
            4. Terminar.
El operador elige la opción ingresando el número.

"""
camion_cod = {'cod001':'Camion 1','cod002':'Camion 2','cod003':'Camion 3','cod004':'Camion 4','cod005':'Camion 5'} # camiones con sus respectivos códigos.
lista_cod = ["cod001","cod002","cod003","cod004","cod005"] # la lista de los códigos de los camiones
lista_opciones = ["1. Salida de un camión.", "2. Devolución de un camión.","3. Disponnibilidad de un camión.", "4. Terminar."]
lista_backup_indices = []
camiones_ocupados = {}
camiones_ocupados_backup = {}

for y in lista_opciones:
    print(y)

print("\n")

for x in lista_cod:
    print(x)

print("\n")


while(True):    
        
    try:
        elegir_opc =  int(input("elija la opcion del programa: "))
        
        if(elegir_opc == 1):
            print("\n")
            print("usted ha seleccionado la opcion %s "%elegir_opc)
            for x in lista_cod:
                print(x)
            elegir_cod = str(input("Elija el codigo del camion que desee: "))
            print("usted ha seleccionado el camion %s para una salida "%camion_cod[str(elegir_cod)])
            indice = lista_cod.index(elegir_cod) # el indice de la lista de codigos, porque vamos a agregar esta varibale a la lista backup para quitarla de los
            # camiones disponibles 
            lista_backup_indices.append(elegir_cod)

            camiones_ocupados[elegir_cod] = str(indice)
            camiones_ocupados_backup[str(indice)] = elegir_cod
            lista_cod.pop(indice)
           
        elif(elegir_opc == 2):
            print("\n")
            print("camiones ocupados",len(lista_backup_indices))
            for z in lista_backup_indices:
                print(z)

            if(len(lista_backup_indices) > 0):
                desocupar_camion = input("elija que camion desea devolver: ")
                print("\n")
                print("usted ha seleccionado el camion %s" %desocupar_camion)
                print("\n")
                indice_1 = int(camiones_ocupados[desocupar_camion])
                print("object ocupados ",camiones_ocupados)
                #print("index_ %s"%indice_1)
                print("\n")
                #indice_2 = camiones_ocupados_backup[desocupar_camion]
                #print("object ocupados backup ",camiones_ocupados_backup)
                #print("index_2 %s"%indice_2)
                print("\n")
                lista_cod.insert(indice_1 ,desocupar_camion)
                lista_backup_indices.pop(lista_backup_indices.index(desocupar_camion))
                print("se agrego correctamente el camion ")
                """
                try:
                    desocupar_camion = input("elija que camion desea devolver: ")
                    print("\n")
                    print("usted ha seleccionado el camion %s" %desocupar_camion)
                    print("\n")
                    indice_1 = int(camiones_ocupados[desocupar_camion])
                    print("object ocupados ",camiones_ocupados)
                    print("index_ %s"%indice_1)
                    print("\n")
                    indice_2 = camiones_ocupados_backup[desocupar_camion]
                    print("object ocupados backup ",camiones_ocupados_backup)
                    print("index_2 %s"%indice_2)
                    print("\n")
                    lista_cod.insert(indice_1 ,indice_2)
                except:
                    print("numero de camion incorrecto para devolver")
                """
            else:
                print("no hay camiones ocupados...")
                print(len(lista_backup_indices))

        
        elif(elegir_opc == 3):
            elegir_cod = str(input("Elija el codigo del camion que desee: "))
            if(elegir_cod not in lista_cod):
                print("El camion %s se encuentra en servicio en estos momentos..."%camion_cod[str(elegir_cod)])
            else:
                print("el camion se encuentra disponible... ")


        elif(elegir_opc == 4):
            print("Fin del programa. ")
            break
    except:
        print("error al elegir opciones... ")
