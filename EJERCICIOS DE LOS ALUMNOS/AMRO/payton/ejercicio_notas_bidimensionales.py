notas=[["Matemáticas", 10], ["Historia", 9], ["Lengua", 5]]
print("posicion 0,0 ", notas[0][0])  
print("posicion 0,1 ", notas[0][1])  
print("posicion 1,0 ", notas[1][0])  
print("posicion 1,1 ", notas[1][1])  
print("posicion 2,0 ", notas[2][0])  
print("posicion 2,1 ", notas[2][1])  


#posicion Fila, columna

print("*******************")


for fila in range(len(notas)):
    for columna in range(len(notas[fila])):
        print(f"posicion {fila}, {columna}", notas[fila][columna])    
