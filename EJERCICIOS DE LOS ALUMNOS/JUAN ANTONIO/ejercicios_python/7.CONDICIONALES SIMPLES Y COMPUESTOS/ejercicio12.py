#Se ingresan tres notas de un alumno, 
# si el promedio es mayor o igual a siete mostrar un mensaje "Promocionado".

#Ingreso de datos 
nota1 = int(input("Introduzca la primera nota:"))
nota2 = int(input("Introduzca la segunda nota:"))
nota3 = int(input("Introduzca la tercera nota:"))

#Cálculo de la nota media
nota_media = (nota1 + nota2 + nota3) / 3

#Se realiza la comparación con 7 y se muestran los mensajes porl consola
if nota_media >= 7:
    print(f"El alumno 'HA PROMOCIONADO' ya que su nota media es {nota_media}")
else:
    print("El alumno 'NO HA PROMOCIONADO'")
    