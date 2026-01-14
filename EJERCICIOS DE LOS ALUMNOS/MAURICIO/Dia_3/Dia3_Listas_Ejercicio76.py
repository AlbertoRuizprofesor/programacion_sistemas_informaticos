lista = []
for i in range(4):

    nombre = input(f"Nombre del individuo {i}: ")
    altura = float(input(f"Altura del mismo {i}: "))
    individuo = [nombre, altura]
    lista.append(individuo)

print(lista)
altTotal = 0
for n in range(len(lista)):
    altTotal = altTotal + lista[n][1]

print(f"Alturas media de los {len(lista)} participantes: {altTotal/len(lista)}")
