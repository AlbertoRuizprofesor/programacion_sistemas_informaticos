salarios = [["Profe", 3000], ["Funcionario", 2000], ["sepulturero", 1600]]
print("posicion 0,0 ", salarios[0][0])
print("posicion 1,0 ", salarios[1][0])
print("posicion 2,0 ", salarios[2][0])
print("posicion 0,1 ", salarios[0][1])
print("posicion 1,1 ", salarios[1][1])
print("posicion 2,1 ", salarios[2][1])

# posicion Fila, columna

print("*******************")


for profesion, sueldo in salarios:
    print(f"La salario de {profesion} es de {sueldo}.")
    print("-----")
