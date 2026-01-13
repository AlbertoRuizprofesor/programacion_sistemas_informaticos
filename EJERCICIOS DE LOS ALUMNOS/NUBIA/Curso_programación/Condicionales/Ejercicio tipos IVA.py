#Tipos de IVA: me tiene que pedir un producto e importe.
#Si el producto es bebida, IVA del 7%
#Si el producto eselectrodoméstico, IVA del 21%
#Si el producto es curso de informática o de cocina, IVA del 0%

producto = input("Ingrese el tipo de producto (bebida, alimento, electrodoméstico, curso de informática, curso de cocina): ")
importe = float(input("Ingrese el importe del producto: "))

if producto == "bebida" or producto == "alimento":
    iva = 0.07
    print(f"El IVA para bebidas es del 7%")
    print(f"Precio con IVA: {importe * (1 + iva):.2f}")
elif producto == "electrodoméstico":
    iva = 0.21
    print(f"El IVA para electrodomésticos es del 21%. Importe con IVA: {importe * (1 + iva):.2f}")
elif producto == "curso de informática" or producto == "curso de cocina":
    iva = 0.0
    print(f"El IVA para cursos es del 0%. Importe con IVA: {importe * (1 + iva):.2f}")

else:
    while True:
        producto = input("Producto no reconocido. Por favor, ingrese un producto válido: ")
        importe = float(input("Ingrese el importe del producto: "))
        if producto == "bebida":
            iva = 0.07
            print(f"El IVA para bebidas es del 7%")
            print(f"Precio con IVA: {importe * (1 + iva):.2f}")
            break
        elif producto == "electrodoméstico":
            iva = 0.21
            print(f"El IVA para electrodomésticos es del 21%. Importe con IVA: {importe * (1 + iva):.2f}")
            break
        elif producto == "curso de informática" or producto == "curso de cocina":
            iva = 0.0
            print(f"El IVA para cursos es del 0%. Importe con IVA: {importe * (1 + iva):.2f}")
            break