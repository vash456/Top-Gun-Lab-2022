"""El capitán del barco pirata Thousand Sunny,el famoso Monkey D. Luffy te 
ha designado para que sirva de vigía en el mástil principal. Esto es lo que te ha
dichoel capitán:
Tu   misión   es   simple   marinero,   pero   importante   para
la tripulación,   cuando   veas   alguna   de   estas   criaturas   debes 
decirlo de esta manera:
  •¡Ahoy! capitán, un Kraken
  •¡Ahoy! capitán, unas Sirenas
  •¡Ahoy! capitán, una Ballena
  •¡Ahoy! capitán, un Hipocampo
  •¡Ahoy! capitán, una Macaraprono
  •¡Ahoy! capitán, un Pulpo
  •¡Ahoy! capitán, unos Leviatanes
  •¡Ahoy! capitán, Unas Hidras
Tu vida va en ello marinero, debes pronunciarlos con el articulo correcto de 
acuerdo con su especie (uno, una, unos, unas).
Además, debes decirla dirección del barco por la que aparece la criatura:
  •A babor
  •A estribor
  •Por la proa
  •Por la popa 
Para cumplir la misión debes crear un programa que,dada la criatura y  
la  ubicación,  construya  la  cadena  correcta.El  programa  se  debe ejecutar 
las  veces  que  sea  necesario  hasta  que  el capital te  diga “stop”.
Por ejemplo, si aparecen:
  •Kraken y Babor debe decir:¡Ahoy!capitán, un Kraken a babor.
  •Leviatanes y Proa debe decir:¡Ahoy!capitán, unos Leviatanes por la proa.
Y así hasta que ingresen la palabra para detener el programa."""

# declaracion de variables
mensajes_criaturas = [
                        "¡Ahoy! capitán, un Kraken ",
                        "¡Ahoy! capitán, unas Sirenas ",
                        "¡Ahoy! capitán, una Ballena ",
                        "¡Ahoy! capitán, un Hipocampo ",
                        "¡Ahoy! capitán, una Macaraprono ",
                        "¡Ahoy! capitán, un Pulpo ",
                        "¡Ahoy! capitán, unos Leviatanes ",
                        "¡Ahoy! capitán, Unas Hidras "
                    ]

mensajes_direcciones = [
                        "a babor.",
                        "a estribor.",
                        "por la proa.",
                        "por la popa." 
                        ]

criaturas_opciones = ["Kraken", "Sirenas", "Ballena", "Hipocampo", 
                      "Macaraprono", "Pulpo", "Leviatanes", "Hidras"]

direcciones_opciones = ["Babor", "Estribor", "Proa", "Popa"]

# mostrando mensajes de opciones
print("Bienvenido marinero, ahora es cuando empieza tu labor de vigia")

print("\nCriaturas: ")
for criatura in criaturas_opciones:
    print(f"\t{criatura}")

print("\nDirecciones: ")

for direccion in direcciones_opciones:
    print(f"\t{direccion}")

print("\nPara terminar el programa ingresar 'stop'")

# ciclo principal del programa
terminar = True
while terminar:
    print("")

    # variables de control
    terminar1 = True
    terminar2 = True

    # ciclo para entrada de dato de criatura
    while terminar1:
        criatura_avistada = input("Ingrese la criatura avistada: ").capitalize()
        # validacion de criatura y validacion condicion para finalizar programa
        if criatura_avistada in criaturas_opciones:
            # se guarda la posicion para saber el mensaje correspodiente
            index_criatura = criaturas_opciones.index(criatura_avistada)
            terminar1 = False
        elif criatura_avistada == "Stop":
            terminar = False
            terminar1 = False
            terminar2 = False
        else:
            print("Criatura no valida!!!")

    # ciclo para entrada de dato de direccion
    while terminar2:
        direccion_barco = input("Ingrese la direccion del barco: ").capitalize()
        # validacion de direccion y validacion condicion para finalizar programa
        if direccion_barco in direcciones_opciones:
            # se guarda la posicion para saber el mensaje correspodiente
            index_direccion = direcciones_opciones.index(direccion_barco)
            terminar2 = False
        elif direccion_barco == "Stop":
            terminar = False
            terminar1 = False
            terminar2 = False
        else:
            print("Direccion no valida!!!")
    print("")

    # se concatena el mensaje final
    if terminar:
        print("Marinero dice: " 
              + mensajes_criaturas[index_criatura] 
              + mensajes_direcciones[index_direccion])

print("Capitan dice: !Stop¡")
