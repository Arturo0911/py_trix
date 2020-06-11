"""
Un problema hospitalario es la falta de control de las medicinas. Suponga que una percha de farmacia tiene  casillas ubicadas 
en n filas y m columas cada casilla contiene los siguientes datos: códigos del medicamento y la cantidad de cajas disponibles.

Para organizar el sistema de control de inventario escriba un programa con una matriz para representar la percha en la que cada casilla
contendrá el código y la cantida de cajas de cada elemento. El progrrama debe funcionar con un menú con las siguientes opciones:

        1) Iniciar una casilla. Especificar la fila y columna. Almacenar el código del medicamento
            y la cantidad inicial de cajas de medicamento
        2) consultar si una casilla estpa disponible(el código del medicamento es 0)
        3) Mostrar la ubicación (fila y columna) de un medicamento, dado su código
        4) Mostrar la cantidad de cajas disponibles de un medicamento dado su código
        5) Agregar más cajas de un medicamento. Especificar el código y la cantidad
        6) Sacas cajas de un medicamento. Especificar el codigo y la cantidad.
        7) Eliminar un medicamento de la percha. Especificar la fila y columna. Asinar
            cero al codigo del medicamento y la cantidad de cajas.
        8) Salir

"""



print("Aplicacion para controlar el inventario de un hospital, a continuacion se mostrara el codigo de cada elemento y su descripcion \n")


# definimos la matriz de nxm
matriz_inventario = [[{},{},{}],[{},{},{}],[{},{},{}],[{},{},{}]] # para hacer la prueba definimos una matriz de 4x3 4 filas y 3 columnas


# el codigo de los productos con su respectiva descripcion
#cod_names = {"cod_001": "Penicilina","cod_002": "Ibuprofeno","cod_003": "Paracetamol","cod_004": "Cajas de jeringas","cod_005": "Caja de guantes",
#"cod_006": "Caja de mascarillas","cod_007": "Pruebas de embarazo","cod_008": "Preservatios","cod_009": "Pastillas del dia siguiente","cod_010": "Alcohol 95"}
cod_names_test = {}







# la lista de codigos
#cod_list = ['cod_001','cod_002','cod_003','cod_004','cod_005','cod_006','cod_007','cod_008','cod_009','cod_010']
cod_list_test = []





#lista de las opciones
opcion_list =["1) Iniciar una casilla. Especificar la fila y columna. Almacenar el codigo del medicamento y la cantidad inicial de cajas de medicamento",
"2) consultar si una casilla estpa disponible(el codigo del medicamento es 0)", "3) Mostrar la ubicacion (fila y columna) de un medicamento, dado su código",
"4) Mostrar la cantidad de cajas disponibles de un medicamento dado su código", "5) Agregar mas cajas de un medicamento. Especificar el codigo y la cantidad",
"6) Sacas cajas de un medicamento. Especificar el codigo y la cantidad.",
"7) Eliminar un medicamento de la percha. Especificar la fila y columna. Asignar cero al codigo del medicamento y la cantidad de cajas. ","8) Salir"]


#for x in cod_list:
    #print("codigo del producto (%s) y su descripcion: =>  %s"%(x,cod_names[x]))

print("\n")


