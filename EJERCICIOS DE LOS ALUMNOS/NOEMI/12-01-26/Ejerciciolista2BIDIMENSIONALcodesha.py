#Ejercicio 2 lista bidimensional: hacer el mismo pero con puestos y salarios, "profesor", 2000,  "administrativo",1500, "auxiliar", 1200, "Becario",100 igual que en el ejercicio anterior con respecto a print(posicion......)

lista=[["profesor",2000],["administrativo",1500],["auxiliar",1200],["becario",100]]

print("posicion 0,0:", lista[0][0])
print("posicion 0,1:", lista[0][1])
print("posicion 1,0:", lista[1][0])
print("posicion 1,1:", lista[1][1])
print("posicion 2,0:", lista[2][0])
print("posicion 2,1:", lista[2][1])
print("posicion 3,0:", lista[3][0])
print("posicion 3,1:", lista[3][1])
                                    
print("***************")

for puesto, numeros in lista:
    print(f"El puesto de {puesto} gana {numeros}.")
    print("--------")