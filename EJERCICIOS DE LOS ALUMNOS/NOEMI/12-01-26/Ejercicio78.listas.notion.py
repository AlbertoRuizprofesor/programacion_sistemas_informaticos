#Ejercicio 78: Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float) Obtener el promedio de las mismas. Contar cuántas personas son más altas que el promedio y cuántas más bajas.

altura=[]
suma=0

for i in range(5):
    valor=float(input("Introduce la altura: "))
    altura.append(valor)
    suma=suma+valor

promedio=suma/5
    
print("Las alturas ingresadas son: ", altura)
print(f"El promedio de las alturas ingresadas es: {promedio:.2f}")

altas=0
bajas=0

for x in range(5):
    if altura[x]>promedio:
        altas=altas+1

    else:
        if altura[x]<=promedio:
            bajas=bajas+1
        
        
print("Personas más altas que el promedio: ", altas)    
print("personas mas bajas que el promedio: ", bajas)