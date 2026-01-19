

class Operaciones:

    def __init__(self):
        self.valor1 = int(input("Ingrese primer valor: "))
        self.valor2 = int(input("Ingrese segundo valor: "))

    def sumar(self):
        suma = self.valor1+self.valor2
        print("La suma es",suma)

    def restar(self):
        resta=self.valor1-self.valor2
        print("La resta es",resta)

    def multiplicar(self):
        producto=self.valor1*self.valor2
        print("El producto es",producto)

    def division(self):
        division=self.valor1/self.valor2
        print("La division es",division)


# Programa

operacion1=Operaciones()
operacion1.sumar()
operacion1.restar()
operacion1.multiplicar()
operacion1.division()