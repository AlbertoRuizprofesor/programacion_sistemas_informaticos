"""

"""

class Producto:

    def __init__(self, nombre, fabricante, precio):
        self.nombre = nombre
        self.fabricante = fabricante
        self.precio = precio
    
    def imprimir(self):
        print("El producto es: ", self.nombre)
        print("El fabricante es: ", self.fabricante)
        print("El precio es: ", self.precio)

class Electronica(Producto):

    def __init__(self, nombre, fabricante, precio, modo):
        super().__init__(nombre, fabricante, precio)
        self.modo = modo
        
    def imprimir(self):
        super().imprimir()
        print("Categoria: " , self.modo)

class Electrodomestico(Producto):

    def __init__(self, nombre, fabricante, precio, etiqueta):
        super().__init__(nombre, fabricante, precio)
        self.etiqueta = etiqueta
    
    def imprimir(self):
        super().imprimir()
        print("Categoria: " , self.etiqueta)

class Monitores(Electronica):

    def __init__(self, nombre, fabricante, precio, modo, pulgadas):
        super().__init__(nombre, fabricante, precio, modo)
        self.pulgadas = pulgadas
    
    def imprimir(self):
        super().imprimir()
        print("Categoria: " , self.pulgadas)

class Teclado(Electronica):

    def __init__(self, nombre, fabricante, precio, modo, ergo):
        super().__init__(nombre, fabricante, precio, modo)
        self.ergo = ergo
    
    def imprimir(self):
        super().imprimir()
        print("Categoria: " , self.ergo)

class Portatil(Electronica):

    def __init__(self, nombre, fabricante, precio, modo, ram):
        super().__init__(nombre, fabricante, precio, modo)
        self.ram = ram
    
    def imprimir(self):
        super().imprimir()
        print("Categoria: " , self.ram)

class Lavadora(Electrodomestico):

    def __init__(self, nombre, fabricante, precio, etiqueta, carga):
        super().__init__(nombre, fabricante, precio, etiqueta)
        self.carga = carga

    def imprimir(self):
        super().imprimir()
        print("Categoria: " , self.carga)

class Frigorifico(Electrodomestico):

    def __init__(self, nombre, fabricante, precio, etiqueta, tipo):
        super().__init__(nombre, fabricante, precio, etiqueta)
        self.tipo = tipo
    
    def imprimir(self):
        super().imprimir()
        print("Categoria: " , self.tipo)

class Lavadora(Electrodomestico):

    def __init__(self, nombre, fabricante, precio, etiqueta, carga):
        super().__init__(nombre, fabricante, precio, etiqueta)
        self.carga = carga
    
    def imprimir(self):
        super().imprimir()
        print("Categoria: " , self.carga)

class Frigorifico(Electrodomestico):

    def __init__(self, nombre, fabricante, precio, etiqueta, tipo):
        super().__init__(nombre, fabricante, precio, etiqueta)
        self.tipo = tipo
    
    def imprimir(self):
        super().imprimir()
        print("Categoria: " , self.tipo)

class Freidora(Electrodomestico):

    def __init__(self, nombre, fabricante, precio, etiqueta, temp):
        super().imprimir()
        self.temp = temp
    
    def imprimir(self):
        super().imprimir()
        print("Categoria: " , self.temp)



nombre = input("Ingrese el nombre: ")
fabricante = input("Ingrese el fabricante: ")
precio = int(input("Ingrese el precio: "))
modo = input("Dime el modo(ergonomico): ")
etiqueta = "A"

print("____________________________")

producto1 = Producto(nombre, fabricante, precio)
producto1.imprimir()

print("____________________________")

electronica1 = Electronica(nombre, fabricante, precio, "Gaming")
electronica1.imprimir()

print("____________________________")

electrodomestico1 = Electrodomestico(nombre, fabricante, precio, "A+")
electrodomestico1.imprimir()

print("____________________________")

monitores = Monitores(nombre, fabricante, precio, modo, "Ergonomico")
monitores.imprimir()

print("____________________________")

teclado = Teclado(nombre, fabricante, precio, modo, "Ergonomico")
teclado.imprimir()

print("____________________________")

portatil = Portatil(nombre, fabricante, precio, modo, "16GB")
portatil.imprimir()


monitores = Lavadora(nombre, fabricante, precio, etiqueta, "7 kg")
monitores.imprimir()

print("____________________________")

teclado = Frigorifico(nombre, fabricante, precio, etiqueta, "No Frost")
teclado.imprimir()

print("____________________________")

portatil = Freidora(nombre, fabricante, precio, etiqueta, "Temp 230ºC")
portatil.imprimir()










    


    

