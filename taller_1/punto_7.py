"""
Debes utilizar todo lo que sabes sobre los strings, las listas y sus 
métodos o funciones para transformar el siguiente texto:

    thor lanzó su martillo#flash ha fallado por un pie! -gritó Loki Laufeyson#dos 
pies -le   corrigió Hulk#flash menea   la   cabeza   como   disgustado... -agrega   el 
comentarista

En:

    Thor lanzó su martillo...
    -   ¡Flash ha fallado por un pie! -gritó Loki Laufeyson.
    -   Dos pies le corrigió Hulk.
    -   Flash menea la cabeza como disgustado... -agrega el comentarista.
"""

texto = """thor lanzó su martillo#flash ha fallado por un pie! -gritó Loki Laufeyson#dos 
pies -le   corrigió Hulk#flash menea   la   cabeza   como   disgustado... -agrega   el 
comentarista"""

print("Texto original: ")
print(texto)

# separar las palabras del texto para organizar los espacios
texto = texto.split()

# uniendo nuevamente el texto con espacios
texto = ' '.join(texto)

# separando el texto en parrafos
texto = texto.split("#")

# eliminando el guion en el parrafo
texto[2] = texto[2].replace("-","")

# poniendo mayuscula a la primera palabra y agregando las tabulaciones y 
# guiones al texto
texto[0] = texto[0].replace("thor","\tThor")
texto[1] = texto[1].replace("flash","\t-\t¡Flash")
texto[2] = texto[2].replace("dos","\t-\tDos")
texto[3] = texto[3].replace("flash","\t-\tFlash")

# agregando al final de los parrafos los puntos
texto[0] += '...'
texto[1] += '.'
texto[2] += '.'
texto[3] += '.'

# uniendo nuevamente los parrafos con saltos de linea
texto = "\n".join(texto)

print("\nTexto modificado: ")
print(texto)
