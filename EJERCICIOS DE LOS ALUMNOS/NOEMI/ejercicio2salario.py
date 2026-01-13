#Ejercicio de salario.

Salariobruto=int(input("Introzuca su salario bruto mensual: "))

Salarioanual=Salariobruto*14

if Salarioanual > 40000:
    Impuesto=Salarioanual*0.21
    salario_neto=Salarioanual - Impuesto
    salario=Salarioanual-Impuesto
    print("Se le aplica el 21%")
    print("Tiene que pagar a Hacienda", Impuesto )
else:
    Impuesto1=Salarioanual*0.15
    salario_neto=Salarioanual-Impuesto1
    print("Se le aplica el 15%")
    print("Tiene que pagar a Hacienda", Impuesto1)
    
print("Su salario mensual es", Salariobruto)
print("El salario anual es de", Salarioanual)
print("Su salario anual neto es:", salario_neto)

