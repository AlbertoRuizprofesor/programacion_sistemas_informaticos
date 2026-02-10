#numeros mayor que 100

mayor=0
for x in range(5):
    numero=int(input("escribe un numero: "))
    if numero > 100:
        mayor += 1
print("cantidad de numeros mayores que 100: ", mayor)