# 1. Pedimos el salario bruto mensual
salario_mensual = float(input("Introduce tu salario bruto mensual: "))

# 2. Calculamos el salario bruto anual (14 pagas)
pagas = 14
salario_anual = salario_mensual * pagas

# 3. Determinamos el impuesto según el rango
if salario_anual > 40000:
    porcentaje_impuesto = 0.21
    tipo_mensaje = "21% (Rango alto)"
else:
    porcentaje_impuesto = 0.15
    tipo_mensaje = "15% (Rango bajo)"

# 4. Calculamos los impuestos y el neto
impuestos_totales = salario_anual * porcentaje_impuesto
salario_neto_anual = salario_anual - impuestos_totales
salario_neto_mensual = salario_neto_anual / pagas

# --- RESULTADOS ---
print("-" * 30)
print(f"Salario Bruto Mensual: {salario_mensual:,.2f}€")
print(f"Salario Bruto Anual (14 pagas): {salario_anual:,.2f}€")
print(f"Impuesto aplicado: {tipo_mensaje}")
print(f"Total impuestos anuales: {impuestos_totales:,.2f}€")
print("-" * 30)
print(f"SALARIO NETO ANUAL: {salario_neto_anual:,.2f}€")
print(f"SALARIO NETO MENSUAL (14 pagas): {salario_neto_mensual:,.2f}€")
print("-" * 30)