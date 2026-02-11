# --- ENTRADA DE DATOS ---
producto = input("Introduce el producto: ").lower() # .lower() convierte a minúsculas para evitar errores
importe = float(input("Introduce el importe base: "))

# --- LÓGICA DE IVA ---
if producto == "bebida" or producto == "alimentación":
    iva_porcentaje = 0.07
    categoria = "Reducido (7%)"

elif producto == "electrodoméstico" or producto == "informática":
    iva_porcentaje = 0.21
    categoria = "General (21%)"

elif producto == "curso de informática" or producto == "curso de cocina":
    iva_porcentaje = 0.0
    categoria = "Exento (0%)"

else:
    # Caso por si el usuario escribe un producto que no está en la lista
    iva_porcentaje = 0.21
    categoria = "General (por defecto 21%)"

# --- CÁLCULOS ---
iva_calculado = importe * iva_porcentaje
total = importe + iva_calculado

# --- RESULTADO ---
print("\n" + "="*30)
print(f"Producto: {producto.capitalize()}")
print(f"Tipo IVA: {categoria}")
print(f"Importe base: {importe:.2f}€")
print(f"IVA:          {iva_calculado:.2f}€")
print(f"TOTAL:        {total:.2f}€")
print("="*30)