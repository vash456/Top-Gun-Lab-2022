"""
Se  debe  crear  un  programaque  dada  luna  longitud  en  cuadros
(mayor a cero), genere un tablero,como en la siguiente imagen(Es un tablero 
con una longitud de 8x8):
                        #   #   #   #
                      #   #   #   #
                        #   #   #   #
                      #   #   #   #
                        #   #   #   #
                      #   #   #   #
                        #   #   #   #
                      #   #   #   #
"""

print("Generar tablero")

# solicitando longitud
terminar = True
while terminar:
    longitud = int(input("Ingrese una longitud: "))
    
    # validando longitud
    if longitud > 0:
        terminar = False
    else:
        print("Ingrese un valos mayor a cero!!!")

# dibujando tablero
cambio = False
dibujo = ""
print("")
for lon in range(longitud*3):
    for ancho in range(longitud*3):
        # caracteres a dibujar
        if cambio:
            dibujo += "*"
        else:
            dibujo += " "

        # condicion de cambio de columnas
        if (ancho+1) % 3 == 0:
            if cambio:
                cambio = False
            else:
                cambio = True
    
    # imprimiendo fila completa
    print(dibujo)
    dibujo = ""

    # para casos con longitud impar
    if (longitud+1) % 2 == 0:
        if cambio:
            cambio = False
        else:
            cambio = True

    # condicion de cambio para las filas
    if (lon+1) % 3 == 0:
        if cambio:
            cambio = False
        else:
            cambio = True

