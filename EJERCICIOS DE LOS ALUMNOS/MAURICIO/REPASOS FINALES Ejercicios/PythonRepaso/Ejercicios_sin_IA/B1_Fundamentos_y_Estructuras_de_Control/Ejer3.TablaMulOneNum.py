# Ejercicio 3. Tabla de multiplicar interactiva
# Pide un número entero y muestra su tabla de multiplicar del 1 al 10 usando un bucle.
# Ampliación: Amplía el ejercicio para que el usuario pueda pedir varias tablas hasta escribir "salir".
# Ejercicio 3. Tabla de multiplicar interactiva

while True:
    opcion = input("\n¿De qué número quieres la tabla? (o escribe 'salir'): ").lower()

    if opcion == "salir":
        print("¡Hasta luego!")
        break

    # Verificamos si la entrada es un número
    if opcion.isdigit():
        numero = int(opcion)

        # Validamos que esté en el rango del 1 al 10 (opcional)
        if 1 <= numero <= 10:
            print(f"\n--- TABLA DEL {numero} ---")
            for i in range(1, 11):
                print(f"{numero} x {i} = {numero * i}")
        else:
            print("Por favor, introduce un número entre 1 y 10.")
    else:
        print("Entrada no válida. Introduce un número o escribe 'salir'.")
