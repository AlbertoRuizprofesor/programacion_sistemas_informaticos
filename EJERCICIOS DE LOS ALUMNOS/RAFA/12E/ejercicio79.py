sueldosman=[]
print("Sueldos turno manana")
for x in range(4):
    valor=float(input("Ingrese sueldo:"))
    sueldosman.append(valor)

sueldostar=[]
print("Sueldos turno tarde")
for x in range(4):
    valor=float(input("Ingrese sueldo:"))
    sueldostar.append(valor)

print("Turno manana")
print(sueldosman)
print("Turno tarde")
print(sueldostar)