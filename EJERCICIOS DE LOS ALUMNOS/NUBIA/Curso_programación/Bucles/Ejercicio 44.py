aprobados=0
reprobados=0

print("A continuación, ingrese la nota de 10 estudiantes para contar cuántos aprobaron y cuántos suspendieron: ")
for f in range(10):
    nota=float(input("Ingrese la nota:"))
    if nota>=7:
        aprobados=aprobados+1
    else:
        reprobados=reprobados+1
        
print("Cantidad de aprobados")
print(aprobados)
print("Cantidad de reprobados")
print(reprobados)
