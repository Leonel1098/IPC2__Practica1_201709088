def Menu():

    opcion = True  
    
    while opcion :
        
        print("**** Funciones del Sistema ****")
        print("---1. Ingresar Orden")
        print("---2. Entregar Orden")
        print("---3. Gráfica")
        print("---4. Salir")
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

    print("Ingrese su dirección")
    direccion = input("")

    print("Ingrese su nombre")
    nombre = input("")

    print("Ingrese su número de teléfono")
    telefono = input("")


Menu()



