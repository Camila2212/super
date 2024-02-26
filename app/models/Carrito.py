from app.models.Producto import Producto

class Carrito:
    def __init__(self):
        self.carrito = []

    def agregar_producto(self, producto_id, cantidad):
        producto = Producto.query.get(producto_id)
        if producto:
            item = {'producto': producto, 'cantidad': cantidad}
            self.carrito.append(item)

    def calcular_total(self):
        return sum(item['producto'].precio * item['cantidad'] for item in self.carrito)
    
    def tamañoD(self):   
        return len(self.carrito)

    def getItems(self):
        return self.carrito
    
    def eliminarItem(self,item):
        print("Antes de eliminar item", item)
        self.carrito.remove(item)
        print("despues de eliminar item",item)
    
    def vaciarcarrito(self):
        self.carrito = []
    