print("Problema 53")
print("")
print("")

pos=0
neg=0
multi15=0
sumapar=0
for i in range(10):
    n=int(input("Introduce un número: "))
    if n>=0:
        pos=pos+1
    else:
        neg=neg+1
    if n%15==0:
        multi15=multi15+1
    if n%2==0:
        sumapar=sumapar+n
print("Números positivos: ", pos)
print("Números negativos: ", neg)
print("Múltiplos de 15: ", multi15)
print("Suma de los números positivos: ", sumapar)
    