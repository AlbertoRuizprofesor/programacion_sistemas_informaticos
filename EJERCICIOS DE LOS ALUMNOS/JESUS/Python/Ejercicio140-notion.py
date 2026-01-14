# Confeccionar una función que reciba el nombre de un operario, el pago por hora y la cantidad de horas trabajadas. 
# Debe mostrar su sueldo y el nombre. 
# Hacer la llamada de la función mediante argumentos nombrados.

def calc_sueldo(nombre,costehora,cantihoras):
    sueldo=costehora*cantihoras
    print(nombre,"trabajó",cantihoras,"y cobra un sueldo de",sueldo)


#bloque principal del programa 
calc_sueldo("Juan",20,200)
calc_sueldo(costehora=16,cantihoras=180,nombre="Pepe")