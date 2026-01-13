"""
Ejercicio: salario

con un input me pide el salario bruto mensual
me tiene que calcular las 14 pagas
si el salario es mayor de 40.000 el impuesto a aplicar es del 21%, si es menor del 15%

Resultado

Su salario mensual es 4000
el salario anual es de 48.000
el tramo a aplicar es del 21%
Tiene que pagar a Hacienda: 
"""

salario = float(input("Introduce el salario bruto mensual: "))
anual = salario * 14
iva1 = anual * 0.21
iva2 = anual * 0.15

print("Su salario mensual es: " , (anual/14))
print("Su salario anual es: " , anual)


if anual > 40000 :
    print("El tramo a aplicar es: 21%")
    print("Tiene que pagar a Hacienda: " , iva1)
else:
    print("El tramo a aplicar es: 15%")
    print("Tiene que pagar a Hacienda: " , iva2)




    

