print("Ejercicio 122")
print("")
print("")

def longitud(cadena):
    return len(cadena)

# Programa principal

n1=input("Introduce el primer nombre: ")
n2=input("Introduce el segundo nombre: ")

l1=longitud(n1)
l2=longitud(n2)

if l1==l2:
    print("Los nombres: ",n1,n2, " Tienen la misma cantidad de caractéres.")
elif l1<l2:
    print(n2," Es más largo.")
else:
    print(n1," Es más largo.")
    
print("Fin del programa")
