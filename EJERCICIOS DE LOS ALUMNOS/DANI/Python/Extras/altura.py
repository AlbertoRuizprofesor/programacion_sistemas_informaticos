class Persona:
    
    def __init__(self):
        self.nombre = input("Nombre: ")
        self.altura = float(input("Altura: "))

print("\nDatos de la persona 1")
persona1 = Persona()
print("\nDatos de la persona 2")
persona2 = Persona()

if persona1.altura > persona2.altura:
    print(f"La persona más alta es {persona1.nombre}")
elif persona1.altura < persona2.altura:
    print(f"La persona más alta es {persona2.nombre}")
else:
    print("Ambos miden igual")