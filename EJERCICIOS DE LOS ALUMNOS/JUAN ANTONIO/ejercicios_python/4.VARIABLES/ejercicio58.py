#Realizar la carga por teclado del nombre, edad y altura de dos personas. 
# Mostrar por pantalla el nombre de la persona con mayor altura.

#Ingreso de datod de la primera persona
print("Datos de la primera persona")
nombre1 = input("Introduzca el nombre: ")
edad1 = int(input("Introduzca la edad: "))
altura1 = float(input("Introduzca la altura Ej: 1.75: "))

#Ingreso de datos de la segunda persona
print("Datos de la segunda persona: ")
nombre2 = input("Introduzca el nombre: ")
edad2 = int(input("Introduzca la edad: "))
altura2 = float(input("Introduzca la altura Ej: 1.75: "))


#Determina la persona de mayor altura e imprime su nombre
if altura1 > altura2:
    print(f"La persona de mayor altura es {nombre1}")
else:
    print(f"La persona de mayor altura es {nombre2}")