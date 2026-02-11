# Confeccionar un programa con las siguientes funciones:
# 1) Cargar el nombre de un empleado y su sueldo. Retornar una tupla con dichos valores
# 2) Una función que reciba como parámetro dos tuplas con los nombres y sueldos de empleados y muestre el nombre del empleado con sueldo mayor. 


def datos_empleado():

    print("Introduzca los siguientes datos del empleado: ")
    nombre = input("Nombre: ")
    sueldo = float(input("Sueldo: "))

    return (nombre,sueldo)

def comparar_empleados(empleado1, empleado2):

     
     if empleado1[1] > empleado2[1]:
          
          print(f"{empleado1[0]} tiene el mayor sueldo")
     else:
          
          print(f"{empleado2[0]} tiene el mayor sueldo")

# Programa
empleado1 = datos_empleado()
empleado2 = datos_empleado()
comparar_empleados(empleado1, empleado2)