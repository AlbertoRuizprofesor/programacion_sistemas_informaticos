nombre1 = input("Ingrese el primer nombre: ")
nombre2 = input("Ingrese el segundo nombre: ")  

if nombre1 > nombre2:
    print(f"{nombre1} va después que {nombre2} en orden alfabético.")
elif nombre1 < nombre2:
    print(f"{nombre1} va antes que {nombre2} en orden alfabético.")