#Definir una lista por asignación que almacene en la primer componente el nombre de un alumno y en las dos siguientes sus notas. 
# Imprimir luego el nombre y el promedio de las dos notas.

#Declaración de la lista alumno
alumno = ["Juan", 5, 7]

#Imprime los elementos con indice 0, 1, 2
print(f"Nombre: {alumno[0]}")
print(f"Nota1: {alumno[1]}")
print(f"Nota2: {alumno[2]}")

#Calcula el promedio de las notas usando los elementos de la lista
promedio = (alumno[1] + alumno[2]) / 2

#Imprime el promedio con dos decimales
print(f"El promedio de las dos notas es: {promedio:.2f}")


