continuar = True

while continuar:
    print("\n--- CALCULADORA INTERACTIVA ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
    opcion = input("\nElige una opción (1-5): ")

    # Si la opción está entre 1 y 4, pedimos los números
    if opcion in ["1", "2", "3", "4"]:
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))

        if opcion == "1":
            print(f"Resultado: {n1} + {n2} = {n1 + n2}")
        elif opcion == "2":
            print(f"Resultado: {n1} - {n2} = {n1 - n2}")
        elif opcion == "3":
            print(f"Resultado: {n1} * {n2} = {n1 * n2}")
        elif opcion == "4":
            if n2 != 0:
                print(f"Resultado: {n1} / {n2} = {n1 / n2}")
            else:
                print("Error: No se puede dividir entre cero.")
    
    elif opcion == "5":
        print("Saliendo del programa... ¡Hasta pronto!")
        continuar = False
    
    else:
        print("Opción no válida. Inténtalo de nuevo.")