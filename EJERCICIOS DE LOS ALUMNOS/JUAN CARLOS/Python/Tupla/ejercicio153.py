"""
Lista 5 empleados: [nombre, tupla(sueldo1,sueldo2,sueldo3)].
3 funciones: cargar, totales, >10000 trimestral.
"""

#Funciones
def mensaje(mensaje):
    print(f"=== === === {mensaje} === === ===")

def cargar_empleados():
    empleados = []
    for cnt in range(5):
        nombre = input(f"Empleado {cnt+1}: ").strip()
        s1 = float(input("Sueldo mes 1: "))
        s2 = float(input("Sueldo mes 2: "))
        s3 = float(input("Sueldo mes 3: "))
        tupla_sueldos = (s1, s2, s3)
        empleados.append([nombre, tupla_sueldos])
    return empleados

def total_cobrado(empleados):
    print("\nTOTALES:")
    for emp in empleados:
        nombre = emp[0]
        total = sum(emp[1])  # Suma tupla
        print(f"{nombre}: {total:.2f}")

def mayores_10000(empleados):
    print("\n>10.000 trimestral:")
    for emp in empleados:
        if sum(emp[1]) > 10000:
            print(emp[0])


#Main
empleados = cargar_empleados()
mensaje("Datos cargados")
total_cobrado(empleados)
mayores_10000(empleados)
mensaje("Fin del programa")
