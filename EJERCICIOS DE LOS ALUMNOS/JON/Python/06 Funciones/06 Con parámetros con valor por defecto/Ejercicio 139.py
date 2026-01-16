print("Ejercicio 139")
print("")
print("")

# Confeccionar una función que reciba entre 2 y 5 enteros. 
# La misma nos debe retornar la suma de dichos valores. 
# Debe tener tres parámetros por defecto.

def crearlista():
    lista=[]
    cantidad=int(input("¿Cuántos números desea ingresar (mínimo 2, máximo 5)? "))
    if cantidad<2:
        cantidad=2
    elif cantidad>5:
        cantidad=5
    for n in range(cantidad):
        numero=int(input(f"Ingrese el número {n+1}: "))
        lista.append(numero)
    return lista
    

def sumarlista(lista):
    suma=0
    for numero in lista:
        suma+=numero
    return suma

numeros=crearlista()
resultado=sumarlista(numeros)
print(f"La suma de los números ingresados es: {resultado}")


print("Fin del programa")

