#Desarrollar un programa que cargue los lados de un triángulo e implemente los siguientes métodos: 
# inicializar los atributos, imprimir el valor del lado mayor y otro método que muestre si es equilátero o no. 
# El nombre de la clase llamarla Triangulo.

class Triangulo:

    def __init__(self):
        self.lado1=int(input("Ingresa el primer lado: "))
        self.lado2=int(input("Ingresa el segundo lado: "))
        self.lado3=int(input("Ingresa el tercer lado: "))

    def imprimir(self):
        print(f"Los valores de los lados del triangulo son: ")
        print(f"Lado 1 {self.lado1} Lado 2 {self.lado2} Lado 3 {self.lado3}")


    def lado_mayor(self):
        print("Lado mayor")
        
        
        if self.lado1>self.lado2 and self.lado1>self.lado3:
            print(self.lado1)
        else:
            if self.lado2>self.lado3:
                print(self.lado2)
            else:
                print(self.lado3)

    def es_equilatero(self):
        if self.lado1==self.lado2 and self.lado1==self.lado3:
            print("El triangulo es equilatero")
        else:
            print("El triangulo no es equilatero")

    #bloque principal 

triangulo1=Triangulo()
#triangulo1.inicializar()
triangulo1.imprimir()
triangulo1.lado_mayor()
triangulo1.es_equilatero()
