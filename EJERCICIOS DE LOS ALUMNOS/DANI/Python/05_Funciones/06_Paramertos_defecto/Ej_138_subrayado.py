# Confeccionar una función que reciba un string como parámetro y en forma opcional un segundo string con un caracter. 
def palabras():
    frase = input("Escribe algo:\n")
    opcion = input("¿Quieres buscar un caracter? (S/N)")
    
    if opcion.upper == 'S':
        
# La función debe mostrar el string subrayado con el caracter que indica el segundo parámetro