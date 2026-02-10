#Desarrollar un programa que solicite la carga de 10 números e imprima la suma de los últimos 5 valores ingresados.

#Inicializamos la variable suma en 0 para acumular los valores
suma=0

#Repetimos el ingreso de los valores 10 veces (f va de 0 a 9)
for f in range(10):
    valor=int(input("Ingrese un valor:"))   #Pedimos un valor al usuario y lo convertimos a entero
    if f>4:     #Si f es mayor que 4, significa que estamos en las últimas 5 vueltas (5,6,7,8,9). Sumamos los valores ingresados en esas vueltas
        suma=suma+valor

#Mostramos el resultado de la suma de los últimos 5 valores ingresados
print("La suma de los últimos 5 valores es", suma)
