# Confeccionar una función que reciba un string como parámetro y en forma opcional un segundo string con un caracter. 
# La función debe mostrar el string subrayado con el caracter que indica el segundo parámetro

def titulo_subrayado(titulo,caracter="*"):
    # El algoritmo de la función es muy sencillo, imprimimos el primer parámetro:
    print(titulo)
    # Para mostrar subrayado el titulo procedemos a imprimir el caracter del segundo parámetro tantas veces como caracteres tenga el string del titulo. 
    # Utilizamos una propiedad de los string en Python que nos permite utilizar el operador matemático * y generar un string del largo del título:
    print(caracter*len(titulo))

titulo_subrayado("Sistema de Administracion")
titulo_subrayado("Ventas","-")

# -----------------IMPORTANTE-----------------
# Los parámetros por defecto deben ser los últimos que se declaren en la función.
# Se genera un error sintáctico si tratamos de definir una función indicando primero el o los parámetros con valores por defecto: