# Nombre, Apellido, Tlf, Domicilio, CP, Ciudad y Provincia

class Persona:

    def inicializar(self,nom, apell, tlf, dom, cp, ciu, prov):
        self.nombre=nom
        self.appellido=apell
        self.telefono=tlf
        self.domicilo=dom
        self.codigopostal=cp
        self.ciudad=ciu
        self.provincia=prov

    def imprimir(self):
        print(f"Nombre y apellido: {self.nombre} {self.appellido}") 
        print(f"Teléfono: {self.telefono}")
        print(f"Domicilio: {self.domicilo}")
        print(f"Código postal: {self.codigopostal}")
        print(f"Ciudad y provincia: {self.ciudad}, {self.provincia}")
        print("------------------------")

# Bloque principal
persona1 = Persona()
persona1.inicializar("Darío", "Villena", "633104392", "Calle Debussy", "29011", "Málaga", "Malaga")
persona1.imprimir()

persona2 = Persona()
persona2.inicializar("Dío", "Villena", "687654321", "Calle Flor", "29011", "El Yermo", "Ingary")
persona2.imprimir()

persona3 = Persona()
persona3.inicializar("Nubia", "Montesinos", "664851885", "Plaza Ángeles", "29011", "Málaga", "Malaga")
persona3.imprimir()