class Compras:
    
    def __init__(self):
        self.producto = input("Dime el producto: ")
        self.precio = float(input("Dime el precio: "))
        # Valores por defecto
        self.meses = 1
        self.precio_total = self.precio
        self.cuota = self.precio
        # Funciones
        self.plazo()
        self.imprimir()
    
    def plazo(self):
        opcion = input("¿Quieres pagar a plazos? (S/N): ")
        
        if opcion.upper() == "S":
            print("ATENCION:\nSi la cantidad supera 6 meses, recibiras un cargo del 5%.")
            self.meses = int(input("¿Durante cuánto tiempo quieres? "))
            
            if self.meses > 6:
                self.precio_total = self.precio * 1.05
            
            self.cuota = self.precio_total / self.meses

    def imprimir(self):
        print(f"Producto: {self.producto}")
        print(f"Precio: {self.precio}")
        print(f"Número de meses a pagar: {self.meses}")
        print(f"Cuota: {self.cuota:.2f}")
        print(f"Precio final: {self.precio_total:.2f}")
