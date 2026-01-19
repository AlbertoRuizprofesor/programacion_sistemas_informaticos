# --- Clase Padre (Nivel 1) ---
class Vehiculo:
    def __init__(self, marca, modelo, combustible):
        self.marca = marca
        self.modelo = modelo
        self.combustible = combustible

    def imprimir(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Combustible: {self.combustible}")

# --- Clases Intermedias (Nivel 2) ---
class Transporte(Vehiculo):
    def __init__(self, marca, modelo, combustible, capacidad):
        super().__init__(marca, modelo, combustible)
        self.capacidad = capacidad

    def imprimir(self):
        super().imprimir()
        print(f"Capacidad: {self.capacidad} personas")

class Construccion(Vehiculo):
    def __init__(self, marca, modelo, combustible, potencia):
        super().__init__(marca, modelo, combustible)
        self.potencia = potencia

    def imprimir(self):
        super().imprimir()
        print(f"Potencia: {self.potencia} CV")

# --- Ramas de Transporte (Nivel 3) ---
class Autobus(Transporte):
    def __init__(self, marca, modelo, combustible, capacidad, piso_bajo):
        super().__init__(marca, modelo, combustible, capacidad)
        self.piso_bajo = piso_bajo

    def imprimir(self):
        print("\n--- FICHA AUTOBÚS ---")
        super().imprimir()
        print(f"Accesible (Piso bajo): {self.piso_bajo}")

class Moto(Transporte):
    def __init__(self, marca, modelo, combustible, capacidad, tipo_carnet):
        super().__init__(marca, modelo, combustible, capacidad)
        self.tipo_carnet = tipo_carnet

    def imprimir(self):
        print("\n--- FICHA MOTO ---")
        super().imprimir()
        print(f"Licencia requerida: {self.tipo_carnet}")

class Coche(Transporte):
    def __init__(self, marca, modelo, combustible, capacidad, puertas):
        super().__init__(marca, modelo, combustible, capacidad)
        self.puertas = puertas

    def imprimir(self):
        print("\n--- FICHA COCHE ---")
        super().imprimir()
        print(f"Número de puertas: {self.puertas}")

# --- Ramas de Construcción (Nivel 3) ---
class Excavadora(Construccion):
    def __init__(self, marca, modelo, combustible, potencia, profundidad_max):
        super().__init__(marca, modelo, combustible, potencia)
        self.profundidad_max = profundidad_max

    def imprimir(self):
        print("\n--- FICHA EXCAVADORA ---")
        super().imprimir()
        print(f"Excavación máx: {self.profundidad_max} metros")

class Hormigonera(Construccion):
    def __init__(self, marca, modelo, combustible, potencia, capacidad_mezcla):
        super().__init__(marca, modelo, combustible, potencia)
        self.capacidad_mezcla = capacidad_mezcla

    def imprimir(self):
        print("\n--- FICHA HORMIGONERA ---")
        super().imprimir()
        print(f"Mezcla: {self.capacidad_mezcla} litros")

class Apisonadora(Construccion):
    def __init__(self, marca, modelo, combustible, potencia, ancho_rodillo):
        super().__init__(marca, modelo, combustible, potencia)
        self.ancho_rodillo = ancho_rodillo

    def imprimir(self):
        print("\n--- FICHA APISONADORA ---")
        super().imprimir()
        print(f"Ancho del rodillo: {self.ancho_rodillo} metros")

# --- Bloque Principal (Instancias con datos inventados) ---

# Vehículos de Transporte
bus = Autobus("Scania", "Citywide LF", "Biodiésel", 95, "Sí")
moto = Moto("Honda", "CBR500R", "Gasolina", 2, "A2")
coche = Coche("Tesla", "Model S", "Eléctrico", 5, 5)

# Vehículos de Construcción
excavadora = Excavadora("Caterpillar", "320 GC", "Diésel", 145, 6.7)
hormigonera = Hormigonera("Iveco", "Trakker 450", "Diésel", 450, 10000)
apisonadora = Apisonadora("Bomag", "BW 120 AD-5", "Diésel", 33, 1.2)

# Ejecución de los métodos imprimir
bus.imprimir()
moto.imprimir()
coche.imprimir()
excavadora.imprimir()
hormigonera.imprimir()
apisonadora.imprimir()