"""Crear una estructura de Calses con Vehiculos. """
#Clase Padre
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def print_vehiculo(self):
        print(f"Marca: {self.marca}, modelo: {self.modelo}")
#Clases hijas 1er nivel
class Trasporte(Vehiculo):
    def __init__(self, marca, modelo, n_ruedas, n_plazas, combustible):
        super().__init__(marca, modelo)
        self.n_ruedas = n_ruedas
        self.n_plazas = n_plazas
        self.combustible = combustible
    def print_vehiculo(self):
        super().print_vehiculo()
        print(f"Número de Ruedas: {self.n_ruedas}. Número plazas: {self.n_plazas}. Combustible: {self.combustible}")
class Construccion(Vehiculo):
    def __init__(self, marca, modelo, tipo_licencia):
        super().__init__(marca, modelo)
        self.tipo_liencia = tipo_licencia
    def print_vehiculo(self):
        super().print_vehiculo()
        print(f"Tipo de licencia necesaria: {self.tipo_liencia}")
#Clases hijas 2º Nivel
class Camion(Trasporte):
    def __init__(self, marca, modelo, n_ruedas, n_plazas, combustible, tara, pma):
        super().__init__(marca, modelo, n_ruedas, n_plazas, combustible)
        self.tara = tara
        self.pma = pma
    def print_vehiculo(self):
        super().print_vehiculo()
        print(f"T.A.R.A.: {self.tara}Kg. P.M.A.: {self.pma}Kg")
class Coche(Trasporte):
    def __init__(self, marca, modelo, n_ruedas, n_plazas, combustible, silla_bebe, taxi):
        super().__init__(marca, modelo, n_ruedas, n_plazas, combustible)
        self.silla_bebe = silla_bebe
        self.taxi = taxi
    def print_vehiculo(self):
        super().print_vehiculo()
        print(f"Silla Bebe: {self.silla_bebe}. Taxi: {self.taxi}")
class Moto(Trasporte):
    def __init__(self, marca, modelo, n_ruedas, n_plazas, combustible, porta_cascos, ind_marcha):
        super().__init__(marca, modelo, n_ruedas, n_plazas, combustible)
        self.porta_cascos = porta_cascos
        self.ind_marcha = ind_marcha
    def print_vehiculo(self):
        super().print_vehiculo()
        print(f"Porta Cascaos {self.porta_cascos}. Indicador Marcha {self.ind_marcha}")
class Apisonadora(Construccion):
    def __init__(self, marca, modelo, tipo_licencia, presion_eje, n_piston ):
        super().__init__(marca, modelo, tipo_licencia)
        self.presion_eje = presion_eje
        self.n_piston = n_piston
    def print_vehiculo(self):
        super().print_vehiculo()
        print(f"Presion Eje: {self.presion_eje}cm/2. Numero Pistones {self.n_piston}")
class Escavadora(Construccion):
    def __init__(self, marca, modelo, tipo_licencia, capacidad_pala, altura_pala ):
        super().__init__(marca, modelo, tipo_licencia)
        self.capacidad_pala = capacidad_pala
        self.altura_pala = altura_pala
    def print_vehiculo(self):
        super().print_vehiculo()
        print(f"Capacidad Pala: {self.capacidad_pala}m/3. Altura Pala {self.altura_pala}m")
class Hormigonera(Construccion):
    def __init__(self, marca, modelo, tipo_licencia, capacidad_cuba, n_rotacion):
        super().__init__(marca, modelo, tipo_licencia)
        self.capacidad_cuba = capacidad_cuba
        self.n_rotacion = n_rotacion
    def print_vehiculo(self):
        super().print_vehiculo()
        print(f"Capacidad Cuba: {self.capacidad_cuba}m/3. Velocidad Rotacion {self.n_rotacion}m")
#Main
#Prueba Clase Padre
print("****************** Clase Padre ********************")
vehiculo1 = Vehiculo("Mini", "Cooper")
vehiculo1.print_vehiculo()
print("***************************************************")
print("************** Clase Hija 1er Nivel ***************")
#Puebas Clases hijas 1er nivel
transporte1 = Trasporte("Mercedes", "A220", 4, 5, "Diesel")
transporte1.print_vehiculo()
print("                      ----------                   ")
contruccion1 = Construccion("Caterpillar", "CLipper 120", "E2")
contruccion1.print_vehiculo()
print("***************************************************")
print("************* Clase Hija 2ndo Nivel ***************")
#Pruebas Clases hijas 2ndo nivel
camion1 = Camion("Volvo", "Igneus", 10, 2, "Diesel", 2500, 1500)
camion1.print_vehiculo()
print("                      ----------                   ")
coche1 = Coche("Lexus", "LBX", 4, 4,"BioMetanol", "SI", "NO")
coche1.print_vehiculo()
print("                      ----------                   ")
moto1 = Moto("BMW", "R1200R", 2, 2,"Gasolina 98", "SI", "SI")
moto1.print_vehiculo()
print("                      ----------                   ")
apisonadora1 = Apisonadora("Caterpillar", "Corsair", "EX1", 2000, 8)
apisonadora1.print_vehiculo()
print("                      ----------                   ")
escavadora1 = Escavadora("Caterpillar", "Cutlass", "EX2", 500, 10)
escavadora1.print_vehiculo()
print("                      ----------                   ")
hormigonera1 = Hormigonera("Caterpillar", "Bucanner", "EX3", 1400, 4)
hormigonera1.print_vehiculo()
print("***************************************************")