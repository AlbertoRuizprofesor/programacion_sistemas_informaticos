class Compra:
    def __init__(self, producto, precio, meses):
        self.producto = producto
        self.precio = precio
        self.meses = meses
        self.recargo = 0
        self.precio_final = 0
        self.cuota_mensual = 0

    def calcular_financiacion(self):
        # Lógica del recargo: si es más de 6 meses, 5% de recargo
        if self.meses > 6:
            self.recargo = self.precio * 0.05
        else:
            self.recargo = 0
        
        self.precio_final = self.precio + self.recargo
        self.cuota_mensual = self.precio_final / self.meses

    def mostrar_ticket(self):
        print("--- DETALLE DE COMPRA ---")
        print(f"Producto: {self.producto}")
        print(f"Precio base: {self.precio} euros")
        print(f"Plazo: {self.meses} meses")
        
        if self.recargo > 0:
            print(f"Recargo aplicado (5%): {self.recargo} euros")
        else:
            print("Recargo aplicado: 0% (Pago en menos de 6 meses)")
            
        print(f"Precio final: {self.precio_final} euros")
        print(f"Cuota mensual: {self.cuota_mensual:.2f} euros/mes")
        print("-" * 25)


# Bloque principal
# Creamos el objeto con los datos del ejemplo
compra1 = Compra("Portatil Gaming Omen HP", 2000, 10)

# Ejecutamos los cálculos y mostramos el resultado
compra1.calcular_financiacion()
compra1.mostrar_ticket()