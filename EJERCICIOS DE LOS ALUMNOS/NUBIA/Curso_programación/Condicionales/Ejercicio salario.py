#Con un input me pide el salario bruto mensual, me tiene que calcular las 14 pagas, si el salario es mayor de 40.000 el impuesto a aplicar es del 21%, si es menor del 15%

salario_bruto_mensual = float(input("Introduce tu salario bruto mensual: "))
salario_anual = salario_bruto_mensual * 14

if salario_anual > 40000:
    impuesto = 0.21
    salario_neto_anual = salario_anual * (1-impuesto)

    print(f"El salario mensual es {float(salario_bruto_mensual)} euros")
    print(f"El salario anual es: {float(salario_anual)}, es mayor a 40000 euros, así que el tramo a aplicar es del 21%")
    print(f"Tiene que pagar: {salario_anual * impuesto} euros de impuestos")
    
else:
    impuesto = 0.15
    salario_neto_anual = salario_anual * (1 - impuesto)
    print(f"El salario mensual es {float(salario_bruto_mensual)} euros")
    print(f"El salario anual es {float(salario_anual)} euros, es menor a 40000 euros, así que el tramo a aplicar es del 15%")
    print(f"Tiene que pagar: {salario_anual * impuesto} euros de impuestos")

