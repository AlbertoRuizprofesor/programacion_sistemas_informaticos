"""
Confeccionar una función que reciba el nombre de un operario, 
el pago por hora y la cantidad de horas trabajadas. 
Debe mostrar su sueldo y el nombre. 
Hacer la llamada de la función mediante argumentos nombrados.
"""

def cargar_datos(nombre, pago, horas):
    sueldo = pago * horas
    print(nombre , " tiene un sueldo de: " , sueldo)

cargar_datos("Pepe", 15, 80)
cargar_datos(horas=20, pago=10, nombre="Carmen")
cargar_datos(pago=30, horas=80, nombre="Carlos")



