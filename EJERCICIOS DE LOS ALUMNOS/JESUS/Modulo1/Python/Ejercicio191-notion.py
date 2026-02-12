#Desarrollar una clase que represente un punto en el plano y tenga los siguientes métodos: 
# inicializar los valores de x e y que llegan como parámetros, imprimir en que cuadrante se encuentra dicho punto (concepto matemático, 
# primer cuadrante si x e y son positivas, si x<0 e y>0 segundo cuadrante, etc.)


class Cordenada:
    def __init__(self):
          self.x=int(input("Ingresa coordenada 1 "))
          self.y=int(input("Ingresa coordenada 2 "))


    def imprimir(self):
      print(f"Las coordenadas son x {self.x} e y {self.y}")


    def impri_cuadrante(self):
        if self.x>0 and self.y>0:
            print("Primer cuadrante")
        else:
            if self.x<0 and self.y>0:
                print("Segundo cuadrante")
            else:
                if self.x<0 and self.y<0:
                    print("Tercer cuadrante")
                else:
                    if self.x>0 and self.y<0:
                        print("Cuarto cuadrante")


punto1=Cordenada()
punto1.imprimir()
punto1.impri_cuadrante()

