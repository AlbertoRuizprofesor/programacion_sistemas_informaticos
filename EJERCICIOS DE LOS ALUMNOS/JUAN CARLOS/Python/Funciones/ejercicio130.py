"""Desarrollar una función que reciba una lista de string y nos retorne el que tiene más caracteres.
Si hay más de uno con dicha cantidad de caracteres debe retornar el que tiene un valor de componente más baja.
En el bloque principal iniciamos por asignación la lista de string:"""
#Funciones
def mensaje(mensaje):
    print(f"=== === === {mensaje} === === ===")
def contarPalabras(listaString):
    resultado = listaString[0]
    max_len = len(resultado)
    for cnt in listaString[1:]:
        len_s = len(cnt)
        if len_s > max_len or (len_s == max_len and cnt < resultado):
            resultado = cnt
            max_len = len_s
    return resultado
#Main
listaAsignacion = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "febrera", "febreru"]
mensaje("Resultado")
print(contarPalabras(listaAsignacion))
mensaje("")
