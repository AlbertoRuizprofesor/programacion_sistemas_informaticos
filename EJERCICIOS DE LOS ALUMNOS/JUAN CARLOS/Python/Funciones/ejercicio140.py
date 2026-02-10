"""
Confeccionar una función que reciba el nombre de un operario,
el pago por hora y la cantidad de horas trabajadas.
Debe mostrar su sueldo y el nombre. Hacer la llamada de la función mediante argumentos nombrados.
"""

#Funciones
def mensaje(mensaje):
    print(f"=== === === {mensaje} === === ===")

def calcularSueldo(nombre, pago_hora, horas):
    sueldo = pago_hora * horas
    print(f"Operario: {nombre}")
    print(f"Sueldo: ${sueldo:.2f}")


#Main
mensaje("Llamada con argumentos nombrados")
calcularSueldo(nombre="Juan Perez", pago_hora=25.5, horas=40)
mensaje("Otra llamada")
calcularSueldo(horas=35, pago_hora=30.0, nombre="Ana Gomez")
mensaje("Fin del programa")
