#Almacenar en una lista los sueldos (valores float) de 5 operarios. 
# Imprimir la lista y el promedio de sueldos.

#Declaración de lista vacía
sueldos = []

#Declaraciónd e iniciación de variable
suma = 0

#Introducción de datos, almacenamiento en la lista sueldos 
# y suma de todos los sueldos
for x in range(5):
    valor = float(input("Ingrese el sueldo del operario: "))
    sueldos.append(valor)
    suma = suma + valor

#Imprime los sueldos de los operarios, la lista de sueldos y
#promedio de los sueldos
print(f"Lista de sueldos: {sueldos}")
promedio = suma / 5
print(f"El promedio de los sueldos es: {promedio}")
    