class Cuadrado:

    def __init__(self,lado):
        self.lado=lado

    def mostrar_perimetro(self):
        per=self.lado*4
        print("El perimetro del cuadrado es:",per)

    def mostrar_superficie(self):
        sup=self.lado*self.lado
        print("La superficie del cuadrado es:",sup)


# bloque main

cuadrado1=Cuadrado(12)
cuadrado1.mostrar_perimetro()
cuadrado1.mostrar_superficie()
