print("Problema 5")
print("")
print("")

aprobados=0
reprobados=0
for x in range(10):
    nota=float(input("Introduce la nota del alumno: "))
    if nota>=7:
        aprobados=aprobados+1
    else:
        reprobados=reprobados+1
print("Número de aprobados: ", aprobados)
print("Número de reprobados: ", reprobados)
