#Implementaremos una clase llamada Persona que tendrá como atributo (variable) su nombre y dos métodos (funciones), 
# uno de dichos métodos inicializará el atributo nombre y el siguiente método mostrará en la pantalla el contenido del mismo.


class Persona:

    def __init__(self,nombre,apellido,domicilio="",cp="",telefono="",ciudad="",provincia=""):
        self.nombre=nombre
        self.apellido=apellido
        self.domicilio=domicilio
        self.cp=cp
        self.telefono=telefono
        self.ciudad=ciudad
        self.provincia=provincia


    def imprimir(self):
        print(f"Nombre {self.nombre} Apellido {self.apellido} dir {self.domicilio} CP {self.cp} Telf {self.telefono} ciudad {self.ciudad} provincia {self.provincia}")



#bloque principal

persona1=Persona("Pedro","Martin","calle falsa",29000,7222222,"Malaga","Malaga")
#persona1.inicializar("Pedro","Martin","calle falsa",29000,7222222,"Malaga","Malaga")
persona1.imprimir()


persona2=Persona("Carla","Sanchez")
#persona2.inicializar("Carla","Sanchez")
persona2.imprimir()

persona3=Persona("Albertron","Ruiz")
#persona3.inicializar("Albeltron","Ruiz")
persona3.imprimir()