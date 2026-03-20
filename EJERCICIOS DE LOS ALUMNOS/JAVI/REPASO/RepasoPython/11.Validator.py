def validar_password(password):
    errores = []

    if len(password) < 8:
        errores.append("Debe tener al menos 8 caracteres")
    if not any(c.isupper() for c in password):
        errores.append("Debe incluir una mayúscula")
    if not any(c.islower() for c in password):
        errores.append("Debe incluir una minúscula")
    if not any(c.isdigit() for c in password):
        errores.append("Debe incluir un dígito")
    if not any(not c.isalnum() for c in password):
        errores.append("Debe incluir un carácter especial")

    return len(errores) == 0, errores

es_valida, errores = validar_password("Clave123")
print(es_valida)
print(errores)
