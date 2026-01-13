#1º Ejercicio, tiene que pedirme por consola un importe
#y me tiene que salir el importe, el iva 21% y el total.

#100

#el importe es 100
#el iva es 21
#el total es 121#

# Solicitamos el importe al usuario
# Usamos float() para permitir números con decimales
entrada = input("Introduce el importe base: ")
importe = float(entrada)

# Definimos el porcentaje de IVA
porcentaje_iva = 0.21

# Realizamos los cálculos
iva_calculado = importe * porcentaje_iva
total = importe + iva_calculado

# Mostramos los resultados
print("-" * 30)
print(f"importe base:  {importe:>10.2f}")
print(f"IVA (21%):     {iva_calculado:>10.2f}")
print(f"Total:         {total:>10.2f}")
print("-" * 30)

# 2º Ahora vamos a hacer el siguiente cambio, añadimos las unidades y descripción, ambos que
#me lo pida por consola: #

# Solicitamos los datos por consola
descripcion = input("Introduce la descripción del producto: ")
unidades = int(input("Introduce el número de unidades: "))
precio_unitario = float(input("Introduce el importe por unidad: "))

# Definimos el porcentaje de IVA
IVA_PORCENTAJE = 0.21

# Realizamos los cálculos
importe_subtotal = unidades * precio_unitario
iva_total = importe_subtotal * IVA_PORCENTAJE
total_a_pagar = importe_subtotal + iva_total

# Mostramos el resultado con el formato solicitado
print("\n" + "="*30)
print(f"{descripcion}")
print(f"unidades: {unidades}")
print(f"el importe es {importe_subtotal:.0f}")
print(f"total: {importe_subtotal:.0f}") # Este es el total sin IVA
print(f"el iva es {iva_total:.0f}")
print(f"el total a pagar es {total_a_pagar:.0f}")
print("="*30)

#3º vamos a añadir un descuento o rebajas, del 30%, este descuento
#se ha de realizar sobre el total, no sobre el total a pagar.


# --- ENTRADA DE DATOS ---
descripcion = input("Introduce la descripción del producto: ")
unidades = int(input("Introduce el número de unidades: "))
precio_unitario = float(input("Introduce el importe por unidad: "))

# --- CONFIGURACIÓN DE TASAS ---
IVA_PORCENTAJE = 0.21
DESCUENTO_PORCENTAJE = 0.30

# --- CÁLCULOS ---
# 1. Calculamos el total inicial (bruto)
importe_bruto = unidades * precio_unitario

# 2. Calculamos el descuento (30% sobre el bruto)
descuento_aplicado = importe_bruto * DESCUENTO_PORCENTAJE

# 3. Calculamos el nuevo total tras la rebaja
total_rebajado = importe_bruto - descuento_aplicado

# 4. Calculamos el IVA sobre el valor ya rebajado
iva_total = total_rebajado * IVA_PORCENTAJE

# 5. Total final a pagar
total_a_pagar = total_rebajado + iva_total

# --- SALIDA DE RESULTADOS ---
print("\n" + "="*30)
print(f"Producto: {descripcion}")
print(f"unidades: {unidades}")
print(f"Importe inicial: {importe_bruto:.0f}")
print(f"Descuento (30%): -{descuento_aplicado:.0f}")
print(f"Total tras descuento: {total_rebajado:.0f}")
print(f"El IVA (21%) es: {iva_total:.0f}")
print(f"El total a pagar es: {total_a_pagar:.0f}")
print("="*30)

#4º Para matrícula, vamos a añadir, que el usuario ponga el dinero al contado que va a entregar
#con lo cual, usaremos un input, y que el programa diga el dinero a devolver.

#Entrega: 300
#a devolver: 58

# --- ENTRADA DE DATOS ---
descripcion = input("Introduce la descripción del producto: ")
unidades = int(input("Introduce el número de unidades: "))
precio_unitario = float(input("Introduce el importe por unidad: "))

# --- CONFIGURACIÓN DE TASAS ---
IVA_PORCENTAJE = 0.21
DESCUENTO_PORCENTAJE = 0.30

# --- CÁLCULOS DE VENTA ---
# 1. Importe bruto
importe_bruto = unidades * precio_unitario

# 2. Descuento (30% sobre el bruto)
descuento_aplicado = importe_bruto * DESCUENTO_PORCENTAJE
total_rebajado = importe_bruto - descuento_aplicado

# 3. IVA (21% sobre el total con descuento)
iva_total = total_rebajado * IVA_PORCENTAJE

# 4. Total final a pagar
total_a_pagar = total_rebajado + iva_total

# --- MOSTRAR TICKET ---
print("\n" + "="*30)
print(f"PRODUCTO: {descripcion}")
print(f"Unidades: {unidades}")
print(f"Importe inicial: {importe_bruto:.2f}")
print(f"Descuento (30%): -{descuento_aplicado:.2f}")
print(f"Total tras descuento: {total_rebajado:.2f}")
print(f"IVA (21%): {iva_total:.2f}")
print(f"TOTAL A PAGAR: {total_a_pagar:.2f}")
print("="*30)

# --- GESTIÓN DEL PAGO ---
entrega = float(input("\nEntrega (dinero al contado): "))
devolver = entrega - total_a_pagar

# --- RESULTADO FINAL ---
print(f"A devolver: {devolver:.2f}")
print("="*30)


importe=int(input("Ingrese el importe: "))
unidades=int(input("Ingrese la cantidad de unidades: "))
tipo_de_pago=input("Ingrese el tipo de pago (tarjeta/efectivo): ")

totalUnidades=importe*unidades
descuento=totalUnidades*0.30
iva=descuento*0.21
total=descuento+iva

print("El importe es:", importe)
print("Las unidades son:", unidades)
print("El total sin IVA es:", totalUnidades)
print("El descuento es (30%):", descuento)
print("El IVA es:", iva)
print("El total con IVA es:", total)



if tipo_de_pago=="tarjeta":
       print("El tipo de pago es tarjeta",total)
else:
   entrega=int(input("Ingrese entrega en metálico: ")) 
   total_devolver=entrega-total
   print("El tipo de pago es efectivo",total_devolver)
