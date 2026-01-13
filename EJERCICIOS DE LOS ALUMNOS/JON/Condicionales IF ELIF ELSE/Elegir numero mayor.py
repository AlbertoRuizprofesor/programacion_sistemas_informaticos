print("Ejercicio elegir numero mayor")
print("")
print("")

n1=int(input("Introduzca el primer número: "))
n2=int(input("Introduzca el segundo número: "))
n3=int(input("Introduzca el tercer número: "))

if n1>n2>n3 or n1>n3>n2:
    print("El número mayor es:", n1)
if n2>n1>n3 or n2>n3>n1:
    print("El número mayor es: ", n2)
if n3>n1>n2 or n3>n2>n1:
    print("El número mayor es: ", n3)
    
    
    
    
