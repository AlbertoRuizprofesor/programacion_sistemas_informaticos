import re

# Texto de prueba con varios correos y algunos "trampa"
texto_de_ejemplo = """
Hola, puedes contactarme en juan.perez@gmail.com o en el 
correo de la empresa: soporte_tecnico@mi-tienda.es. 
No escribas a esto@com porque le falta la extensión, 
ni a "falso @ gmail.com" porque tiene espacios. 
El de ventas es ventas123@corporativo.net.
"""

def extraer_emails(texto):
    # El patrón r"" indica que es una cadena "raw" (ignora escapes de Python)
    # [\w.-]+  -> busca letras, números, guiones o puntos
    # @        -> busca el símbolo arroba
    # \.[a-z]{2,3} -> busca un punto seguido de 2 o 3 letras (com, es, net)
    patron = r"[\w.-]+@[\w.-]+\.[a-z]{2,4}"
    
    # re.findall busca todas las coincidencias y las mete en una lista
    encontrados = re.findall(patron, texto.lower())
    
    return encontrados

# --- EJECUCIÓN ---
print("--- BUSCADOR DE CORREOS ---")
# Puedes usar el texto de ejemplo o pedir uno al usuario
resultado = extraer_emails(texto_de_ejemplo)

if resultado:
    print(f"Se han encontrado {len(resultado)} correos válidos:")
    for i, email in enumerate(resultado, 1):
        print(f"{i}. {email}")
else:
    print("No se encontraron correos con el formato correcto.")