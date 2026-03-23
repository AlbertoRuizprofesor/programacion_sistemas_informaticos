#Crea una función que reciba una contraseña y verifique si cumple estas reglas: al menos 8 caracteres,
#una mayúscula, una minúscula, un dígito y un carácter especial.

def validar_password (pasword):
    errores = []

    if len(pasword) < 8:
        errores.append("Debe tener al menos 8 caracteres")
    if not any(c.isupper() for c in password):
        errores.append("Debe incluir una mayuscula")
    if not any (c.islower() for c in password):
        errores.append("Debe incluir una minuscula")
    if not any (c.isdigit() for c in password):
        errores.append("Debe incluir un dígito")
    if not any(not c.isalnum() for c in password):
        errores.append("Debe incluir un carácter especial")
        return len(errores) == 0, errores
    es_valida, errores = validar_password("Clave123")
    print(es_valida)
    print(errores)
