#Ejercicio 71: Definir una lista por asignación que almacene en la primer componente el nombre de un alumno y en las dos siguientes sus notas. Imprimir luego el nombre y el promedio de las dos notas.

lista=["Noemi", 9, 10]


print("Nombre del alumno:")
print(lista[0])
promedio=(lista[1]+lista[2])//2

print("Sus notas son: ")
print(lista[1], "y", lista[2])
print("El promedio de las notas es: ")
print(promedio)
