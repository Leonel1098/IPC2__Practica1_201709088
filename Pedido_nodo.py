from Lista_Ingredientes import Lista_Ingredientes
class Pedido_nodo :

    def __init__(self,nameCliente,addresCliente,numberCliente,cantidadPizza):
        self.nameCliente = nameCliente
        self.addresCliente = addresCliente
        self.numberCliente = numberCliente
        self.cantidadPizza = cantidadPizza
        self.Lista_Ingredientes = Lista_Ingredientes()
        self.time = None
        self.siguiente = None



    def set_Tiempo(self,time):
        self.time = time
    
    def set_siguiente(self):
        self.siguiente = siguiente

    def get_siguiente(self):
        return self.siguiente
    
    def get_nameCliente(self):
        return self.nameCliente
    
    def get_addresCliente(self):
        return self.addresCliente
    
    def get_numberCliente(self):
        return self.numberCliente
    
    def get_cantidadPizza(self):
        return self.cantidadPizza
    
    def get_Tiempo(self):
        return self.time

    