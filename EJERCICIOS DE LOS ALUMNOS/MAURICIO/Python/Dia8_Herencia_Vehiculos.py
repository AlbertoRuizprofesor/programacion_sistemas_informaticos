class Vehiculo:

    def __init__(self, modelo, marca, precio):
        self.modelo = modelo
        self.marca = marca
        self.precio = precio

    def imprimir(self):
        print(f"Vehiculo: {self.modelo}")
        print(f"Fabricante: {self.marca}")
        print(f"Precio: {self.precio}")


class Transporte(Vehiculo):

    def __init__(self, modelo, marca, precio, numero_plazas):
        super().__init__(modelo, marca, precio)
        self.numero_plazas = numero_plazas

    def imprimir(self):
        super().imprimir()
        print("Número de Plazas: ", self.numero_plazas)
        if self.numero_plazas > 5:
            clase = "Transporte Maxivo"
        else:
            clase = "Transporte Particular"

        print(
            f"Los {self.numero_plazas} de {self.modelo} hacen este vehiculo de {clase}"
        )


class Autobus(Transporte):

    def __init__(self, modelo, marca, precio, numero_plazas, cine_gratis):
        super().__init__(modelo, marca, precio, numero_plazas)
        self.cine_gratis = cine_gratis

    def imprimir(self):
        super().imprimir()
        print("Cine Gratis?: ", self.cine_gratis)


class Moto(Transporte):

    def __init__(self, modelo, marca, precio, numero_plazas, manillar_pro_o_basico):
        super().__init__(modelo, marca, precio, numero_plazas)
        self.manillar_pro_o_basico = manillar_pro_o_basico

    def imprimir(self):
        super().imprimir()
        print("Tipo de Manillar: ", self.manillar_pro_o_basico)


class Coche(Transporte):

    def __init__(self, modelo, marca, precio, numero_plazas, descapotable):
        super().__init__(modelo, marca, precio, numero_plazas)
        self.descapotable = descapotable.lower()

    def imprimir(self):
        super().imprimir()
        if self.descapotable == "si":
            clase = "Vehiculo con Techo Rigido"
        else:
            clase = "vehiculo Descapotable"

        print(clase)


class Construccion(Vehiculo):

    def __init__(self, modelo, marca, precio, traccion):
        super().__init__(modelo, marca, precio)
        self.traccion = traccion.lower()

    def imprimir(self):
        super().imprimir()
        print("Tipo de traccion: ", self.traccion)
        if self.traccion.lower() == "rueda":
            traccion = "vehiculo de ruedas"
        else:
            traccion = "vehiculo de orugas"

        print(f"{self.modelo} {traccion}")


class Apisonadora(Construccion):

    def __init__(self, modelo, marca, precio, traccion, size_rodillo):
        super().__init__(modelo, marca, precio, traccion)
        self.size_rodillo = size_rodillo

    def imprimir(self):
        super().imprimir()
        print("Tamaño del Rodillo: ", self.size_rodillo)


class Excavadora(Construccion):

    def __init__(self, modelo, marca, precio, traccion, size_pala):
        super().__init__(modelo, marca, precio, traccion)
        self.size_pala = size_pala

    def imprimir(self):
        super().imprimir()
        print("Tamaño de Pala: ", self.size_pala)


class Hormigonera(Construccion):

    def __init__(self, modelo, marca, precio, traccion, capacidad_litros_hormigon):
        super().__init__(modelo, marca, precio, traccion)
        self.capacidad_litros_hormigon = capacidad_litros_hormigon

    def imprimir(self):
        super().imprimir()
        print(
            "Litros de cemento que puede transportar: ", self.capacidad_litros_hormigon
        )


# Bloque Principal

vehiculos = [
    Autobus(
        modelo="Autobus",
        marca="Protobus",
        precio=60000,
        numero_plazas=55,
        cine_gratis="Superior",
    ),
    Moto(
        modelo="Moto",
        marca="Honda",
        precio=24000,
        numero_plazas=1,
        manillar_pro_o_basico="Pro",
    ),
    Coche(
        modelo="Coche",
        marca="PhiliFerrari",
        precio=50000,
        numero_plazas=5,
        descapotable="Si",
    ),
    Apisonadora(
        modelo="Apisonadora",
        marca="Aplastatodo",
        precio=20000,
        traccion="Oruga",
        size_rodillo="XL",
    ),
    Excavadora(
        modelo="Excavadora",
        marca="Excabeitor",
        precio=120000,
        traccion="Orugag",
        size_pala="XXL",
    ),
    Hormigonera(
        modelo="Hormigonera",
        marca="Samsung",
        precio=300000,
        traccion="Oficina",
        capacidad_litros_hormigon=27000,
    ),
]

for vehiculo in vehiculos:
    print("_______________________\n")
    vehiculo.imprimir()
    print("_______________________\n")
