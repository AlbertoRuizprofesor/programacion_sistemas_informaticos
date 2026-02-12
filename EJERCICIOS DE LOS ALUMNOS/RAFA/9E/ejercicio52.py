cant1=0
cant2=0
cant3=0
cant4=0
n=int(input("cuantos puntos:"))
for f in range(n):
    x=int(input("coordenada x:"))
    y=int(input("coordenada y:"))
    if x>0 and y>0:
        cant1=cant1+1
    else:
        if x<0 and y>0:
            cant2=cant2+1
        else:
            if x<0 and y<0:
                cant3=cant3+1
            else:
                if x>0 and y<0:
                    cant4=cant4+1

print("1 cuadrante:")
print(cant1)
print("2cuadrante:")
print(cant2)
print("3 cuadrante:")
print(cant3)
print("4 cuadrante:")
print(cant4)
