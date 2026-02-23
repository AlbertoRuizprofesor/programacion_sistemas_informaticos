#Crea un programa que pregunte al usuario qué día de la semana es, indicando un número del 1 al 7. 
# Luego debe mostrar el nombre del día correspondiente


#Mostramos el título del programa
print("Días de la Semana")

#Indicamos al usuario qué debe hacer
print("Elige un número del un al siete")

#Pedimos al usuario que introduzca un número 
#Lo guardamos como cadena porque lo compararemos con textos en el match
dia = input("Número: ")

#Utilizamos la estructura match-case para identificar qué día corresponde
#1:Lunes, 2:Martes, 3: Miércoles etc...
match dia:
    case "1":
        print("Has elegido el Lunes")
    case "2":
        print("Has elegido el Martes")
    case "3":
        print("Has elegido el Miércoles")
    case "4":
        print("Has elegido el Jueves")
    case "5":
        print("Has elegido el Viernes")
    case "6":
        print("Has elegido el Sábado")
    case "7":
        print("Has elegido el Domingo")
    case _: # Si introduce cualquier otro valor, mostramos un mensaje de error
        print("Has introducido un dato incorrecto")

    
