#Confeccionar una función que reciba una serie de edades y me retorne la cantidad 
#que son mayores o iguales a 18 (como mínimo se envía un entero a la función)

# -----------------------------------------
# Función: contar_mayores
# Recibe al menos una edad obligatoria (edad_principal)
# y luego cualquier cantidad de edades adicionales
# gracias a *otras_edades.
# Devuelve cuántas de todas esas edades son >= 18.
# -----------------------------------------

def contar_mayores(edad_principal, *otras_edades):
    cantidad = 0

    # Verifica la primera edad obligatoria
    if edad_principal >= 18:
        cantidad += 1

    # Recorre las edades adicionales
    for edad in otras_edades:
        if edad >= 18:
            cantidad += 1

    return cantidad


# -----------------------------------------
# Bloque principal del programa
# -----------------------------------------

print(
    "La cantidad de personas mayores a 18 son:",
    contar_mayores(23, 6, 8, 19, 24)
)
