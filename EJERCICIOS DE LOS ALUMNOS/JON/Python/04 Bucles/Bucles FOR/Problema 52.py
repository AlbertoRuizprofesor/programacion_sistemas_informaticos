print("Problema 52")
print("")
print("")

n=int(input("Introduce el número de puntos: "))
c1=0
c2=0
c3=0
c4=0
for i in range(n):
    x=int(input("Introduce la coordenada x del punto: "))
    y=int(input("Introduce la coordenada y del punto: "))
    if x>0 and y>0:
        print("El punto está en el primer cuadrante")
        c1=c1+1
    elif x<0 and y>0:
        print("El punto está en el segundo cuadrante")
        c2=c2+1
    elif x<0 and y<0:
        print("El punto está en el tercer cuadrante")
        c3=c3+1
    elif x>0 and y<0:
        print("El punto está en el cuarto cuadrante")
        c4=c4+1

print("Número de puntos en el primer cuadrante: ", c1)
print("Número de puntos en el segundo cuadrante: ", c2)
print("Número de puntos en el tercer cuadrante: ", c3)
print("Número de puntos en el cuarto cuadrante: ", c4)


