'''
Crea una clase Producto y una clase Carrito. 
El carrito debe permitir añadir productos, eliminar productos, calcular el total y mostrar un resumen. 
Idea clave: Implementa __len__ para saber cuántos productos contiene. 
'''

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        
    def __eq__(self, otro):
        if not isinstance(otro, Producto):
            return False
        return self.nombre == otro.nombre and self.precio == otro.precio
        
class Carrito:
    def __init__(self):
        self.productos = []
        
    def añadir_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' añadido al carrito.")
    
    def eliminar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)
            print(f"Producto '{producto.nombre}' eliminado del carrito.")
        else:
            print(f"El producto '{producto.nombre}' no se encuentra en el carrito.")
        
    def calcular_total(self):
        total = sum(producto.precio for producto in self.productos)
        return total
    
    def __len__(self): 
        return len(self.productos) 
 
    def resumen(self): 
        for producto in self.productos: 
            print(f"- {producto.nombre}: {producto.precio:.2f} €") 
        print(f"Total: {self.calcular_total():.2f} €")
        

# main
carrito = Carrito()

carrito.añadir_producto(Producto("Juego", 15.99))
carrito.eliminar_producto(Producto("Juego", 15.99))  
carrito.añadir_producto(Producto("Libro", 9.99))
carrito.añadir_producto(Producto("Sushi", 10))
carrito.resumen()