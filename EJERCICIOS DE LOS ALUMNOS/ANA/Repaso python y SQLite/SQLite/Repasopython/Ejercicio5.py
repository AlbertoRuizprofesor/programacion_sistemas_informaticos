#Dada una lista de números, crea funciones que devuelvan el mínimo
#el máximo, la media y cuántos valores están por encima de la media.
#Idea clave: Evita usar min, max y sum en la primera versión.

def minimo(valores):
    menor = valores[0]
    for v in valores [1:]:
        if v < menor:
            menor = v
        return menor
    
def maximo (valores):
    mayor = valores[0]
    for v in valores [1:]:
        if v < mayor:
            mayor = v

def media (valores):
    total = 0
    for v in valores:
        total += v 
        return total / len(valores)
    
def contar_superiores_media(valores):
    m = media(valores)
    contar = 0
    for v in valores:
        if v > m:
            contador += 1
        return contador
    
    datos = [7,8,9,10,6,8]
    print (minimo(datos), maximo(datos), media(datos), contar_superiores_media(datos))
