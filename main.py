from Lista_Ingredientes import Lista_Ingredientes 
from Lista_Pedidos import Lista_Pedidos
pedidos = Lista_Pedidos()
ingrediente = Lista_Ingredientes()
def Menu():

    opcion = True  
    
    while opcion :
        
        print("**** Funciones del Sistema ****")
        print("---1. Ingresar Orden")
        print("---2. Entregar Orden")
        print("---3. Gráfica")
        print("---4. Datos del Estudiante")
        print("---5. Salir")
        print("** Elija una opción **")
        opcion = input ("")
        if opcion == "1" :
            print("")
            print("---------- Nueva Orden -----------")
            Datos()
            print("")

        elif opcion == "2" :
            print("")
            print("--------- Orden Entregada ----------")
            print("")

        elif opcion == "3" :
            print("")
            print("---------- Gráfica ----------")
            #print(Datos)
            print("")
        elif opcion == "4" :
            print("")
            print("--------- Datos ---------")
            print("")
            print("Leonel Antonio González García")
            print("201709088")
            print("3636192320115")
            print("Laboratorio de Introducción a la Programación 2")
            print("")
        elif opcion == "5" :
            print("")
            print("----------Gracias, vuelve pronto :) --------")
            opcion = False
            print("")
            
        else:
            input("Ingrese una opción válida :)")
            print("")

def Datos():
    datos = ""
    nombre = ""
    telefono = ""
    pizza = ""
    cantingrediente = ""

    print("Ingrese su nombre")
    nombre = input()

    print("Ingrese su dirección")
    direccion = input()

    print("Ingrese su número de teléfono")
    telefono = input()

    print("Ingrese la cantidad de pizzas")
    cantpizza = input()

    print("Ingrese la cantidad de Ingredientes")
    cantingrediente = input()
    
    i = 0
    pedidonew = pedidos.PedidoNuevo(nombre,direccion,telefono,cantpizza)
    while i < int(cantingrediente) : 
        print("------Elija el Ingrediente para su pizza------")
        print("1. Pepperoni")
        print("2. Salchicha")
        print("3. Carne")
        print("4. Queso")
        print("5. Piña")
        opcion = int(input())
        
        if opcion == 1:
            print("")
            print("--Ingrediente Pepperoni Agregado--")
            pedidonew.Lista_Ingredientes.Ingrediente_Nuevo("Pepperoni",3)
            print("")
            i += 1

        elif opcion == 2:
            print("")
            print("--Ingrediente Salchicha Agregado--")
            pedidonew.Lista_Ingredientes.Ingrediente_Nuevo("Salchicha",4)
            print("")
            i += 1

        elif opcion == 3:
            print("")
            print("--Ingrediente Carne Agregado--")
            pedidonew.Lista_Ingredientes.Ingrediente_Nuevo("Carne",10)
            print("")
            i += 1
        
        elif opcion == 4:
            print("")
            print("-- Ingrediente Queso Agregado--")
            pedidonew.Lista_Ingredientes.Ingrediente_Nuevo("Queso",5)
            print("")
            i += 1

        elif opcion == 5:
            print("")
            print("-- Ingrediente Piña Agregado--")
            pedidonew.Lista_Ingredientes.Ingrediente_Nuevo("Piña",2)
            print("")
            i += 1
        else :
            print("Opción no válida :( ")



Menu()


