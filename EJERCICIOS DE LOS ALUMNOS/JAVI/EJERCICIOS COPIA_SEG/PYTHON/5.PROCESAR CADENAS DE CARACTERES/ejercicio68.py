#Solicitar el ingreso de una clave por teclado y almacenarla en una cadena de caracteres. 
# Controlar que el string ingresado tenga entre 10 y 20 caracteres para que sea válido, 
# en caso contrario mostrar un mensaje de error.

#Pide al usuario que escriba una clave y la guarda en la variable "clave"
clave = input("Ingrese una clave que tenga entre 10 y 30 caracteres: ")

#Calcula cuántos caracteres tiene la clave
caracteres = len(clave)

#Comprueba si la clave tien más de 10 y menos de 30 caracteres: clave válida
#Si tiene menos de 10 o más de 30: clave no válida
if caracteres > 10 and caracteres < 30:
    print(f"La clave \"{clave}\" es válida")
else:
    print(f"La clave \"{clave}\" no es válida")