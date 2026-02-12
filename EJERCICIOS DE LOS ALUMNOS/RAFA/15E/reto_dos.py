class Compras:

    def __init__(self, producto, precio, meses):
        self.producto = producto
        self.precio = precio
        self.meses = meses

    def calcular_recargo(self):
        if self.meses > 6:
            return self.precio * 0.05
        else:
            return 0

    def calcular_precio_final(self):
        return self.precio + self.calcular_recargo()

    def calcular_cuota(self):
        return self.calcular_precio_final() / self.meses

    def mostrar_compra(self):
        print(f"Producto: {self.producto}")
        print(f"Precio inicial: {self.precio} €")
        print(f"Número de meses: {self.meses}")

        if self.calcular_recargo() > 0:
            print(f"Recargo 5%: {self.calcular_recargo()} €")
        else:
            print("Sin recargo")

        print(f"Precio final: {self.calcular_precio_final()} €")
        print(f"Cuota mensual: {self.calcular_cuota()} €")


#MAIN
compra = Compras("Portatil Gaming Omnio HP", 2000, 10)
compra.mostrar_compra()
