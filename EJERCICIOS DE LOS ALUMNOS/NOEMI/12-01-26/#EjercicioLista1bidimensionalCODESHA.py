#Ejercicio Lista 1 bidimensional CODESHARE: hacer el mismo pero con notas, ejemplo "Matematicas", 10, "Historia",9, "Lengua",5 cuando me muestre print posicion, al tener esta lista mas elementos quiero que salgan todos los elementos de manera que se tiene que quedar en el print("posicion.. ", notaw[x][x][x])  


notas=[["Matematicas", 10],["Historia",9],["Lengua",5]]

print("posicion 0,0:", notas[0][0])
print("posicion 0,1: ", notas[0][1])  
print("posicion 1,0. ", notas[1][0])  
print("posicion 1,1. ", notas[1][1])  
print("posición 2,0: ", notas[2][0])
print("posicion 2,1: ", notas[2][1])

print("***************")

for asignaturas, numeros in notas:
    print(f"El resultado de {asignaturas} es {numeros}.")
    print("--------")