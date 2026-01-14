#Ejercicio 123: Elaborar una función que reciba tres enteros y nos retorne el valor promedio de los mismos.

def valor_promedio(v1,v2,v3):
    promedio=(v1+v2+v3)//3
    return promedio


v1=int(input("Introduce un numeero: "))
v2=int(input("Introduce un numeero: "))
v3=int(input("Introduce un numeero: "))

print("El promedio de los tres numeros es",valor_promedio(v1,v2,v3)) 