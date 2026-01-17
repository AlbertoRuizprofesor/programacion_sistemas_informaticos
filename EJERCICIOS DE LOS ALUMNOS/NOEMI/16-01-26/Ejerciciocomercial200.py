#CREAR TRES CLASES: 1 PERSONA(NOMBRE,EDAD), 2 EMPLEADO (SUELDO), 3 COMERCIAL (COMISION).

class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Edad:",self.edad)
        
class Empleado(Persona):
    def __init__(self,nombre,edad,sueldo):
        super().__init__(nombre,edad)
        self.sueldo=sueldo
        
    def imprimir(self):
        super().imprimir()
        print("Sueldo:",self.sueldo)
        
    def paga_impuestos(self):
        impuesto=0.05
    
        if self.sueldo>3000:
            retencion=self.sueldo*impuesto
            sueldo_Final=self.sueldo-retencion
            print("Paga impuestos.")
            print("Retención:",retencion)
            print("Sueldo final:",sueldo_Final)
        else:
            print("No paga impuestos.")
            
class Comercial(Empleado):
    def __init__(self, nombre, edad, sueldo, comision):
        super().__init__(nombre, edad, sueldo)
        self.comision=comision
        
    def imprimir(self):
        super().imprimir()
        print("Comision por ventas:",self.comision)
        
persona1=Persona("Sheila",20)
persona1.imprimir()
print("*"*50)
empleado1=Empleado("Maria",40,3500)
empleado1.imprimir()
empleado1.paga_impuestos()
print("*"*50)
comercial1=Comercial("Sephora",60,3344,0.2)
comercial1.imprimir()
