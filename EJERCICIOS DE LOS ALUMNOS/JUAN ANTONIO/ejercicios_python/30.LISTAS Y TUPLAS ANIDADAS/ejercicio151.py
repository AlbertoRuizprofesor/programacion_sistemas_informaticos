

# Creamos una lista llamada 'empleado' con:
# - un nombre (cadena)
# - una edad (entero)
# - una fecha de nacimiento (tupla)
empleado = ["juan", 53, (25, 11, 1999)]

# Mostramos la lista completa
print(empleado)

# Agregamos una nueva tupla al final de la lista.
# Las listas son MUTABLES, así que se pueden modificar.
empleado.append((1, 1, 2016))

# Mostramos la lista ya modificada
print(empleado)


# Creamos una tupla llamada 'alumno' con:
# - un nombre (cadena)
# - una lista de notas (lista)
alumno = ("pedro", [7, 9])

# Mostramos la tupla
print(alumno)

# Aunque 'alumno' es una tupla (INMUTABLE),
# su segundo elemento es una LISTA, y las listas sí se pueden modificar.
# Por eso podemos agregar una nueva nota sin problema.
alumno[1].append(10)

# Mostramos la tupla con la lista interna ya modificada
print(alumno)
