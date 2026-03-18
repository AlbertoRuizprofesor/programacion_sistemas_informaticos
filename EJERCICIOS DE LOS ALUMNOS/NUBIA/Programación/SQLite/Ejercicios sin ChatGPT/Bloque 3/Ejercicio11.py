'''
Crea una función que reciba una contraseña y verifique si cumple estas reglas: 
al menos 8 caracteres, una mayúscula, una minúscula, un dígito y un carácter especial. 
Idea clave: Devuelve también una lista con los errores encontrados. 
'''

def validarContraseña():
    
    while True:
        contraseña = input("Ingrese la contraseña: ")
        errores = []

        if len(contraseña) < 8:
            errores.append("La contraseña debe tener al menos 8 caracteres.")
            
        if not any(c.isupper() for c in contraseña):
            errores.append("La contraseña debe contener al menos una letra mayúscula.")
            
        if not any(c.islower() for c in contraseña):
            errores.append("La contraseña debe contener al menos una letra minúscula.")
            
        if not any(c.isdigit() for c in contraseña):
            errores.append("La contraseña debe contener al menos un dígito.")
            
        if not any(not c.isalnum() for c in contraseña): 
            errores.append("Debe incluir un carácter especial")

        if errores:
            print("Contraseña no válida. Errores encontrados:")
            for error in errores:
                print("- " + error)
        else:
            print("Contraseña válida.")
            break
        
validarContraseña()