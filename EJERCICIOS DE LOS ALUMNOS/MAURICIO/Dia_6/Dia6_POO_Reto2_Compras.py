# Realizar con poo una clase Compras, que además me permite pagar a plazos dicha compra,
# con las funciones que sea necesario:

# ejemplo:

# Producto: Portatil Gaming omnio HP
# Precio: 2000 euros
# Número de meses a pagar: 10 (En el caso que el número de meses sea mas de 6 meses, un recargo del 5%)
# Cuota: (2000+(5%*2000))/10 (numero de meses que voy a estar pagando)
# Precio final: (2000+(5%*2000))


class Compras:
    def __init__(self, producto, precio):
        self.producto = producto
        self.precio = precio

    def calcular_cuota(self, meses):
        if meses > 6:
            recargo = 0.05 * self.precio
        else:
            recargo = 0
        precio_final = self.precio + recargo
        cuota = precio_final / meses
        return cuota, precio_final


# Ejemplo de uso
compra = Compras("Portatil Gaming omnio HP", 2000)
cuota, precio_final = compra.calcular_cuota(10)
print(f"Producto: {compra.producto}")
print(f"Precio final: {precio_final} euros")
print(f"Cuota mensual: {cuota} euros")
# Salida esperada:
# Producto: Portatil Gaming omnio HP
# Precio final: 2100.0 euros
# Cuota mensual: 210.0 euros
cuota, precio_final = compra.calcular_cuota(5)
print(f"\nProducto: {compra.producto}")
print(f"Precio final: {precio_final} euros")
print(f"Cuota mensual: {cuota} euros")
# Salida esperada:
# Producto: Portatil Gaming omnio HP
# Precio final: 2000 euros
# Cuota mensual: 400.0 euros
