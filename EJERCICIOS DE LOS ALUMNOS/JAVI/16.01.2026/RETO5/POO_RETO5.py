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
    def __init__(self, nombre, fabricante, precio, categoria):
        super().__init__(nombre, fabricante, precio)
        self.categoria = categoria  # Por ejemplo: Gaming, Oficina, Profesional

    def imprimir(self):
        super().imprimir()
        print("Categoría:", self.categoria)


class Monitores(Electronica):
    def __init__(self, nombre, fabricante, precio, categoria, pulgadas):
        super().__init__(nombre, fabricante, precio, categoria)
        self.pulgadas = pulgadas

    def imprimir(self):
        super().imprimir()
        print("Pulgadas:", self.pulgadas)


class Teclado(Electronica):
    def __init__(self, nombre, fabricante, precio, categoria, ergonomico):
        super().__init__(nombre, fabricante, precio, categoria)
        self.ergonomico = ergonomico

    def imprimir(self):
        super().imprimir()
        print("Ergonómico:", self.ergonomico)


class Portatil(Electronica):
    def __init__(self, nombre, fabricante, precio, categoria, ram):
        super().__init__(nombre, fabricante, precio, categoria)
        self.ram = ram

    def imprimir(self):
        super().imprimir()
        print("RAM:", self.ram)


# ---------------- ELECTRODOMÉSTICOS ----------------

class Electrodomestico(Producto):
    def __init__(self, nombre, fabricante, precio, etiqueta):
        super().__init__(nombre, fabricante, precio)
        self.etiqueta = etiqueta  # Por ejemplo: A+, A++, A+++

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

# Entrada de datos
nombre = input("Ingrese el nombre del producto: ")
fabricante = input("Ingrese el fabricante: ")
precio = int(input("Ingrese el precio: "))
categoria = input("Ingrese la categoría (ej. Gaming, Oficina, Profesional): ")
etiqueta = input("Ingrese la etiqueta energética (ej. A+, A++, A+++): ")

print("\n____________________________\n")

# Crear instancias
producto = Producto(nombre, fabricante, precio)
producto.imprimir()

print("\n____________________________\n")

monitor = Monitores(nombre, fabricante, precio, categoria, "27 pulgadas")
monitor.imprimir()

print("\n____________________________\n")

teclado = Teclado(nombre, fabricante, precio, categoria, "Sí")
teclado.imprimir()

print("\n____________________________\n")

portatil = Portatil(nombre, fabricante, precio, categoria, "16 GB")
portatil.imprimir()

print("\n____________________________\n")

lavadora = Lavadora(nombre, fabricante, precio, etiqueta, "7 kg")
lavadora.imprimir()

print("\n____________________________\n")

frigorifico = Frigorifico(nombre, fabricante, precio, etiqueta, "No Frost")
frigorifico.imprimir()

print("\n____________________________\n")

freidora = Freidora(nombre, fabricante, precio, etiqueta, "230 °C")
freidora.imprimir()
