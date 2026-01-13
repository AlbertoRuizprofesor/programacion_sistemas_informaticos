#crear una lista bidimensional con materias y notas 
 #Ejercicio: hacer el mismo pero con notas, ejemplo "Matematicas", 10, "Historia",9, "Lengua",5
 #cuando me muestre print posicion, al tener esta lista mas elementos quiero que salgan todos los elementos
 #de manera que se tiene que quedar en el print("posicion.. ", notaw[x][x][x])   

notas=[["matematicas",10],["historia",9],["lengua",5]]
print("posicion 0,0", notas[0][0]) #imprime matematicas
print("posicion 0,1 ", notas[0][1]) #imprime 10 
print("posicion 1,0", notas[1][0]) #imprime historia
print("posicion 1,1", notas[1][1]) #imprime 9
print("posicion 2,0 ", notas[2][0]) #imprime lengua
print("posicion 2,1 ", notas[2][1]) #imprime 5

for materia, nota in notas:
    print(f"La nota de {materia} es {nota}")

