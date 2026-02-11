# Escribir un programa que solicite por teclado 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.

aprobados=0
suspensos=0

for x in range(1, 11):
    nota=float(input(f"Ingrese la {x}ª nota: "))
    
    if nota>=5:
        aprobados=aprobados+1
    else:
        suspensos=suspensos+1

print(f"Cantidad de aprobados {aprobados}")
print(f"Cantidad de suspensos {suspensos}")

# Nuevamente utilizamos el for ya que sabemos que el ciclo repetitivo debe repetirse 10 veces.
# Recordemos que si utilizamos el while debemos llevar un contador y recordar de incrementarlo en cada vuelta.