while(True):
    for y in opcion_list:
        print(y)
    try:
        select_option = int(input("elija la opcion de las que estan mostradas: "))
        print("\n")

        if(select_option == 1):
            print("En estos momentos hay %s filas y %s columnas"%(len(matriz_inventario),len(matriz_inventario[0])))
            fila = int(input("indique la fila: "))
            columna = int(input("indique la columna: "))
            
            # HACEMOS LA VALIDACION DE QUE SE ESTÉ ELIGIENDO FILAS Y COLUMNAS DENTRO DEL LIMITE. NO QUEREMOS QUE SE ELIJA UNA FILA QUE NO EXISTA
            
            if(fila>len(matriz_inventario) or columna > len(matriz_inventario[0])):
                print("esta sobrepasando el limite de filas o columnas")
            else:
                print("\n")
                codigo_producto = input("indique el codigo del producto: ")
                print("\n")
                descripcion_producto =  input("indique la descripcion del producto: ")
                print("\n")
                cantidad_producto =  int(input("indique la cantidad de unidades de este producto: "))
                print("\n")
                
                # AGREGAMOS EN UN DICCIONARIO CON SU CODIGO Y DESCRIPCION, EN UNA LISTA LOS CODIGOS QUE ACABMOS DE INTRODUCIR
                cod_names_test[codigo_producto] = descripcion_producto
                cod_list_test.append(codigo_producto)

                # AHORA AGREGAMOS EN LA FILA Y COLUMNA QUE ESPECIFICAMOS ARRIBA
                matriz_inventario[fila-1][columna-1][codigo_producto] = cantidad_producto


    
        elif(select_option == 2):
            print("usted ha seleccinado para verificar si una casilla esta disponible...")
            try:
                fila = int(input("indique la fila: "))
                columna = int(input("indique la columna: "))
                if(fila > len(matriz_inventario) or columna >len(matriz_inventario[0])):
                    print("fila o valor de columna exceden o no estan en el invetario")
                else:
                    if(len(matriz_inventario[fila][columna])>0):
                        print("la casilla se encuentra ocupada %s"%matriz_inventario[fila][columna])
                    else:
                        print("la casilla se encuentra disponible %s"%matriz_inventario[fila][columna])
            except:
                print("numeracion incorrecta... ")

        elif(select_option == 3):
            print("\n")
            codigo_producto = input("indique el codigo del producto que desea buscar: ")
            for i in range(0,len(matriz_inventario)):
                for j in range (0,len(matriz_inventario[0])):
                    if(codigo_producto in matriz_inventario[i][j]):
                        print("El producto se enccuentra en la fila %s columna %s"%(i+1,j+1))
            print("\n")
        elif(select_option==4):
            print("\n")
            codigo_producto = input("indique el codigo del producto que desea buscar: ")
            for i in range(0,len(matriz_inventario)):
                for j in range (0,len(matriz_inventario[0])):
                    if(codigo_producto in matriz_inventario[i][j]):
                        print("El producto %s  se enccuentra en la fila %s columna %s "%(cod_names_test[codigo_producto],i+1,j+1))
                        print("y contiene %s unidades \n"%matriz_inventario[i][j][codigo_producto])
                    else:
                        print("no se encontro el producto en el codigo proporcionado")

        elif(select_option==5):
            print("\n")
            codigo_producto = input("indique el codigo del producto que desea buscar: ")
            while(True):
                try:
                    aumento = int(input("indique la cantidad de unidades que desea aumentar, ejemplo: si tenia 20 y ahora quiere tener 60; solo debe colocar 60 que es la cantidad total que va a tener ahora: "))
                    break
                except:
                    print("cantidad erronea")    
            

            for i in range(0,len(matriz_inventario)):
                for j in range (0,len(matriz_inventario[0])):
                    if(codigo_producto in matriz_inventario[i][j]):
                        print("El producto %s  se enccuentra en la fila %s columna %s "%(cod_names_test[codigo_producto],i+1,j+1))
                        print("y contiene %s unidades \n"%matriz_inventario[i][j][codigo_producto])
                        matriz_inventario[i][j][codigo_producto] = aumento
                        print("Ahora contiene %s unidades despues de haberle agregado mas \n"%matriz_inventario[i][j][codigo_producto])
                    else:
                        print("no se encontro el producto en el codigo proporcionado")

        elif(select_option==6):
            print("\n")
            codigo_producto = input("indique el codigo del producto que desea buscar: ")
            while(True):
                try:
                    disminucion = int(input("indique la cantidad de unidades que desea sacar: "))
                    break
                except:
                    print("cantidad erronea")    
            

            for i in range(0,len(matriz_inventario)):
                for j in range (0,len(matriz_inventario[0])):
                    if(codigo_producto in matriz_inventario[i][j]):
                        
                        print("El producto %s  se enccuentra en la fila %s columna %s "%(cod_names_test[codigo_producto],i+1,j+1))
                        print("y contiene %s unidades \n"%matriz_inventario[i][j][codigo_producto])
                        last_total = matriz_inventario[i][j][codigo_producto]
                        if(disminucion <= last_total):
                            matriz_inventario[i][j][codigo_producto] = last_total - disminucion
                            print("Haz sacado %s Ahora contiene %s unidades despues de haberle agregado mas \n"%(disminucion,matriz_inventario[i][j][codigo_producto]))
                    else:
                        print("no se encontro el producto en el codigo proporcionado")

        elif(select_option==7):
            print("haz seleccionado la opcion para eliminar un elemento de la casilla")
            print("\n")
            codigo_producto = input("indique el codigo del producto que desea eliminar: ")
            
            for i in range(0,len(matriz_inventario)):
                for j in range (0,len(matriz_inventario[0])):
                    if(codigo_producto in matriz_inventario[i][j]):
                        
                        print("El producto %s  se enccuentra en la fila %s columna %s "%(cod_names_test[codigo_producto],i+1,j+1))
                        print("y contiene %s unidades \n"%matriz_inventario[i][j][codigo_producto])
                        del matriz_inventario[i][j][codigo_producto]
                        matriz_inventario[i][j]["0"] = "0"
                        print("item fue eliminado exitosamente...")
                    else:
                        print("no se encontro el producto en el codigo proporcionado")
        elif(select_option == 8):
            print("fin del programa...")
            break
    except:
        print("Error al seleccionar opcion")