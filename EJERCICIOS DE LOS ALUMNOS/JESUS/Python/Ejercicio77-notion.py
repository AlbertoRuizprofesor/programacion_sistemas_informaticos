#Almacenar en una lista los sueldos (valores float) de 5 operarios. 
# Imprimir la lista y el promedio de sueldos.

sueldos=[]
suma=0
for x in range(5):
    valor=float(input("ingrese el sueldo del operario: "))
    sueldos.append(valor)
    suma=suma+valor

    print("lista de sueldos")
    print(sueldos)
    promedio=suma/5
    print("promedio de sueldos")
    print(promedio)