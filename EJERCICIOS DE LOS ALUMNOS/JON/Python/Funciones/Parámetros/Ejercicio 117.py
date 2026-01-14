print("Ejercicio 117")
print("")
print("")

def mayorque(v1,v2,v3):
    print("El mayor de los tres valores es: ")
    if v1 > v2 and v1 > v3:
        print(v1)
    elif v2 > v1 and v2 > v3:
        print(v2)
    else:
        print(v3)

def carga_valores():
    a=int(input("Ingrese el primer valor entero: "))
    b=int(input("Ingrese el segundo valor entero: "))
    c=int(input("Ingrese el tercer valor entero: "))    
    mayorque(a,b,c)


carga_valores()


print("Fin del programa")