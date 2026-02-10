class Producto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.stock = 0

    def reponer(self, unidades):
        self.stock = self.stock + unidades

    def vender(self, unidades):
        if unidades <= self.stock:
            self.stock = self.stock - unidades
        else:
            print(f"No hay suficiente stock de {self.nombre} para vender {unidades} unidades.")

    def retornar_stock(self):
        return self.stock

    def imprimir(self):
        print(f"Producto: {self.nombre} - Stock actual: {self.stock}")


class Tienda:
    def __init__(self):
        # Creamos tres productos iniciales como en el ejercicio 197
        self.producto1 = Producto("Manzanas")
        self.producto2 = Producto("Pan")
        self.producto3 = Producto("Leche")

    def abastecer(self):
        # Simulamos la entrada de mercancía
        self.producto1.reponer(50)
        self.producto2.reponer(30)
        self.producto3.reponer(100)

    def realizar_ventas(self):
        # Simulamos algunas ventas
        self.producto1.vender(10)
        self.producto2.vender(5)
        self.producto3.vender(120)  # Esto debería mostrar error por falta de stock

    def mostrar_estado_inventario(self):
        print("--- Estado del Inventario ---")
        self.producto1.imprimir()
        self.producto2.imprimir()
        self.producto3.imprimir()
        
        total_articulos = (self.producto1.retornar_stock() + 
                           self.producto2.retornar_stock() + 
                           self.producto3.retornar_stock())
        print("-" * 30)
        print(f"Total de artículos en tienda: {total_articulos}")


# Bloque principal (equivalente al del ejercicio 197)
mi_tienda = Tienda()
mi_tienda.abastecer()
mi_tienda.realizar_ventas()
mi_tienda.mostrar_estado_inventario()