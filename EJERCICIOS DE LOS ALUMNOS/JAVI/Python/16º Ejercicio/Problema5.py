aprobados=0
suspensos=0
for f in range(10):
    nota=float(input("Ingrese la nota:"))
    if nota>=7:
        aprobados=aprobados+1
    else:
        suspensos=suspensos+1
print("Cantidad de aprobados")
print(aprobados)
print("Cantidad de reprobados")
print(suspensos)


