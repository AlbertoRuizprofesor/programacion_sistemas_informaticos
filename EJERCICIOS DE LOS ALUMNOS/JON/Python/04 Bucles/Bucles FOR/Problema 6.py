print("Problema 6")
print("")
print("")

mul3=0
mul5=0
for x in range(10):
    numero=int(input("Introduce un número entero: "))
    if numero%3==0:
        mul3=mul3+1
    if numero%5==0:
        mul5=mul5+1
print("Números múltiplos de 3: ", mul3)
print("Números múltiplos de 5: ", mul5) 
