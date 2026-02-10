def calcular_iva(precio, porcentaje_iva):
    """Calcula el valor del IVA sobre un precio dado."""
    return precio * (porcentaje_iva / 100)

def imprimir_factura(numero_factura, producto, precio):
    """Calcula el total y muestra la factura formateada."""
    iva_aplicado = 21  # Porcentaje estándar
    valor_iva = calcular_iva(precio, iva_aplicado)
    total = precio + valor_iva

    print(f"Factura nº: {numero_factura}")
    print(f"Producto: {producto}")
    print(f"Precio: {precio}")
    print("") # Salto de línea para claridad
    print(f"IVA: {valor_iva}")
    print(f"Total: {total}")

# --- Bloque principal ---
# Llamamos a la función con los datos del ejemplo
imprimir_factura(1, "Portátil HP GAME", 2000)