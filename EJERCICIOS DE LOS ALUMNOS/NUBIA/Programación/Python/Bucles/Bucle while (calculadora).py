# Hacer calculadora básica con un bucle while, sin usar funciones y evitar código espagueti.
# He buscado la manera de volver al inicio del bucle sin usar funciones, para ello, uso "continue"

option = True

while option:
    print("Seleccione la operación a realizar:")
    eleccion = int(input("1: Suma, 2: Resta, 3: Multiplicación, 4: División, 5: Salir\n")) #\n para salto de línea

    if 1 <= eleccion <= 4:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
    
        if eleccion == 1:
            operacion = "Suma"
            resultado = num1 + num2
        elif eleccion == 2:
            operacion = "Resta"
            resultado = num1 - num2
        elif eleccion == 3:
            operacion = "Multiplicación"
            resultado = num1 * num2
        elif eleccion == 4:
            operacion = "División"
            if num2 == 0:
                print("No se puede dividir por cero")
                continue
            resultado = num1 / num2
            
            
        print(f"La operación es: {operacion}. El total es: {resultado}")
    elif eleccion == 5:
        option = False
        print("Saliendo de la calculadora.")
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
        continue #vuelve al inicio del bucle
  