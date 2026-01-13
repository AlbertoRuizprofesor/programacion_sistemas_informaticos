#BOOLEANO TRUE O FALSE. OPCION TRUE.

opcion=True

while opcion:
    print("1:sumar, 2:restar, 3:salir")
    eleccion=int(input("Elige una opcion: "))
    if eleccion ==1:
        print("Has elegido sumar")
    elif eleccion==2:
        print("Has elegido multiplicar")
    elif eleccion==3:
        print("salien")
        opcion=False
    else:
        print("Opción no válida")
        