from Pedido_nodo import Pedido_nodo

class Lista_Pedidos():
    
    def __init__(self):
        self.anterior = None
        self.siguiente = None
        self.tamaño = 0
    
    def PedidoNuevo(self,nameCliente,addresCliente,numberCliente,cantidadPizza):
        nuevo = Pedido_nodo(nameCliente,addresCliente,numberCliente,cantidadPizza)
        self.tamaño += 1
        if self.anterior is None:
            self.anterior = nuevo
            self.ultimo = nuevo
        else :
            self.ultimo.set_siguiente(nuevo)
            self.ultimo = nuevo
        
        return nuevo













    