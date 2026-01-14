#Ejercicio con funcion def: añadir 5 notas y realizar la suma y la media:



def suma_valor(suma, contador):
    valor=int(input("Introduce una nota: "))
    contador=contador+1
    suma=suma+valor
    return suma, contador

suma=0
contador=0

def separacion():
    print("***********")

for i in range (5):
    suma, contador = suma_valor(suma, contador)
    separacion()
    
    
promedio=suma/5
print("El promedio de las notas es: ", promedio)