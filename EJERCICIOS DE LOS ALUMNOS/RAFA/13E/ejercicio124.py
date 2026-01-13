def retornar_perimetro(lado):
    perimetro= lado*3
    return perimetro

lado=int(input("valor de un lado: "))
print("el perimetro del triangulo es: ",retornar_perimetro(lado))