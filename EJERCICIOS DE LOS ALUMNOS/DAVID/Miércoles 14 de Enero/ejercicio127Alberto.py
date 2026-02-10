def obtener_edades(cantidad=5):
    """Solicita al usuario una lista de edades con validación básica."""
    edades = []
    print(f"Introduce {cantidad} edades:")
    while len(edades) < cantidad:
        try:
            edad = int(input(f"Edad {len(edades) + 1}: "))
            if edad < 0:
                print("La edad no puede ser negativa.")
                continue
            edades.append(edad)
        except ValueError:
            print("Por favor, introduce un número entero válido.")
    return edades

def calcular_media(edades):
    """Calcula la media aritmética de una lista de números."""
    if not edades:
        return 0
    return sum(edades) / len(edades)

def contar_categorias_edad(edades, umbral_mayoria=18):
    """
    Cuenta cuántas personas son mayores y menores de edad.
    Retorna un diccionario para facilitar la escalabilidad.
    """
    resultado = {
        "mayores": 0,
        "menores": 0
    }
    for edad in edades:
        if edad >= umbral_mayoria:
            resultado["mayores"] += 1
        else:
            resultado["menores"] += 1
    return resultado

def ejecutar_programa():
    """Función principal que orquestal la lógica del programa."""
    # 1. Entrada de datos
    lista_edades = obtener_edades(5)
    
    # 2. Procesamiento
    media = calcular_media(lista_edades)
    conteo = contar_categorias_edad(lista_edades)
    
    # 3. Salida de resultados
    print("\n--- Resultados ---")
    print(f"Edades ingresadas: {lista_edades}")
    print(f"La media de edad es: {media:.2f}")
    print(f"Personas mayores de edad: {conteo['mayores']}")
    print(f"Personas menores de edad: {conteo['menores']}")

if __name__ == "__main__":
    ejecutar_programa()