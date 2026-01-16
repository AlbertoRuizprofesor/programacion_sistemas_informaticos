#Ejercicio 193: Implementar la clase Operaciones. Se deben cargar dos valores enteros por teclado en el método __init__, calcular su suma, resta, multiplicación y división, cada una en un método, imprimir dichos resultados.

class Operaciones:
    
    def __init__(self):
        self.valor1=int(input("Introduce el primer valor: "))
        self.valor2=int(input("Introduce el segundo valor: "))
        
    def suma(self):
        suma=self.valor1+self.valor2
        print("La suma es:",suma)
    
    def resta(self):
        resta=self.valor1-self.valor2
        print("La resta es: ",resta)
        
    def multiplicacion(self):
        producto=self.valor1*self.valor2
        print("El producto es:",producto)
        
    def division(self):
        if self.valor1!=0 and self.valor2!=0:
            division=self.valor1/self.valor2
            print("La división es:",division)
        else:
            print("No se puede dividir entre 0.")
            
operaciones1=Operaciones()
operaciones1.suma()
operaciones1.resta()
operaciones1.multiplicacion()
operaciones1.division()
            
        