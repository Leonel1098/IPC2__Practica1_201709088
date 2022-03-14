from  Ingredientes_nodo import Ingredientes_nodo

class Lista_Ingredientes:
    def __init__(self):
        self.anterior = None
        self.siguiente = None
        self.size = 0

    def Ingrediente_Nuevo(self,nombre,tiempo):
        newIngrediente = Ingredientes_nodo(nombre,tiempo)
        self.size +=1
        if self.anterior is None:
            self.anterior = newIngrediente
            self.ultimo = newIngrediente
        else : 
            self.ultimo.set_Ingredientesiguiente(Ingrediente_Nuevo)
            self.ultimo = newIngrediente
    
    def Ingrediente_Mostrar(self):
        contador = self.anterior
        print("---Lista de Ingredientes---")
        for i in range(self.size):
            print(i+1)
            print("Nombre : ", contador.get_Nombre)
            print("Tiempo :", contador.get_Tiempo)
            contador = contador.get_Ingredientesiguiente()
            print("")

    def Tiempo(self):
        time = 0
        timer = self.anterior
        for i in range(self.size):
            tiempo += int(timer.get_tiempo())
            timer = timer.get_Ingredientesiguiente()
        print("")
        print("Tiempo de cada pizza :", time,)
        print("")
        return time

  
