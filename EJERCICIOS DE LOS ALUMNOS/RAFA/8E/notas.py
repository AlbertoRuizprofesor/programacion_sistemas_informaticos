nota=float(input("ingrese su nota: "))

if nota<0 or nota>10:
    print("nota no valida")
else:
    if nota>0 and nota<4.4:
        print("suspenso")
    if nota>=4.5 and nota<=5.4:
        print("aprobado")
    if nota>=5.5 and nota<=6.4:
        print("bien")
    if nota>=6.5 and nota<=8.4:
        print("Pedazo notable")
    if nota>=8.5 and nota<=10:
        print("sobresaliente")