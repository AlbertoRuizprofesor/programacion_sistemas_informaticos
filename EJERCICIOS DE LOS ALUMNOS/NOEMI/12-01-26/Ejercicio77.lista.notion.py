#Ejercicio 77: Almacenar en una lista los sueldos (valores float) de 5 operarios. Imprimir la lista y el promedio de sueldos.

sueldos=[]

suma=0

for i in range(5):
    valor=float(input("Introduce su sueldo: "))
    sueldos.append(valor)
    suma=suma+valor
    
promedio=suma/5
    
    
print("Lista de sueldos")
print(sueldos)
print("Lista de promedios")    
print(promedio)