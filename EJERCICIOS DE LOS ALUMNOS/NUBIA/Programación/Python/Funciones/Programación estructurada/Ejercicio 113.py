# Hacer un promedio de las 5 notas de un alumno.
# Mostrar una línea separadora después de cada vez que cargamos una nota.
# Separar cada carga de notas con una linea separadora.
# Al final, mostrar promedio de notas

def cargar_notas(cantidad):
    notas = []
    for n in range(cantidad):
        nota = float(input(f"Ingresa la nota {n + 1}: "))
        notas.append(nota)
        mostrar_separador()
    return notas

def mostrar_separador():
    print("---------------------")

def calcular_promedio(notas):
    return sum(notas) / len(notas)

def resultado():
    mostrar_separador()
    print("CARGA DE NOTAS")
    cantidad=int(input("Ingresa la cantidad de notas a cargar: "))
    mostrar_separador()
    
    notas = cargar_notas(cantidad)
    promedio = calcular_promedio(notas)
    
    print(f"El promedio de las notas es: {promedio:.2f}")
    mostrar_separador()

# Ejecutar el programa
resultado()
