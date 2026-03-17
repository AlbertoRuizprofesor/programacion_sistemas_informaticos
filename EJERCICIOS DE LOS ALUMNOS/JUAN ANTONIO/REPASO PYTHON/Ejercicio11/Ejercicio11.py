# Ejercicio 11. Validador de contraseñas

def comprobar_clave(clave):
    fallos = []

    if len(clave) < 8:
        fallos.append("Debe tener al menos 8 caracteres")
    if not any(x.isupper() for x in clave):
        fallos.append("Debe incluir una mayúscula")
    if not any(x.islower() for x in clave):
        fallos.append("Debe incluir una minúscula")
    if not any(x.isdigit() for x in clave):
        fallos.append("Debe incluir un dígito")
    if not any(not x.isalnum() for x in clave):
        fallos.append("Debe incluir un carácter especial")

    return len(fallos) == 0, fallos


es_segura, lista_fallos = comprobar_clave("Clave123")
print(es_segura)
print(lista_fallos)
