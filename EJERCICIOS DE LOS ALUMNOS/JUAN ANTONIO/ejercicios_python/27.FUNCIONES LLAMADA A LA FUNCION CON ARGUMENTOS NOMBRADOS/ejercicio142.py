#Elaborar una función que muestre la tabla de multiplicar del valor que le enviemos como parámetro. 
# Definir un segundo parámetro llamado termino que por defecto almacene el valor 10. Se deben mostrar 
# tantos términos de la tabla de multiplicar como lo indica el segundo parámetro. 
# Llamar a la función desde el bloque principal de nuestro programa con argumentos nombrados.


# -----------------------------------------
# Función: tabla
# Genera la tabla de multiplicar de un número.
# 'numero' es obligatorio.
# 'terminos' es opcional y por defecto vale 10.
# -----------------------------------------

def tabla(numero, terminos=10):
    for x in range(terminos):        # Recorre desde 0 hasta terminos-1
        resultado = x * numero       # Calcula cada término de la tabla
        print(resultado, ",", sep="", end="")  # Imprime en una sola línea
    print()                          # Salto de línea al final


# -----------------------------------------
# Bloque principal del programa
# Se muestran distintas formas de llamar
# a la función, con y sin argumentos opcionales.
# -----------------------------------------

print("Tabla del 3")
tabla(3)                             # Usa 10 términos por defecto

print("Tabla del 3 con 5 términos")
tabla(3, 5)                          # Se especifican 5 términos

print("Tabla del 3 con 20 términos")
tabla(terminos=20, numero=3)         # Argumentos nombrados (orden libre)
