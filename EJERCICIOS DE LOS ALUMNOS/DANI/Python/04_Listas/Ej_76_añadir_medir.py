# Realizar la carga de valores enteros por teclado, almacenarlos en una lista. Finalizar la carga de enteros al ingresar el cero. 
# Mostrar finalmente el tamaño de la lista.

lista=[]

# En este problema la lista crecerá hasta que el operador ingrese el valor cero. 
# La carga del primer valor se efectúa antes del ciclo while ya que la condición depende del valor ingresado:
valor=int(input("Ingresar valor (0 para finalizar):"))

# Luego dentro del ciclo while procedemos a agregar al final de la lista el valor ingresado y solicitar la carga del siguiente valor:
while valor!=0:
    lista.append(valor)
    valor=int(input("Ingresar valor (0 para finalizar):"))

# Cuando salimos del ciclo repetitivo procedemos a obtener el tamaño de la lista mediante la función len:
print(f"Tamano de la lista: {len(lista)}")