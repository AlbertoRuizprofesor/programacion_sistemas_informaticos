#Desarrollar un programa que permita la carga de 10 valores por teclado y nos muestre posteriormente la suma de los valores ingresados y su promedio. 
#Este problema lo resolveremos empleando la estructura for para repetir la carga de los diez valores por teclado.

#Inicializamos la variable suma en 0 para empezar a acumular valores 
suma = 0

#Repetimos el proceso 10 veces. range(10) genera 0 a 9 que son 10 vueltas
for x in range(10):
    valor = int(input("Ingrese un valor: "))    #Pedimos al usuario que ingrese un número y lo convertimos a entero
    suma = suma + valor     #Sumamos el valor ingresado a la variable acumuladora "suma"

#Mostramos el total de la suma de los 10 valores ingresados
print(f"La suma es {suma}")

#Calculamos el promedio dividiendo la suma entre 10
promedio = suma / 10

#Mostramos el promedio
print(f"El promedio es {promedio}")

     