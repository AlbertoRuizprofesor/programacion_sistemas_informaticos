#Ejercicio 5

aprobados=0
suspensos=0

for i in range(11):
    nota=int(input("Introduce su nota: "))
    if nota<7:
        suspensos=suspensos+1
    else:
        aprobados=aprobados+1
print("Cantidad e aprobados", aprobados)
print("Cantidad de suspensos", suspensos)

        
        
        