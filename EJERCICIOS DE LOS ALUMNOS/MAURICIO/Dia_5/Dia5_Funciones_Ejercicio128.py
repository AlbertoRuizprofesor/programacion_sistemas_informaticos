# FUNCIONES


def datos():
    lis = []
    for _ in range(5):
        dato = int(input("Ingrese valor: "))
        lis.append(dato)
    return lis


def mayormenor(lis):
    may = lis[0]
    men = lis[0]
    for x in range(1, len(lis)):
        if lis[x] > may:
            may = lis[x]
        else:
            if lis[x] < men:
                men = lis[x]
    print(f"El valor mayor de la lista es {may}")
    print(f"El valor menor de la lista es {men}")


# BLOKE

lista = datos()
mayormenor(lista)
