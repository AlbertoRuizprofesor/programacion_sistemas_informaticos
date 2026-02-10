print("Ejercicio 121")
print("")
print("")

def numayor (v1,v2):
    if v1>v2:
        mayor=v1
    else:
        mayor=v2
    return mayor

n1=int(input("Introduce el primer valor: "))
n2=int(input("Introduce el segundo valor: "))
print("El número más alto es: ",numayor(n1,n2))

print("Fin del programa")


