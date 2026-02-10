class Producto:
    def __init__(self, nombre, fabricante, precio):
        self.nombre = nombre
        self.fabricante = fabricante
        self.precio = precio  
        
    def imprimir(self):
        
        print(f"{self.nombre} - {self.fabricante} - {self.precio}")
        
class Electronica(Producto): 
    def __init__(self, nombre, fabricante, precio, modo):
        super().__init__(nombre, fabricante, precio)
        self.modo = modo 
        
    def imprimir(self):
        super().imprimir()
        print(f"Modo: {self.modo}")
        
class Portatil(Electronica):
    def __init__(self, nombre, fabricante, precio, modo, ram):
        super().__init__(nombre, fabricante, precio, modo)
        self.ram = ram
        
    def imprimir(self):
        super().imprimir() 
        print("Portatil ram:", self.ram)
        
class Monitor(Electronica):
    def __init__(self, nombre, fabricante, precio, modo, resolucion):
        super().__init__(nombre, fabricante, precio, modo)
        self.resolucion = resolucion
        
    def imprimir(self):
        super().imprimir() 
        print("Monitor resolucion:", self.resolucion)

# --- Bloque principal ---

print("*************** Producto")
producto1 = Producto("Producto1", "Fabricante1", 100)
producto1.imprimir()

print("\n*************** Electronica")
electronica1 = Electronica("Electronica1", "Fabricante1", 100, "Modo1")
electronica1.imprimir()

print("\n*************** Portatil")
portatil1 = Portatil("Portatil1", "Fabricante1", 100, "Modo1", 32)
portatil1.imprimir()

print("\n*************** Monitor")
monitor1 = Monitor("Monitor1", "Fabricante1", 100, "Modo1", 1920)
monitor1.imprimir() 