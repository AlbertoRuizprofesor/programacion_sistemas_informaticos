#Ejercicio 194: Plantear una clase Operaciones que solicite en el método __init__ la carga de dos enteros e inmediatamente muestre su suma, resta, multiplicación y división. Hacer cada operación en otro método de la clase Operación y llamarlos desde el mismo método __init__

class Operaciones:
    
    def __init__(self):
        self.valor1=int(input("Introduce el primer valor: "))
        self.valor2=int(input("Introduce el segundo valor: "))
        self.suma()
        self.resta()
        self.producto()
        self.division()
        
    def suma(self):
        suma=self.valor1+self.valor2
        print("La suma es: ",suma)
    def resta(self):
        resta=self.valor1-self.valor2
        print("La resta es:",resta)
    def producto(self):
        producto=self.valor1*self.valor2
        print("El producto es:",producto)
    def division(self):         
        division=self.valor1/self.valor2
        print("La division es:",division)
    
operacion1=Operaciones()

            
        

