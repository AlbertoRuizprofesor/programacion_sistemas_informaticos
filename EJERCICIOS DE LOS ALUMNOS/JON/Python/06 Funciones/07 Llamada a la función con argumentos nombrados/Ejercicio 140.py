print("Ejercicio 140")
print("")
print("")

# Confeccionar una función que reciba el nombre de un operario, 
# el pago por hora y la cantidad de horas trabajadas.
# Debe mostrar su sueldo y el nombre. 
# Hacer la llamada de la función mediante argumentos nombrados.

def calcular_sueldo(nombre, pago_por_hora, horas_trabajadas):
    sueldo = pago_por_hora * horas_trabajadas
    print(f"Operario: {nombre}, trabajó {horas_trabajadas} horas y cobrará: {sueldo:.2f} €")

calcular_sueldo(nombre="Juan Pérez", pago_por_hora=15.50, horas_trabajadas=160)
calcular_sueldo(horas_trabajadas=120, nombre="Ana Gómez", pago_por_hora=20.00)
calcular_sueldo(pago_por_hora=18.75, nombre="Luis Martínez", horas_trabajadas=140)

print("Fin del programa")


