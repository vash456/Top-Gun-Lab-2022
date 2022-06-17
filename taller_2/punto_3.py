"""
En 1590 Galileo presentó las leyes de la caída libre:
Sin   resistencia   los   cuerpos   caen   a   la   misma   velocidad
independientemente   de   su   masa,   forma   y   composición.
Cuando   se   lanza   un   objeto   la   distancia   que   recorre   es 
proporcional al tiempo d=v∗t±(1/2)∗g∗𝑡2, donde:
    •d es la distancia recorrida.
    •g  es  la  aceleración  originada  por  la  gravedad  es  decir 9.8𝑚/𝑠2.
    •t es el tiempo transcurrido.
Esta y otras afirmaciones le valieron a Galileo una amable invitación a 
beber la Cicuta, pero finalmente fue condonada su pena a cadena Perpetua.
En   honor   al   gran   científico Galilei, se   debe implementar   una 
aplicación que dada una altura en metros de un edificio del que se 
va a lanzar una esfera, vaya mostrando la distancia recorrida segundo
a segundo hasta tocar el suelo.
"""

print("Caida libre\n")

# declarando variables
t = 0
g = 9.8

# solicitando altura del edificio
altura = float(input("Ingrese la altura en metros del edificio: "))

print("\nSoltando esfera...")
print("\tt = Tiempo -> d = Distancia recorrida")

finish = True
while finish:
    # calculo posicion
    distancia = - (1/2) * g * (t**2) + altura

    # validacion de llegada al suelo
    if distancia <= 0:
        finish = False
        distancia = 0.
    
    # mostrar distancia recorrida cada segundo
    print(f"\tt = {t} seg -> d = {distancia:.2f} metros")
    t += 1

print("La esfera llego al suelo")
    