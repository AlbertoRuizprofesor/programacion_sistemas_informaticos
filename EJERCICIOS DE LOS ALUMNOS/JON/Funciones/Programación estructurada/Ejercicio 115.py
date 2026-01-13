print("Ejercicio 115")
print("")
print("")

def menor_de_tres():
    a=int(input("Ingrese el primer valor entero: "))
    b=int(input("Ingrese el segundo valor entero: "))
    c=int(input("Ingrese el tercer valor entero: "))

    if a <= b and a <= c:
        print("El menor de los tres valores es: ", a)
        return a
    elif b <= a and b <= c:
        print("El menor de los tres valores es: ", b)
        return b
    else:
        print("El menor de los tres valores es: ", c)
        return c
    
menor_de_tres()
menor_de_tres()

print("Fin del programa")   
