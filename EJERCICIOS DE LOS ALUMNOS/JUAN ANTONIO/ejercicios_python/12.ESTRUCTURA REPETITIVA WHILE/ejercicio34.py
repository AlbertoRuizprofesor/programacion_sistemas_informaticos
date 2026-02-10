"""
En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, 
realizar un programa que lea los sueldos que cobra cada empleado e 
informe cuántos empleados cobran entre $100 y $300 y 
cuántos cobran más de $300. 
Además el programa deberá informar el importe que gasta la empresa en sueldos al personal.

"""

n = int(input("Introduzca el número de empleaos de la empresa: "))  #Pide el número de empleados de la empresa

x = 1                   #Contador para saber cuántos empleados llevamos procesados
contador_100_300 = 0    #Empleados con sueldo entre 100 y 300
contador_mas_300 = 0    #Empleados con sueldo mayor de 300
gastos = 0              #Acumulador para sumar todos los sueldos

while x <= n:           #Repetimos el proceso "n" veces (numeros de empleados)
    sueldo = float(input("Ingrese el sueldo del empleado: "))       #Pedimos el sueldo 
    if sueldo <= 300:           #Si el sueldo es 300 o menos...
        contador_100_300 += 1   #...sumamos al grupo de 100-300
    else:                       #Si es mayor de 300...
        contador_mas_300 += 1   #...sumamos al grupo de +300
    gastos = gastos + sueldo    #Sumamos el sueldo introducido al total de gastos
    x += 1                      #Avanzamos al siguiente empleado

#Cuando termina el bucle, mostramos los resultados
print(f"El número de empleados que cobran entre $100 y $300 es: {contador_100_300}")
print(f"El número de empleados que cobran más de $300 es: {contador_mas_300}")
        