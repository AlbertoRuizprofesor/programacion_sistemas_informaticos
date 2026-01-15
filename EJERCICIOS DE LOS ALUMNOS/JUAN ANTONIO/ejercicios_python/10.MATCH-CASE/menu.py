#El usuario debe escribir el número de la opción que quiere hacer. 
# El programa mostrará un mensaje distinto según la opción elegida, usando match-case.



#Muestra el título del menú
print("Menú")
print("=====")

#Mostramos las opciones disponibles para el usuario
print("1. Saludar")
print("2. Decir la hora")
print("3. Salir")

#Pedimos al usuario que elija una opción del menú 
#El valor se guarda como cadena porque lo comparamos con textos en el match
opcion  = input("Elige una opción del menú anterior: 1, 2, ó 3: ")

#Estructura match-case para evaluar la opción seleccionada 
#match permite comparar el valor de 'opcion' con distintos casos
match opcion:
    case "1":   #Si elige 1, mostramos un saludo
        print("¡Hola! ¿Cómo estás?")
    case "2":   # Si elige 2, mostramos un mensaje simulando la hora
        print("Son las y pico......")
    case "3":   #Si elige 3, mostramos un mensaje de salida
        print("Me voy, hasta mañana")
    case _: #Si introduce cualquier otro valor, avisamos del error
        print("Ha introducido un dato incorrecto")