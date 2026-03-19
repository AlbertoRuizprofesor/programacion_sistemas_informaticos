def minimo(valores):
    menor = valores[0]
    for v in valores[1:]:
        if v < menor:
            menor = v
    return menor

def maximo(valores):
    mayor = valores[0]
    for v in valores[1:]:
        if v > mayor:
            mayor = v
    return mayor

def media(valores):
    total = 0
    for v in valores:
        total += v
    return total / len(valores)

def contar_superiores_media(valores):
    m = media(valores)
    contador = 0
    for v in valores:
        if v > m:
            contador += 1
    return contador

datos = [4, 5, 7, 8, 4, 7]
print(minimo(datos), maximo(datos), media(datos), contar_superiores_media(datos))
