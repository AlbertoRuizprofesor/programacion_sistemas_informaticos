nota=float(input("Ingrese su nota:"))

if nota<0 or nota>10:
    print("Nota no valida")
    
else:
    if nota>0 and nota<4.4:
        print("Suspenso")
    if nota>=4.5 and nota<=5.4:
        print("Aprobado")
    if nota>=5.5 and nota<6.4:
        print("Bien")
    if nota>=6.5 and nota<=8.4:
        print("Notable")
    if nota>=8.5 and nota<=10:
        print("Sobresaliente")
        
        
        """#if 0>nota>4.4:
        print("Suspenso.")    
    if 4.5<nota<5.5:
        print("Aprobado.")
    if 5.5<nota<6.5:
        print("Bien.")#"""