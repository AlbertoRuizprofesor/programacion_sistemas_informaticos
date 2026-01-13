# Carga de datos por teclado
nombre1 = input("Introduce el primer nombre: ")
nombre2 = input("Introduce el segundo nombre: ")

# Lógica de comparación alfabética
if nombre1.lower() > nombre2.lower():
    print(f"\nEl nombre '{nombre1}' es mayor alfabéticamente que '{nombre2}'")
elif nombre2.lower() > nombre1.lower():
    print(f"\nEl nombre '{nombre2}' es mayor alfabéticamente que '{nombre1}'")
else:
    print("\nAmbos nombres son iguales")