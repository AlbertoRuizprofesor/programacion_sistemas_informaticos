"""
Confeccionar una función que reciba un string como parámetro y en forma opcional un segundo string con un caracter.
La función debe mostrar el string subrayado con el caracter que indica el segundo parámetro
"""

#Funciones
def mensaje(mensaje):
    print(f"=== === === {mensaje} === === ===")

def subrayarTexto(texto, caracter="-"):
    lineaSub = caracter * len(texto)
    print(texto)
    print(lineaSub)


#Main
subrayarTexto("Hola Mundo")
mensaje("Con guion")
subrayarTexto("Hola Mundo", "*")
mensaje("Con asterisco")
subrayarTexto("Python", "=")
mensaje("Fin del programa")
