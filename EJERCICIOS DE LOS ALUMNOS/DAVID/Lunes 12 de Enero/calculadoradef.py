def presentacion():
    print("*******************************")
    print("   CALCULADORA MULTIFUNCIÓN")
    print("*******************************")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

def calculadora():
    opcion = input("¿Qué operación desea realizar? (1/2/3/4): ")
    
    # Solo pedimos los valores si la opción es válida
    if opcion in ["1", "2", "3", "4"]:
        valor1 = int(input("Ingrese el primer valor: "))
        valor2 = int(input("Ingrese el segundo valor: "))
        
        if opcion == "1":
            resultado = valor1 + valor2
            print(f"La suma de {valor1} + {valor2} es: {resultado}")
        elif opcion == "2":
            resultado = valor1 - valor2
            print(f"La resta de {valor1} - {valor2} es: {resultado}")
        elif opcion == "3":
            resultado = valor1 * valor2
            print(f"La multiplicación de {valor1} * {valor2} es: {resultado}")
        elif opcion == "4":
            if valor2 != 0:
                resultado = valor1 / valor2
                print(f"La división de {valor1} / {valor2} es: {resultado}")
            else:
                print("Error: No se puede dividir entre cero.")
    else:
        print("Opción no válida. Por favor, elija un número del 1 al 4.")

def finalizacion():
    print("*******************************")
    print("Gracias por utilizar este programa")

# --- Bloque principal ---
presentacion()
calculadora()
finalizacion()