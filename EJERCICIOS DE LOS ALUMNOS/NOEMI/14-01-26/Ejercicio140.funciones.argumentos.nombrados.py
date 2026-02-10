#Ejercicio 140: Confeccionar una función que reciba el nombre de un operario, el pago por hora y la cantidad de horas trabajadas. Debe mostrar su sueldo y el nombre. Hacer la llamada de la función mediante argumentos nombrados.

def calcular_sueldo(nombre,costohoras,cantidadhoras):
    sueldo=costohoras*cantidadhoras
    print(nombre,"trabaja",cantidadhoras,"horas y cobra un sueldo de",sueldo)
    
calcular_sueldo("Juan",10,120)
calcular_sueldo(costohoras=12,cantidadhoras=40,nombre="Noemi")
calcular_sueldo(cantidadhoras=90,nombre="Jose",costohoras=12)    
