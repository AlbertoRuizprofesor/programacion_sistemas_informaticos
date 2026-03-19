import random

# 1. Preparamos el contador
frecuencias = {i: 0 for i in range(2, 13)}

# 2. Simulamos 1000 lanzamientos
lanzamientos = 1000
for _ in range(lanzamientos):
    suma = random.randint(1, 6) + random.randint(1, 6)
    frecuencias[suma] += 1

# 3. Mostramos los resultados de forma visual
print(f"--- Resultados de {lanzamientos} lanzamientos ---")
print("Suma | Frecuencia | Gráfico")
print("-" * 35)

for suma, veces in frecuencias.items():
    # Creamos una barra de asteriscos (cada asterisco representa 5 apariciones)
    grafico = "*" * (veces // 5) 
    print(f"{suma:>4} | {veces:>10} | {grafico}")

print("-" * 35)
print("Nota: Cada '*' representa aproximadamente 5 apariciones.")