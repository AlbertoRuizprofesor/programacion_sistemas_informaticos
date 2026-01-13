"""
Se cuenta con la siguiente información:Las edades de 5 estudiantes del turno mañana.
Las edades de 6 estudiantes del turno tarde.Las edades de 11 estudiantes del turno noche.
Las edades de cada estudiante deben ingresarse por teclado.
a) Obtener el promedio de las edades de cada turno (tres promedios)
b) Imprimir dichos promedios (promedio de cada turno)
c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un promedio de edades mayor.
"""

cont1 = 0
cont2 = 0
cont3 = 0

for x in range(5):
    edad1 = int(input("Introduce las edades de los estudiantes por la mañana: "))
    cont1 = cont1 + edad1
media1=cont1/5

print("Promedio de edades del turno de mañana:")
print(cont1)


for x in range(6):
    edad2 = int(input("Introduce las edades de los estudiantes por la tarde: "))
    cont2 = cont2 + edad2
media2=cont1/6

print("Promedio de edades del turno de tarde:")
print(cont2)


for x in range(11):
    edad3 = int(input("Introduce las edades de los estudiantes por la noche: "))
    cont3 = cont3 + edad3
media3=cont1/11

print("Promedio de edades del turno de noche: ")
print(cont3)







