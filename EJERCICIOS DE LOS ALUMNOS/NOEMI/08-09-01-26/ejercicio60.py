#Ejercicio 60: Realizar la carga de enteros por teclado. 


suma=0
continuar="si"

while continuar=="si":
    valor=int(input("Ingrese un valor: "))
    suma +=valor
    
    continuar=input("¿Desea ingresar otro valor (si/no)?: ")
    
print("La suma de los valores ingresados es: ",suma)

    
    
