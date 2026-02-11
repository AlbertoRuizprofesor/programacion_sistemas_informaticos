#Confeccionar una aplicación que solicite la carga de dos valores enteros y muestre su suma
#Repetir la carga e impresion de la suma 5 veces.
#Mostrar una línea separadora después de cada vez que cargamos dos valores y su suma.
#Mostrar el promedio de esas 5 notas.

#Confeccionar una aplicación que solicite la carga de dos valores enteros y muestre su suma

def carga_suma():

    valor1=int(input("ingrese el primer valor: "))
    valor2=int(input("ingrese el segundo valor: "))
    suma=valor1+valor2

    print("la suma de los dos valores son" , suma)

def separación():
    print("*************************")

for b in range(5):
    carga_suma()
    separación()



