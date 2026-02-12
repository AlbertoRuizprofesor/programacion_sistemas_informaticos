# Definir una lista por asignación que almacene en la primer componente el nombre de un alumno y en las dos siguientes sus notas. 
# Imprimir luego el nombre y el promedio de las dos notas.

# Lista por asigniacion y variable
alumno = ["Pedro", 5, 10]
promedio=(alumno[1]+alumno[2])/2

# Opción 1
print(f"El alumno {alumno[0]}, tiene un promedio de {promedio}")
# Opción 2
print(f"El alumno {alumno[0]}, tiene un promedio de {(alumno[1]+alumno[2])/2}")