#Plantear una clase Persona que contenga dos atributos: nombre y edad. Definir como responsabilidades la carga por teclado y su impresión.

# En el bloque principal del programa definir un objeto de la clase persona y llamar a sus métodos.

# Declarar una segunda clase llamada Empleado que herede de la clase Persona y agregue un atributo sueldo y muestre si debe pagar impuestos (sueldo superior a 3000)

# También en el bloque principal del programa crear un objeto de la clase Empleado.


class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def imprimir(self):
        print(f"Nombre: {self.nombre} , edad {self.edad}")
        #print("Edad: ",self.edad)


class Empleado(Persona):
    def __init__(self,nombre,edad,sueldo=2400):
        super().__init__(nombre,edad)
        self.sueldo=sueldo

    def imprimir(self):
        super().imprimir()
        print("Sueldo: ",self.sueldo)

    def paga_impuestos(self):
        if self.sueldo>3000:
            print("La persona paga impuestos")
        else:
            print("La persona no paga")


class Alumno(Persona):
    def __init__(self,nombre,edad,asignatura):
        super().__init__(nombre,edad)
        self.asignatura=asignatura
        self.nombre=nombre
        self.edad=edad
        print(f"El alumno {self.nombre} tiene esta {self.asignatura}")

class Profesor(Empleado):
    def __init__(self,nombre,edad,sueldo,asignatura2):
        super().__init__(nombre,edad)
        self.nombre=nombre
        self.edad=edad
        self.asignatura2=asignatura2
        self.sueldo=sueldo
        print(f"El profesor : {self.nombre} da {self.asignatura2} cobra {self.sueldo} y tiene {self.edad} años")

class Comercial(Empleado):
    def __init__(self,nombre,edad,sueldo,comision):
        super().__init__(nombre,edad)
        self.nombre=nombre
        self.edad=edad
        self.sueldo=sueldo
        self.comision=comision
        print(self.comision)



#bloque principal 

empleado1=Empleado("Alberto",51)
empleado1.imprimir()
empleado1.paga_impuestos()

alumno1=Alumno("Luis",16,"lengua")
alumno1.imprimir()

profesor1=Profesor("Pedro",32,1500,"Mates")
profesor1.imprimir()

comercial1=Comercial("Ana",23,1800,75)
comercial1.imprimir()