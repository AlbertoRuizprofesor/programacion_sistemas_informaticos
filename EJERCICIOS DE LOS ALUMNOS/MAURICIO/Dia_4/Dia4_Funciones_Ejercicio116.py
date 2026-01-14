# Confeccionar una aplicación que muestre una presentación en pantalla del programa.
# Solicite la carga de dos valores y nos muestre la suma.
# Mostrar finalmente un mensaje de despedida del programa.

# Definimos Funciones


def mostrar_mensaje(mensaje):
    print("\n*************************************************")
    print("*")
    print(f"* {mensaje}")
    print("*")
    print("*************************************************\n")


def carga_suma():

    v1 = int(input("\nIngrese el primer valor:"))
    v2 = int(input("\nIngrese el segundo valor:"))
    s = v1 + v2
    mostrar_mensaje(f"La suma de los dos valores es: {s}")


# Bloque Principal

mostrar_mensaje("El programa calcula la suma de dos valores ingresados por teclado.")
carga_suma()
mostrar_mensaje("Gracias por utilizar este programa")
