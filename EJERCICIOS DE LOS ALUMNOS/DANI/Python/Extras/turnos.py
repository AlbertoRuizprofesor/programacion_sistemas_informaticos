# Creacion de listas vacias
mañana = []
tarde = []
noche = []

# Para 3 horarios
for x in range(3):
    # Indicar la hora de entrada
    horario = int(input("Dime la hora de entrada: "))
    
    # Ver si es una hora coherente
    if horario >= 0 and horario <= 23:
        # Turno de mañana
        if horario >= 7 and horario < 15:
            print("Trabajador de mañana:")
            sueldo = float(input(f"Dame el sueldo del empleado num {x+1}: "))
            mañana.append(sueldo)
        # Turno de tarde
        elif horario >= 15 and horario < 23:
            print("Trabajador de tarde:")
            sueldo = float(input(f"Dame el sueldo del empleado num {x+1}: "))
            tarde.append(sueldo)
        # Turno de noche
        else:
            print("Trabajador de noche:")
            sueldo = float(input(f"Dame el sueldo del empleado num {x+1}: "))
            noche.append(sueldo)
    else:
        print("Hora no válida. Cerrando")
        break        

# Mostrar los horarios
print(f"Sueldos del turno de mañana: {mañana}")
print(f"Sueldos del turno de tarde: {tarde}")
print(f"Sueldos del turno de noche: {noche}")