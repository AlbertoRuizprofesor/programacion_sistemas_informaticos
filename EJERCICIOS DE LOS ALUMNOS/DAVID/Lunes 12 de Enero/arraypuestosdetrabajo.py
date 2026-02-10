# Definimos la lista con los puestos y sus respectivos salarios
nominas = [
    ["Profesor", 2000],
    ["Administrativo", 1500],
    ["Auxiliar", 1200],
    ["Becario", 100]
]

# Usamos un bucle para recorrer la lista por su índice
for i in range(len(nominas)):
    # nominas[i][0] accede al nombre del puesto
    # nominas[i][1] accede al monto del salario
    print(f"Posición {i}: Puesto: {nominas[i][0]}, Salario: {nominas[i][1]}€")