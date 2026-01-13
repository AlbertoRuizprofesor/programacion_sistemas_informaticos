"""
Almacenar en una lista los sueldos (valores float) de 5 operarios. 
Imprimir la lista y el promedio de sueldos.
"""

sueldos = []
suma = 0


for x in range(5):
    valor = float(input("Introduce el sueldo: "))
    sueldos.append(valor)
    suma = suma + valor
    

print("Sueldos: ")
print(sueldos)

media = suma /5

print("Media de los sueldos: ")
print(media)
