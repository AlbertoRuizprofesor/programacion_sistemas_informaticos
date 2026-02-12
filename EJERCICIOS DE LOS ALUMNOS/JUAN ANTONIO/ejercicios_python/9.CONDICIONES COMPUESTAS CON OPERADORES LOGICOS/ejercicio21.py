#Realizar un programa que pida cargar una fecha cualquiera, 
# luego verificar si dicha fecha corresponde a Navidad.



# Pedimos al usuario que introduzca el día, el mes y el año
dia = int(input("Ingrese el número de día: "))
mes = int(input("Ingrese el número de mes: "))
año = int(input("Ingrese el número de año: "))

#Comprueba que la fecha es 25 del 12
if mes == 12 and dia == 25: # Si el mes es 12 y el día es 25, entonces es Navidad
    print(f"La fecha ingresada es: {dia} del {mes} de {año}")
    print("ES NAVIDAD!")
else:   # Si no coincide con el 25/12, no es Navidad
    print(f"La fecha ingresada es: {dia} del {mes} de {año}")
    print("NO ES NAVIDAD!")