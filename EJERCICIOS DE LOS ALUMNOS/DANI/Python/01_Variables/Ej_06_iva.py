# quiero que me pida con un input un importe, 
# me calcule el iva y me de el total(importe+iva)

importe = float(input("Dame un importe: "))
iva = 0.21

total = importe * (1 + iva)

#Sacamos el resultado por consola.
print(f"El impuesto sería añadir a {importe} un 21%, por lo que el total sería {total}€")