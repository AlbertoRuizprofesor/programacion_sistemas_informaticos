multiplo_3 = 0
multiplo_5 = 0
no_multiplo_3_y_5 = 0
print("A continuación, ingrese 10 valores enteros para contar cuántos son múltiplos de 3 y cuántos de 5:")
for x in range(10):
    valor = int(input("Ingrese valor:"))
    if valor % 3 == 0:
        multiplo_3 = multiplo_3 + 1
    if valor % 5 == 0:
        multiplo_5 = multiplo_5 + 1
    if valor % 3 != 0 and valor % 5 != 0:
        no_multiplo_3_y_5 = no_multiplo_3_y_5 + 1
        multiplo_3 = multiplo_3 + 0
        multiplo_5 = multiplo_5 + 0
    if valor % 3 == 0 and valor % 5 == 0:
        multiplo_3 = multiplo_3 + 1
        multiplo_5 = multiplo_5 + 1
print("Cantidad de múltiplos de 3:")
print(multiplo_3)
print("Cantidad de múltiplos de 5:")
print(multiplo_5)
print("Cantidad de valores que no son múltiplos ni de 3 ni de 5:")
print(no_multiplo_3_y_5)

















