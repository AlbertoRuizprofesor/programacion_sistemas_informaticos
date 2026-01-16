"""
Cargar 2 empleados (nombre,sueldo) → tuplas → función compara, imprime mayor sueldo.
"""

#Funciones
def mensaje(mensaje):
    print(f"=== === === {mensaje} === === ===")

def cargar_empleado():
    nombre = input("Nombre empleado: ").strip()
    sueldo = float(input("Sueldo: "))
    return (nombre, sueldo)  # Tupla


def mayor_sueldo(emp1, emp2):
    if emp1[1] > emp2[1]:
        print(f"Mayor sueldo: {emp1[0]} ({emp1[1]:.2f})")
    else:
        print(f"Mayor sueldo: {emp2[0]} ({emp2[1]:.2f})")


#Main
empleado1 = cargar_empleado()
empleado2 = cargar_empleado()
mensaje("Comparación")
mayor_sueldo(empleado1, empleado2)
mensaje("Fin del programa")
