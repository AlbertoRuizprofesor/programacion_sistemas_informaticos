##Ejercicio 198: 
""" Plantear un programa que permita jugar a los dados. Las reglas de juego son:
    se tiran tres dados si los tres salen con el mismo valor mostrar un mensaje que "gano", sino "perdió".
    Lo primero que hacemos es identificar las clases:
    Podemos identificar la clase Dado y la clase JuegoDeDados.
    Luego los atributos y los métodos de cada clase:"""
    
import random

class Dado:
    def tirar(self):              #metodos
        self.valor=random.randint(1,6)
        
    def imprimir(self):
        print("Valor del dado:",self.valor)
        
    def retornar_dado(self):
        return self.valor
    
class JuegoDeDados:
    def __init__(self):
        self.dado1=Dado()         #3 Dado (3 objetos de la clase Dado)
        self.dado2=Dado()
        self.dado3=Dado()
        
    def jugar(self):
        self.dado1.tirar()
        self.dado1.imprimir()
        self.dado2.tirar()
        self.dado2.imprimir()
        self.dado3.tirar()
        self.dado3.imprimir()
        
        if self.dado1.retornar_dado()== self.dado2.retornar_dado() and \
            self.dado1.retornar_dado()==self.dado3.retornar_dado():
            
            print("Ganaste!")
        else:
            print("Perdiste!")
            
juego_dados=JuegoDeDados()
juego_dados.jugar()
            
        
        
        
        
    
    