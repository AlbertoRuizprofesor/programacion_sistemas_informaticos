#Ingresar el sueldo de una persona, si supera los 3000 dolares mostrar un mensaje en pantalla indicando que debe abonar impuestos.

#Introducimos el sueldo de en la variable "sueldo"
sueldo = int(input("Ingrese su sueldo: "))

#Comprueba si el sueldo es mayor de 3000
#Si es mayor de 3000 tiene que pagar impuestos
if sueldo > 3000:
    print("Desgraciadamente tiene que pagar impuestos")
else:
    print("No tiene que pagar impuestos")