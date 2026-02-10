# Almacenar en una lista 5 empleados, cada elemento de la lista es una sub lista con el nombre del empleado junto a sus últimos tres sueldos (estos tres valores en una tupla) 
# El programa debe tener las siguientes funciones:
# 1) Carga de los nombres de empleados y sus últimos tres sueldos.
# 2) Imprimir el monto total cobrado por cada empleado.
# 3) Imprimir los nombres de empleados que tuvieron un ingreso trimestral mayor a 10000 en los últimos tres meses.

def cargar_empleados():
    
    empleados = [] 
    print("Introduzca los datos de 5 empleados: ")

    for i in range(5):

        nombre = input("Nombre: ")
        sueldo1 = float(input("Primer sueldo: "))
        sueldo2 = float(input("Segundo sueldo: "))
        sueldo3 = float(input("Tercer sueldo: "))
        empleados.append([nombre,(sueldo1,sueldo2,sueldo3)]) 
    return empleados 


def imprimir_total_empleado(empleados):
   

    print("Monta el total percibido por cada empleado en los últimos 3 meses")

    for i in range(len(empleados)): 
        total = 0 
        for j in range(len(empleados[i][1])): 
            total += empleados[i][1][j]
        
        print(empleados[i][0],total) 

    

def ganancias_superior10k(empleados):
    
    print("Empleados con ingresos superiores a 10000 en los últimos 3 meses")

    for i in range(len(empleados)): 
        total = 0 
        for j in range(len(empleados[i][1])): 
            total += empleados[i][1][j]
        
        if total > 10000:
            print(empleados[i][0],total) 

# Programa
empleados = cargar_empleados()
imprimir_total_empleado(empleados)
ganancias_superior10k(empleados)