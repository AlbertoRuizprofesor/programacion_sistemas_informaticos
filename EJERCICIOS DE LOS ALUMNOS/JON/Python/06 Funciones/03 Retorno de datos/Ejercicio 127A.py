print("Ejercicio 127A")
print("")
print("")

# Cargar 5 notas de alumnos y luego, mediante una función,
# calcular y retornar el promedio de las notas.

def ingresar_notas():
    notas = []
    for i in range(5):
        nota = float(input(f"Ingrese la nota del alumno {i + 1}: "))
        notas.append(nota)
    return notas

def calcular_promedio(notas):
      return sum(notas) / len(notas)

def mostrar_promedio(media):
    if media >= 5:
        print(f"Has aprobado con una media de {media:.2f}.")
    else:
        print(f"Has suspendido con una media de {media:.2f}.")

     
media= calcular_promedio(ingresar_notas())
mostrar_promedio(media)
