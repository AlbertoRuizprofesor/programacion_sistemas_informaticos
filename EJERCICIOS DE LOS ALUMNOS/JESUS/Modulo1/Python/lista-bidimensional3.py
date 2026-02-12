#Ejercicio: hacer el mismo pero con puestos y salarios, "profesor", 2000, 
# "administrativo",1500, "auxiliar", 1200, "Becario",100
# igual que en el ejercicio anterior con respecto a print(posicion......)
 
salarios=[["profesor", 2000],["administrativo",1500],["auxiliar", 1200],["becario",100]]

print("posicion 0,0 ", salarios[0][0]) #imprime profesor
print("posicion 0,1 ", salarios[0][1]) #imprime 2000
print("posicion 1,0 ", salarios[1][0]) #imprime administrativo
print("posicion 1,1 ", salarios[1][1]) #imprime 1500
print("posicion 2,0 ", salarios[2][0]) #imprime auxiliar
print("posicion 2,1 ", salarios[2][1]) #imprime 1200
print("posicion 3,0 ", salarios[3][0]) #imprime becario
print("posicion 3,1 ", salarios[3][1]) #imprime 100

for profesion, salario in salarios:
    print(f"La profesion {profesion} tiene un salario de {salario}")
