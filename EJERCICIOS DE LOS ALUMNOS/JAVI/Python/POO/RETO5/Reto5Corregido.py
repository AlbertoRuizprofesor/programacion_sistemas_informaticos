class Producto:
    def __init__(self, nombre, fabricante, precio):
        self.nombre = nombre
        self.fabricante = fabricante
        self.precio = precio

    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Fabricante:", self.fabricante)
        print("Precio:", self.precio)


# ---------------- ELECTRÓNICA ----------------

class Electronica(Producto):
    def __init__(self, nombre, fabricante, precio, modo):
        super().__init__(nombre, fabricante, precio)
        self.modo = modo

    def imprimir(self):
        super().imprimir()
        print("Modo:", self.modo)


class Monitores(Electronica):
    def __init__(self, nombre, fabricante, precio, modo, pulgadas):
        super().__init__(nombre, fabricante, precio, modo)
        self.pulgadas = pulgadas

    def imprimir(self):
        super().imprimir()
        print("Pulgadas:", self.pulgadas)


class Teclado(Electronica):
    def __init__(self, nombre, fabricante, precio, modo, ergonomico):
        super().__init__(nombre, fabricante, precio, modo)
        self.ergonomico = ergonomico

    def imprimir(self):
        super().imprimir()
        print("Ergonómico:", self.ergonomico)


class Portatil(Electronica):
    def __init__(self, nombre, fabricante, precio, modo, ram):
        super().__init__(nombre, fabricante, precio, modo)
        self.ram = ram

    def imprimir(self):
        super().imprimir()
        print("RAM:", self.ram)


# ---------------- ELECTRODOMÉSTICOS ----------------

class Electrodomestico(Producto):
    def __init__(self, nombre, fabricante, precio, etiqueta):
        super().__init__(nombre, fabricante, precio)
        self.etiqueta = etiqueta

    def imprimir(self):
        super().imprimir()
        print("Etiqueta energética:", self.etiqueta)


class Lavadora(Electrodomestico):
    def __init__(self, nombre, fabricante, precio, etiqueta, carga):
        super().__init__(nombre, fabricante, precio, etiqueta)
        self.carga = carga

    def imprimir(self):
        super().imprimir()
        print("Carga:", self.carga)


class Frigorifico(Electrodomestico):
    def __init__(self, nombre, fabricante, precio, etiqueta, tipo):
        super().__init__(nombre, fabricante, precio, etiqueta)
        self.tipo = tipo

    def imprimir(self):
        super().imprimir()
        print("Tipo:", self.tipo)


class Freidora(Electrodomestico):
    def __init__(self, nombre, fabricante, precio, etiqueta, temperatura):
        super().__init__(nombre, fabricante, precio, etiqueta)
        self.temperatura = temperatura

    def imprimir(self):
        super().imprimir()
        print("Temperatura máxima:", self.temperatura)


# ---------------- PROGRAMA PRINCIPAL ----------------

nombre = input("Ingrese el nombre: ")
fabricante = input("Ingrese el fabricante: ")
precio = int(input("Ingrese el precio: "))

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

monitor = Monitores(nombre, fabricante, precio, "Profesional", "27 pulgadas")
monitor.imprimir()

print("____________________________")

teclado = Teclado(nombre, fabricante, precio, "Oficina", "Sí")
teclado.imprimir()

print("____________________________")

portatil = Portatil(nombre, fabricante, precio, "Gaming", "16 GB")
portatil.imprimir()

print("____________________________")

lavadora = Lavadora(nombre, fabricante, precio, "A+++", "7 kg")
lavadora.imprimir()

print("____________________________")

frigorifico = Frigorifico(nombre, fabricante, precio, "A++", "No Frost")
frigorifico.imprimir()

print("____________________________")

freidora = Freidora(nombre, fabricante, precio, "A", "230 °C")
freidora.imprimir()
