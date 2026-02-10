# Almacenar en una lista los sueldos (valores float) de 5 operarios. Imprimir la lista y el promedio de sueldos.
sueldos = []
suma = 0

for x in range(5):
    sueldo = float(input(f"Ingresa el {x+1}º sueldo: "))
    sueldos.append(sueldo)
    suma += sueldo

# Con foreach
# for sueldo in sueldos:
#    suma += sueldo

promedio = suma / 5

print(sueldos)
print(f"El promedio de los sueldos es {promedio:.2f}")