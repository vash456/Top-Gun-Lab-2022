"""
La siguiente gráfica muestra el comportamiento de los descendientes y  ascendientes  
de  una  persona,  si  asumimos  que  esta  persona  es  la generación  0,  la  
generación  1  serán  dos  personas  (sus  padres)  la generación 2 serán 4 personas 
(sus abuelos) y así sucesivamente.

    generacion                                      personas
    3           o   o   o   o       o   o   o   o   8
    2             o       o           o       o     4  
    1                 o                   o         2
    0                           o                   1
Debe crear un programaque dada una generación (mayor o igual a cero):
    -Le indique al usuario el número total de personas de la familia (de todas las 
    generaciones hasta la generación dada).
    -Muestre  el  número  de  personas  de  cada  generación  mientras hace el cálculo.
"""

print("Generaciones pasadas\n")

# validando la generacion ingresada
val_gen = True
while val_gen:
    generacion = input("Ingrese la generacion: ")

    # validando el valor ingresado
    if generacion.isdigit():
        generacion = int(generacion)
        if generacion >= 0:
            val_gen = False
        else:
            print("El valor debe ser mayor o igual a cero.")
    else:
        print("El valor debe ser numerico positivo")

print("\n\tGeneracion => Personas")
total = 0
for g in range(generacion+1):

    # calculo de personas por generacion
    personas = 2 ** g
    total += personas

    print(f"\t{g}\t=>\t{personas}")

print(f"Total personas = {total}")

