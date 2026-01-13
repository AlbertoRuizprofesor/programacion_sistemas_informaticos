aprobados=0
suspensos=0
for x in range(10):
    nota=int(input("ingrese la nota: "))
    if nota>=5:
        aprobados=aprobados+1
    else:
        suspensos=suspensos+1
print("cantidad de aprobados", aprobados)
print("cantidad de suspensos", suspensos)