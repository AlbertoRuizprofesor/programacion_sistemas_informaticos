"""
Plantear un programa que permita jugar a los dados. Las reglas de juego son:

se tiran tres dados si los tres salen con el mismo valor mostrar un mensaje que "gano", sino "perdió".

Lo primero que hacemos es identificar las clases:

Podemos identificar la clase Dado y la clase JuegoDeDados.

Luego los atributos y los métodos de cada clase:
"""

import random

class Dado:
    
    def tirar(self):
        self.tirada = random.randint(1,6)
        
    def imprimir(self):
        print(f"Ha salido {self.tirada}")
        
    def retornar_tirada(self):
        return self.tirada


class Juegodados:
    def __init__(self):
        self.dado1 = Dado()
        self.dado2 = Dado()
        self.dado3 = Dado()
    
    def jugar(self):
        print("JUEGO DE DADOS")
        print("Saca los 3 números iguales y gana")
        print("-"*50)
        self.dado1.tirar()
        self.dado1.imprimir()
        self.dado2.tirar()
        self.dado2.imprimir()
        self.dado3.tirar()
        self.dado3.imprimir()
        if self.dado1.retornar_tirada() == self.dado2.retornar_tirada() and self.dado1.retornar_valor() == self.dado3.retornar_tirada():
            print("HAS GANADO")
        else:
            print("HAS PERDIDO")
            
# Bloque principal
juego = Juegodados()
juego.jugar()

