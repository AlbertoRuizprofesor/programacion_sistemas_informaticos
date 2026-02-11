#Escribir un programa que solicite por teclado 10 notas de alumnos 
#y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.


#Contadores para las notas: uno para 7 o más y otro para menores de 7
mayor_igual7 = 0
menor7 = 0

#Repetimos el proceso 10 veces
for x in range(10):
    nota = int(input("Ingrese la nota: "))
    if nota >= 7:   #Si la nota es 7 o más, sumamos al contador correspondiente
        mayor_igual7 = mayor_igual7 +1
    else:           #Si la nota es menor que 7, sumamos al otro contador
        menor7 = menor7 + 1

#Mostramos cuántos alumnos tienen nota 7 o más
print("Alumnos con notas mayores o iguales a 7: ", mayor_igual7)

#Mostramos cuántos alumnos tienen nota menor que 7
print("Alumnos con notas menores a 7: ", menor7)

