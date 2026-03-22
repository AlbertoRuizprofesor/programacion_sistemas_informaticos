#Pide una frase y muestra: número de palabras, conjunto de palabras únicas, palabra más larga y frecuencia de cada palabra.

frase = input ("frase: " ).lower()
for signo in ",.¨:;!?":
    frase = frase.replace(signo, "")

palabras = frase.split()
for palabra in palabras:
    frecuencias [palabra] = frecuencias.get(palabra,0) +1

    mas_larga = ""
    for palabra in palabras:
        
        if len(palabra) > len (mas_larga):
            mas_larga = palabra
    print ("numero de palabras: ", len(palabras))
    print ("unicas: ", set(palabras))
    print ("mas larga: ", mas_largas)
    print ("frecuencias: ", frecuencias)
    