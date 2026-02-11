def mostrar_perimetro(lado):
    per = lado * 4
    print("El perimetro es", per)

def mostrar_superficie(lado):
    sup = lado * lado
    print("La superficie es", sup)

def cargar_dato():
    la = int(input("Ingrese el valor del lado de un cuadrado: "))
    # Convertimos a minúsculas para evitar errores de mayúsculas/minúsculas
    respuesta = input("¿Quiere calcular el perimetro o la superficie? (perimetro/superficie): ").lower()
    
    if respuesta == "perimetro":
        mostrar_perimetro(la)
    elif respuesta == "superficie":
        mostrar_superficie(la)
    else:
        print("Opción no válida.")

# programa principal
cargar_dato()