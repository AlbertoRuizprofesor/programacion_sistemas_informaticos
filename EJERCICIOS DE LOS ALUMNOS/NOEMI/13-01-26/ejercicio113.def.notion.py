#Ejercicio 113: Confeccionar una aplicación que solicite la carga de dos valores enteros y muestre su suma.
#Repetir la carga e impresion de la suma 5 veces.
#Mostrar una línea separadora después de cada vez que cargamos dos valores y su suma.


def suma_valor():
    valor1=int(input("Introduce el primer valor: "))
    valor2=int(input("Introduce el segundo valor: "))
    suma=valor1+valor2
    print("La suma de los valores es: ", suma)
    
def separacion():
    print("************************")
    
for i in range(5):
    suma_valor()
    separacion()

    

