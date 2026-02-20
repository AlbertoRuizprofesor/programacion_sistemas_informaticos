"""
Confeccionar una función que reciba el nombre de un operario, el pago por hora y la cantidad de horas trabajadas. 
Debe mostrar su sueldo y el nombre. Hacer la llamada de la función mediante argumentos nombrados.
"""


def trabajador(nombre, pago_hora, horas_trabajadas):
    sueldo = pago_hora * horas_trabajadas
    print(f"{nombre} ha trabajado {horas_trabajadas} horas y cobra sueldo {sueldo} €")

#Bloque principal
trabajador("Juan", 12, 200)
trabajador(pago_hora = 12, horas_trabajadas = 80, nombre ="María")
trabajador(horas_trabajadas = 100, nombre = "Alberto", pago_hora = 7)
