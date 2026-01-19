from persona import Persona

personas = []

for x in range(2):
    nombre = input(f"Dame el nombre de la persona {x+1}: ")
    edad = int(input("Dame la edad: "))
    personas.append(Persona(nombre, edad))

for persona in personas:
    persona.mostrar()
    persona.mayor()
    print("--------------")
