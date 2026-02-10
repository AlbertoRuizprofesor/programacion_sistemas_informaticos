# Implementaremos una clase llamada Persona que tendrá como atributo (variable) su nombre y dos métodos (funciones), uno de dichos métodos inicializará el atributo 
# nombre y el siguiente método mostrará en la pantalla el contenido del mismo.
# Definir dos objetos de la clase Persona.

class Persona:

    def inicializar(self,nombre,apellido,direccion,cp,ciudad,provincia):
        self.nombre=nombre # Dentro del método diferenciamos los atributos del objeto antecediendo el identificador self:
        self.apellido=apellido
        self.direccion=direccion
        self.cp=cp
        self.ciudad=ciudad
        self.provincia=provincia
        
    def imprimir(self):
        print(f"\nNombre: {self.nombre}\nApellido: {self.apellido}\nDirección: {self.direccion}\nCódigo Postal: {self.cp}\nCiudad: {self.ciudad}\nProvincia: {self.provincia}\n")

# bloque principal

persona1=Persona()
persona1.inicializar("Pedro","Ramirez","C/ Taco",12348,"Cancún","Cancuncito")
persona1.imprimir()

persona2=Persona()
persona2.inicializar("Carl","Ampara","Avn. La luz",23456,"Málaga","Málaga")
persona2.imprimir()

persona3=Persona()
persona3.inicializar("Marc","Iano","Marte",78590,"Marte","Marte")
persona3.imprimir()