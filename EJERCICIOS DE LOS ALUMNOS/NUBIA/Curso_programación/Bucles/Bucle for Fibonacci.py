#Ejercicio 39: Hacer proporción de Fibonacci con un bucle for

a = 0
b = 1
c = 0

for x in range(11):
    a = b
    b = c
    c = a + b
    print(c)


#Fibonacci con while
a = 0
b = 1
c = 0

while c < 89:
    a = b
    b = c
    c = a + b
    print(c)

