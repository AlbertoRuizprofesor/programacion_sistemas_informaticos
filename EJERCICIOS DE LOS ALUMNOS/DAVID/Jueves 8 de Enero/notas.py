# Pedimos la nota al usuario
# Usamos float() para permitir decimales como 4.5
nota = float(input("Introduce tu nota: "))

# Mostramos la nota introducida
print(f"su nota es {nota}")

# Estructura condicional
if nota > 4.5:
    print("Usted esta aprobado")
else:
    print("Usted esta suspenso")
    
nota=float(input("Ingrese su nota:"))
if nota<0.0 or nota>10.0:
    print("Suspenso")
    if nota>=4.5 and nota<=5.4:
        print("aprobado")
    if nota>=5.5 and nota<=6.4:
        print("bien")
    if nota>=6.5 and nota<=8.4:
        print("Pedazo Notable")
    if nota>=8.5 and nota<=10:
        print("Sobresaliente")