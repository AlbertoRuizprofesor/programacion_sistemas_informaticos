class Persona:
    # Se usa __init__ para que los datos se carguen al crear el objeto
    def __init__(self, nom, ape, dom, loc, cp, tel):
        self.nombre = nom
        self.apellido = ape
        self.domicilio = dom
        self.localidad = loc
        self.codigo_postal = cp
        self.telefono = tel

    def imprimir(self):
        print("--- Ficha de Persona ---")
        print(f"Nombre Completo: {self.nombre} {self.apellido}")
        print(f"Domicilio: {self.domicilio}")
        print(f"Localidad: {self.localidad} (CP: {self.codigo_postal})")
        print(f"Teléfono: {self.telefono}")
        print("-" * 25)


# Bloque principal

# Ahora pasamos los datos directamente entre los paréntesis
persona1 = Persona("Pedro", "García", "Av. Siempre Viva 123", "Madrid", "28001", "600111222")
persona1.imprimir()

persona2 = Persona("Carla", "Méndez", "Calle Mayor 5", "Cádiz", "11001", "611333444")
persona2.imprimir()

persona3 = Persona("Joaquín", "Pérez", "Mangas Verdes", "Málaga", "29012", "622555666")
persona3.imprimir()