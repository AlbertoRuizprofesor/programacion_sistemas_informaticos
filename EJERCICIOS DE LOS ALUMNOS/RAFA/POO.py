class Suma:
    def __init__(self):
        self.valor1=0
        self.valor2=0
    
    def presentacion(self):
        print("Programa que permite cargar dos valores por teclado.")
        print("Efectua la suma de los valores")
        print("Muestra el resultado de la suma")
        print("*******************************")

    def carga_suma(self):
        self.valor1=int(input("ingrese el primer valor: "))
        self.valor2=int(input("ingrese el segundo valor"))
        suma=self.valor1+self.valor2
        print("la suma de los valores es: ", suma)
                        
    def finalizacion(self):
        print("gracias por utilizar este programa")
    
#PRINCIPAL
rafa=Suma()
rafa.carga_suma()
rafa.finalizacion()
