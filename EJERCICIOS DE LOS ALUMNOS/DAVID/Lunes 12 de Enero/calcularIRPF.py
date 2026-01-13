# Entradas de datos
nomina_bruta_mensual = float(input("Introduce tu nómina bruta mensual: "))
porcentaje_irpf = float(input("Introduce el porcentaje de IRPF (ejemplo 15): "))

# --- FUNCIONES ---

def calcular_irpf(bruto, irpf):
    """Calcula la cantidad de dinero que se retiene."""
    resultado = bruto * (irpf / 100)
    return resultado

def calcular_neto(bruto, retencion):
    """Resta la retención al bruto para obtener el neto."""
    return bruto - retencion

# --- CÁLCULOS MENSUALES ---

# Usamos las funciones para obtener los valores de un solo mes
cuota_irpf_mensual = calcular_irpf(nomina_bruta_mensual, porcentaje_irpf)
neto_mensual = calcular_neto(nomina_bruta_mensual, cuota_irpf_mensual)

# --- CÁLCULOS ANUALES (14 pagas) ---

bruto_anual = nomina_bruta_mensual * 14
irpf_anual = cuota_irpf_mensual * 14
neto_anual = neto_mensual * 14

# --- RESULTADOS ---

print("\n--- DESGLOSE DE NÓMINA (MENSUAL) ---")
print(f"Bruto Mensual: {nomina_bruta_mensual}€")
print(f"Retención IRPF ({porcentaje_irpf}%): {cuota_irpf_mensual}€")
print(f"Neto Mensual: {neto_mensual}€")

print("\n--- DESGLOSE DE NÓMINA (ANUAL - 14 PAGAS) ---")
print(f"Bruto Anual: {bruto_anual}€")
print(f"Total IRPF Anual: {irpf_anual}€")
print(f"Neto Anual (Lo que recibes en el banco): {neto_anual}€")