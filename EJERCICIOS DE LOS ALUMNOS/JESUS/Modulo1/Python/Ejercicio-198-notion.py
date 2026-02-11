#Plantear un programa que permita jugar a los dados. Las reglas de juego son:

# se tiran tres dados si los tres salen con el mismo valor mostrar un mensaje que "gano", sino "perdió".

# Lo primero que hacemos es identificar las clases:

# Podemos identificar la clase Dado y la clase JuegoDeDados.

# Luego los atributos y los métodos de cada clase:

from random import randint 

class Dado:
    def tirar(self):
        self.valor=randint(1,6)
    
    def imprimir(self):
        print("Valor del dado: ", self.valor)

    def retornar_valor(self):
        return self.valor
    
class Jugar_dados():
    def __init__(self):
        self.dado1=Dado()
        self.dado2=Dado()
        self.dado3=Dado()

    def jugar(self):
        self.dado1.tirar()
        self.dado1.imprimir()
        self.dado2.tirar()
        self.dado2.imprimir()
        self.dado3.tirar()
        self.dado3.imprimir()

        if self.dado1.retornar_valor()==self.dado2.retornar_valor() and self.dado1.retornar_valor==self.dado3.retornar_valor():
            print("Ganas")
        else:
            print("Pierdes")

#bloque principal 

juego_dados=Jugar_dados()
juego_dados.jugar()