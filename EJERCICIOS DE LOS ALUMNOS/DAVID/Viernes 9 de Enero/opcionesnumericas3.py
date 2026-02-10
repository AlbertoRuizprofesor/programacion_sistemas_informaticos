# --- FUNCIONES DE OPERACIÓN ---
def sumar(a, b): return a + b
def restar(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

# --- FUNCIÓN PRINCIPAL DEL MENÚ ---
def ejecutar_calculadora():
    continuar = True

    while continuar:
        print("\n--- CALCULADORA MODULAR ---")
        print("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "5":
            print("Cerrando calculadora...")
            continuar = False
            continue # Salta el resto del bucle

        if opcion in ["1", "2", "3", "4"]:
            try:
                # Pedimos datos solo si la opción es válida
                n1 = float(input("Primer número: "))
                n2 = float(input("Segundo número: "))

                if opcion == "1":
                    print(f"Resultado: {sumar(n1, n2)}")
                elif opcion == "2":
                    print(f"Resultado: {restar(n1, n2)}")
                elif opcion == "3":
                    print(f"Resultado: {multiplicar(n1, n2)}")
                elif opcion == "4":
                    print(f"Resultado: {dividir(n1, n2)}")
            
            except ValueError:
                print("Error: Por favor, ingresa solo números.")
        else:
            print("Opción no válida.")

# Iniciar el programa
if __name__ == "__main__":
    ejecutar_calculadora()