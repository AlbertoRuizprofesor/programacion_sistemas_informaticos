"""
Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.
"""
x = 0 #Contador para saber cuántas notas llevamos
mayor_igual7 = 0    #Contador de alumnos con nota >= 7
menor7 = 0      #Contador de alumnos con nota < 7


while x < 10:      #Repetimos 10 veces (10 alumnos)
    notas = int(input("Introduzca la nota del alumno: "))   #Pedimos la nota

    if notas >= 7:  #Si la nota es 7 o más...
        mayor_igual7 = mayor_igual7 + 1 #...sumamos al grupo de mayores o igual a 7
    else:       #Si es menor
        menor7 = menor7 + 1     #...Sumamos al grupo de meneres de 7

    x += 1      #Avanzamos el contador para acercarnos al final del bucle


#Imprimimos los resultados 
print(f"El número de alumnos con notas mayores o iguales a 7 son: {mayor_igual7}")
print(f"El número de alumnos con notas menores son: {menor7}")


