class Producto:

    def __init__(self, nombre, fabricante, precio):
        self.nombre = nombre
        self.fabricante = fabricante
        self.precio = precio

    def imprimir(self):
        print(f"Producto: {self.nombre}")
        print(f"Fabricante: {self.fabricante}")
        print(f"Precio: {self.precio}")


class Electrodomestico(Producto):

    def __init__(self, nombre, fabricante, precio, consumo):
        super().__init__(nombre, fabricante, precio)
        self.consumo = consumo

    def imprimir(self):
        super().imprimir()
        print("Consumo: ", self.consumo)
        if self.consumo > 1200:
            clase = "Alto consumo"
        else:
            clase = "Bajo Consumo"

        print(f"Los {self.consumo} de {self.nombre} hacen este producto de {clase}")


class Lavadora(Electrodomestico):

    def __init__(self, nombre, fabricante, precio, consumo, carga):
        super().__init__(nombre, fabricante, precio, consumo)
        self.carga = carga

    def imprimir(self):
        super().imprimir()
        print("Tipo de Carga: ", self.carga)


class Frigorifico(Electrodomestico):

    def __init__(self, nombre, fabricante, precio, consumo, capacidad):
        super().__init__(nombre, fabricante, precio, consumo)
        self.capacidad = capacidad

    def imprimir(self):
        super().imprimir()
        print("Litros de Capacidad: ", self.capacidad)


class Freidora(Electrodomestico):

    def __init__(self, nombre, fabricante, precio, consumo, tipo):
        super().__init__(nombre, fabricante, precio, consumo)
        self.tipo = tipo

    def imprimir(self):
        super().imprimir()
        print("Tipo de freidora Aire/Aceite: ", self.tipo)


class Electronica(Producto):

    def __init__(self, nombre, fabricante, precio, modo):
        super().__init__(nombre, fabricante, precio)
        self.modo = modo

    def imprimir(self):
        super().imprimir()
        print("Modo: ", self.modo)
        if self.modo.lower() == "gaming":
            modo = "para Gaming"
        else:
            modo = "para Oficina"

        print(f"{self.nombre} {modo}")


class Portatil(Electronica):

    def __init__(self, nombre, fabricante, precio, modo, ram):
        super().__init__(nombre, fabricante, precio, modo)
        self.ram = ram

    def imprimir(self):
        super().imprimir()
        print("Ram: ", self.ram)


class Teclado(Electronica):

    def __init__(self, nombre, fabricante, precio, modo, ergonomico):
        super().__init__(nombre, fabricante, precio, modo)
        self.ergonomico = ergonomico

    def imprimir(self):
        super().imprimir()
        print("Ergonomía: ", self.ergonomico)


class Monitor(Electronica):

    def __init__(self, nombre, fabricante, precio, modo, pulgadas):
        super().__init__(nombre, fabricante, precio, modo)
        self.pulgadas = pulgadas

    def imprimir(self):
        super().imprimir()
        print("Pulgadas: ", self.pulgadas)


# Bloque Principal

productos = [
    Lavadora(
        nombre="Lavadora",
        fabricante="Zanussi",
        precio=1200,
        consumo=2400,
        carga="Superior",
    ),
    Frigorifico(
        nombre="Frigorífico", fabricante="Bosch", precio=900, consumo=800, capacidad=350
    ),
    Freidora(
        nombre="Freidora", fabricante="Philips", precio=150, consumo=1800, tipo="Aire"
    ),
    Portatil(
        nombre="Portátil", fabricante="HP", precio=2000, modo="Gaming", ram="16GB"
    ),
    Teclado(
        nombre="Teclado",
        fabricante="Logitech",
        precio=120,
        modo="Gaming",
        ergonomico="Sí",
    ),
    Monitor(
        nombre="Monitor", fabricante="Samsung", precio=300, modo="Oficina", pulgadas=27
    ),
]

for producto in productos:
    print("_______________________\n")
    producto.imprimir()
    print("_______________________\n")
