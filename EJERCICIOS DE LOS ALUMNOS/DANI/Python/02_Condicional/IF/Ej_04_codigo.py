# Me pida por consola un codigo, si el codigo es correcto es decir "==", me aparezca por pantalla
# el mensaje "Codigo correcto, puede pasar", si es incorrecto "Codigo erroneo, alerta!!!!"

codigo = "kali"
acceso = input("Ingresa el código para entrar: ")

if codigo == acceso:
    print("Codigo correcto, puedes pasar")
else:
    print("Codigo erroneo, alerta!!!!")