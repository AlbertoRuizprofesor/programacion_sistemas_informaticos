import sys

# 1. Definimos las operaciones como funciones independientes
def sumar(a, b): return a + b
def restar(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b): return a / b if b != 0 else "Error: División por cero"

# 2. Diccionario de configuración (Aquí es donde el código escala)
# Estructura: "opcion": (nombre_visible, funcion_a_ejecutar)
OPERACIONES = {
    "1": ("Sumar", sumar),
    "2": ("Restar", restar),
    "3": ("Multiplicar", multiplicar),
    "4": ("Dividir", dividir),
}

def mostrar_menu():
    print("\n--- CALCULADORA ESCALABLE ---")
    for tecla, (nombre, _) in OPERACIONES.items():
        print(f"{tecla}. {nombre}")
    print(f"{len(OPERACIONES) + 1}. Salir")

def ejecutar_calculadora():
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción: ")

        # Opción de salida dinámica
        if opcion == str(len(OPERACIONES) + 1):
            print("Saliendo...")
            break

        if opcion in OPERACIONES:
            try:
                n1 = float(input("Primer número: "))
                n2 = float(input("Segundo número: "))
                
                # Buscamos la función en el diccionario y la ejecutamos
                nombre, funcion = OPERACIONES[opcion]
                resultado = funcion(n1, n2)
                
                print(f"\n>> Resultado de {nombre}: {resultado}")
            except ValueError:
                print("\n[!] Error: Ingresa solo números válidos.")
        else:
            print("\n[!] Opción no reconocida.")

if __name__ == "__main__":
    ejecutar_calculadora()