

# 1) Listado de todos los alumnos con sus notas
# 2) Consulta de un alumno por su dni, mostrar las materias que cursa y sus notas.

def cargar_alumnos():
    
    alumnos = {}
    print("Introduzca los datos de 3 alumnos: ")

    for i in range(3):
        
        dni = int(input(f"Ingrese el numero de dni del alumno {i}: ")) 
        listamaterias = [] 
        continua ="s"
        
        while continua=="s":
            
            materia = input("Ingrese el nombre de materia que cursa: ")
            nota = int(input("Ingrese la nota: "))
            listamaterias.append((materia,nota))
            continua = input("Desea cargar otra materia para dicho alumno [s/n}: ")
        
        alumnos[dni]=listamaterias 


def listar(alumnos):
    for dni in alumnos: 

        print("Dni del alumno",dni) 
        print("Materias que cursa y notas")
        
        for nota,materia in alumnos[dni]: 
            print(materia,nota)


def consulta_notas(alumnos):

    dni=int(input("Ingrese el dni a consultar:"))
    
    if dni in alumnos: 
        for nota,materia in alumnos[dni]: 
            print(materia,nota) 

# Programa

alumnos=cargar_alumnos()
listar(alumnos)
consulta_notas(alumnos)