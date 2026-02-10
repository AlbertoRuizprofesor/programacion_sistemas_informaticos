continuar = True

while continuar:
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Salir")
    
    opcion = input("\nElige una opción (1-3): ")

    if opcion == "1":
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        print(f"Resultado de la suma: {num1 + num2}")
    
    elif opcion == "2":
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        print(f"Resultado de la resta: {num1 - num2}")
    
    elif opcion == "3":
        print("Saliendo del programa... ¡Adiós!")
        continuar = False  # Cambiamos la condición para romper el bucle
    
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")