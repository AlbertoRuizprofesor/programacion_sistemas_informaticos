"""
Escribir un programa que lea 10 números enteros 
y luego muestre cuántos valores ingresados fueron
 múltiplos de 3 y cuántos de 5. Debemos tener
   en cuenta que hay números que son múltiplos
     de 3 y de 5 a la vez.
"""

mul3=0
mul5=0

for x in range (11):
    num = int(input("introduce un número: "))

    if num%3== 0:
        mul3=mul3+1
    if num%5== 0:
        mul5=mul5+1

print("Valores múltiplos de 3: ")
print(mul3)

print("Valores múltiplos de 5: ")
print(mul5)
