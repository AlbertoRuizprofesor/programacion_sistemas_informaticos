# FUNCIONES


def cargar_nota():
    notas = []
    for i in range(5):
        nota = float(input(f"Introduce la nota {i+1}: "))
        notas.append(nota)
    return notas


def calcular_media(lista_notas):
    return sum(lista_notas) / len(lista_notas)


def mostrar_resultado(med):
    if med >= 5:
        print(f"\nHas aprobado con una media de {med:.2f}")
    else:
        print(f"\nHas suspendido con una media de {med:.2f}")


# BLOKE
notas_alumno = cargar_nota()
media = calcular_media(notas_alumno)
mostrar_resultado(media)
