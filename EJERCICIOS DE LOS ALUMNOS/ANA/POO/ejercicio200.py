

class Persona:

    def __init__(self):
        self.nombre=input("Ingrese el nombre: ")
        self.edad=int(input("Ingrese la edad: "))

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Edad:",self.edad)


class Empleado(Persona):

    def __init__(self):
       
        super().__init__() 
        self.sueldo=float(input("Ingrese el sueldo: "))

    def imprimir(self):
        
        super().imprimir()
        print("Sueldo: ",self.sueldo)

    def paga_impuestos(self):
        if self.sueldo>3000:
            print("El empleado debe pagar impuestos")
        else:
            print("No paga impuestos")


# Programa

print("Instanciamos Persona")
persona=Persona()
persona.imprimir()

print("____________________________")
print("Instanciamos Empleado")

empleado=Empleado()
empleado.imprimir()
empleado.paga_impuestos()