#EJERCICIO 186 CREAR UNA CLASE:   Es una sola clase con muchos objetos(persona1,persona2...)

class Persona:  #Class es una plantilla donde vamos a crear objetos(registros).
    
    def inicializar(self,nom,apellidos,dom,copostal,prov,ciud):    #Ponemos self siempre, antes de las variables.
        self.nom=nom
        self.apellidos=apellidos
        self.dom=dom
        self.copostal=copostal
        self.prov=prov
        self.ciud=ciud
        
                                    #Los metodos son las funciones dentro de la clase.
    def imprimir(self):
        print("Nombre y apellidos:",self.nom,self.apellidos)
        print("Provincia y ciudad:",self.prov,self.ciud)
        print("Domicilio y Código postal:",self.dom,self.copostal)   
        
    def separacion(self):
        print("**********************")    
        
#Bloque principal (los objetos), instanciar una clase es crear un objeto.
        
persona1=Persona()     #Persona() es la clase y siempre empieza por mayuscula.
persona1.inicializar("Noemi","Gonzalez","Malaga","Torremolinos","Calle Molinos,",29620)    #El punto en medio tiene la funcion de llamar a todas las funciones.
persona1.imprimir()
persona1.separacion()

#***************************

persona2=Persona()
persona2.inicializar("Jose","Ahmad","Malaga","Benalmádena","Calle Bella Sombra,",29630)
persona2.imprimir()
persona1.separacion()
#***************************

persona3=Persona()
persona3.inicializar("Sheila","Tobajas","Malaga","Alhaurín de la torre","Calle mar y sol,",29640)
persona3.imprimir()
persona1.separacion()
#**************************

persona4=Persona()
persona4.inicializar("Pilar","Gonzalez","Malaga","Malaga","Calle la esquina,",29650)
persona4.imprimir()
persona1.separacion()
