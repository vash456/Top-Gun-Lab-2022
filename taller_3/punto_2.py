"""
En  un  episodio  de  CSI  un  capo  de  la  mafia  diseño  un interesante   
método   para   evitar   que   en   sus   mensajes descubrieran  los  números  
telefónicos,  las  direcciones  y  los valores  reales  de  sus  transacciones.  
El  método  se  llamaba Saltando al 5.Es   una   estrategia   simple   e   
ingeniosa,   cada   digito   es cambiado por el opuesto del teclado telefónico 
saltando al número 5, comolo muestra la siguientefigura:

Como lo muestra la figura:
    •del 1 se salta al 9 y del 9 al 1 (por encima del 5).
    •del 2 se salta al 8 y del 8 al 2 (por encima del 5).
    •del 3 se salta al 7 y del 7 al 3 (por encima del 5).
    •del 4 se salta al 6 y del 6 al 4 (por encima del 5).
    •del 5 se salta al 0 y del 0 al 5.
Así cuando se pasaba un mensaje primero se codificaban todos los números en él 
de acuerdo con los saltos.
Por ejemplo,si el mensaje es: “Llamar después de las 9:54 al teléfono 3122345676”, 
el mensaje codificado sería: “Llamar después de la 1:06 al teléfono 7988760434”.
Lo  que  debes  haces  es implementar  una  función que codifique  y otra  que 
decodifique  mensajes  utilizando  la estrategia Saltando al 5.
Así que muestra un menú con las opciones.
"""

# se crea una sola funcion ya que la misma codifica y decodifica el mensaje
# la funcion valida cada caracter hasta encontrar digito los cuales codifica o decodifica
def codificar_mensaje(mensaje):
    nuevo_mensaje = ""
    for caracter in mensaje:
        if caracter.isdigit():
            if caracter == "0": caracter = "5"
            elif caracter == "1": caracter = "9"
            elif caracter == "2": caracter = "8"
            elif caracter == "3": caracter = "7"
            elif caracter == "4": caracter = "6"
            elif caracter == "5": caracter = "0"
            elif caracter == "6": caracter = "4"
            elif caracter == "7": caracter = "3"
            elif caracter == "8": caracter = "2"
            elif caracter == "9": caracter = "1"

        nuevo_mensaje += caracter
    return nuevo_mensaje

# variables de control
codifico = False
terminar = True

mensaje = ""

# ciclo para el menu
while terminar:
    print("\nCodificacion \"Saltando al 5\"")
    print("\nMenu: ")
    print("\t1) Escribir mensaje.")
    print("\t2) Codificar mensaje.")
    print("\t3) Decodificar mensaje.")
    print("\t4) Salir del programa")

    opcion = input("\nSeleccione opcion: ")

    if opcion == "1":
        mensaje = input("Ingrese el mensaje: ")
        print("Mensaje guardado.")
    elif opcion == "2":
        # se controla esta opcion para que no se codifique nuevamente
        if not codifico:
            if mensaje != "":
                mensaje = codificar_mensaje(mensaje)
                print(f"Mensaje codificado = {mensaje}")
                codifico = True
            else:
                print("!!! Primero ingrese un mensaje antes de codificar. ¡¡¡")
        else:
                print("!!! El mensaje ya esta codificado. ¡¡¡")
    elif opcion == "3":
        # se controla que primero se codifique antes de entrar en esta opcion
        if codifico:
            mensaje = codificar_mensaje(mensaje)
            print(f"Mensaje decodificado => {mensaje}")
            codifico = False
        else:
            print("!!! Primero codifique el mensaje antes de decodificar. ¡¡¡")
    elif opcion == "4":
        terminar = False
        print("\nPrograma terminado...\n")
    else:
        print("!!! Opcion no valida !!!")    

