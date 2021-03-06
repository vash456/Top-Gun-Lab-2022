"""
El funcionamiento de los radares de velocidad se basa en un principio b谩sico 
de la cin茅tica que establece 饾懀=饾懃/饾憽, donde:
    v:velocidad
    x:posici贸n - distancia
    t:tiempo
El  radar  env铆a  dos  haces  de  luz  en ciertotiempo(en  segundos)  y obtiene 
la distancia del veh铆culo al radar en cada haz de luz enviado, as铆 puede calcular 
la velocidad del veh铆culo y establecer si est谩 en los l铆mites  permitidos  o  
por  el  contrario  debe  ser  multado.  El  radar  toma estos datos en metros.
Dadas las dos distancias obtenidas del veh铆culo y el tiempo, calcular si debe 
pagar una multa de acuerdo con la siguiente tabla:

    Velocidad (km/h)    Multa
    De 1 a 20           Llamado de atenci贸n por baja velocidad.
    De 21 a 60          Normal
    De 61 a 80          Llamado de atenci贸n por alta velocidad.
    De 81 a 120         Multa tipo I
    M谩s de 120          Multa tipo II e inmovilizaci贸n del veh铆culo.
    
En caso de tener multapor velocidad, se le practica un examen de alcoholemia al 
conductor  que  acarrea  multas   adicionales de acuerdo conla siguiente norma:

    鈥ntre 20 y 39 mg de etanol/l00 ml  de sangre total, adem谩s de las  sanciones
    previstas  en  la  presente  ley,  se  decretar谩  la suspensi贸n  de  la  
    licencia  de  conducci贸n  entre  seis  (6)  y  doce (12) meses.

    鈥rimer grado de embriaguez entre 40 y 99 mg de etanol/100 ml de   sangre   
    total,   adicionalmente   a   la   sanci贸n   multa,   se decretar谩  la  
    suspensi贸n  de  la  Licencia  de  Conducci贸n  entre uno (1) y tres (3) a帽os.

    鈥egundo   grado   de   embriaguez   entre   100   y   149   mg   de 
    etanol/100  ml  de  sangre  total,  adicionalmente  a  la  sanci贸n multa, se 
    decretar谩 la suspensi贸n de la Licencia de Conducci贸n entre tres (3) y 
    cinco (5) a帽os, y la obligaci贸n de realizar curso de   sensibilizaci贸n,   
    conocimientos   y   consecuencias   de   la alcoholemia   y   drogadicci贸n  
    en   centros   de   rehabilitaci贸n debidamente  autorizados,  por  un  
    m铆nimo  de  cuarenta  (40) horas.

    鈥ercer  grado  de  embriaguez,  desde  150  mg  de  etanol/100  ml de 
    sangre total en adelante, adicionalmente a la sanci贸n de la sanci贸n de multa,
    se decretar谩 la suspensi贸n entre cinco (5) y diez (10) a帽os de la Licencia 
    de Conducci贸n, y la obligaci贸n de realizar curso de sensibilizaci贸n, 
    conocimientos y consecuencias de la alcoholemia y drogadicci贸n en centros de 
    rehabilitaci贸n debidamente  autorizados,  por  un  m铆nimo  de  ochenta
    (80) horas.
"""

# solicitando distancias
validation_distance = True
while validation_distance:
    distance_1 = input("Ingrese la distancia 1 en metros: ")
    distance_2 = input("Ingrese la distancia 2 en metros: ")

    # validando que se ingrese numeros
    if (distance_1.isdigit() and distance_2.isdigit()):
        validation_distance = False
    else:
        print("Distancias no validas. Debe ingresar numeros.")

# solicitando tiempo
validation_time = True
while validation_time:
    time = input("Ingrese el tiempo: ")

    # validando que se ingrese numeros
    if (time.isdigit()):
        if float(time) <= 0:
            print("Valores de tiempo no validos.")
        else:
            validation_time = False
    else:
        print("Distancias no validas. Debe ingresar numeros.")

# realizando conversion metros a kilometros
distance_1 = float(distance_1)/1000 # distance * 1km/1000m
distance_2 = float(distance_2)/1000 # distance * 1km/1000m

# realizando conversion de segundos a horas
time = (float(time)/60) * (1/60) # time * 1min/60seg * 1h/60min

# calculando velocidad
speed = abs((distance_2 - distance_1) / time)
print(f"\nVelocidad del vehiculo = {speed:.2f} km/h")

# rangos de velocidades y multa respectiva
multa = False
if speed >= 1 and speed <= 20:
    print("Llamado de atenci贸n por baja velocidad.")
elif speed >= 21 and speed <= 60:
    print("Normal")
elif speed >= 61 and speed <= 80:
    print("Llamado de atenci贸n por alta velocidad.")
elif speed >= 81 and speed <= 120:
    mensaje_multa = "\t- Multa tipo I."
    multa = True
elif speed > 120:
    mensaje_multa = "\t- Multa tipo II e inmovilizaci贸n del veh铆culo."
    multa = True

# examen de alcoholemia
if multa:
    print("\nSe realiza examen de alcoholemia...")
    validate_result = True
    while validate_result:
        result_test = input("Ingrese resultados del examen de alcoholemia: ")
        
        # validando que se ingrese numeros
        if result_test.isdigit():
            if float(result_test) <= 0:
                print("Valores no validos.")
            else:
                validate_result = False
        else:
            print("Valores no validos. Debe ingresar numeros.")
    
    # convertir de str a float
    result_test = float(result_test)

    # rangos de resultados de test de alcoholemia y multa correspondiente
    m_multa = ""
    if result_test >= 20 and result_test < 40:
        m_multa = "\n\t- Suspensi贸n de la licencia de conducci贸n entre seis (6) y doce (12) meses."
    elif result_test >= 40 and result_test < 100:
        m_multa = "\n\t- Suspensi贸n  de  la  Licencia  de  Conducci贸n  entre uno (1) y tres (3) a帽os."
    elif result_test >= 100 and result_test < 150:
        m_multa = """\n\t- Suspensi贸n de la Licencia de Conducci贸n entre tres (3) y cinco (5) a帽os."
        - Realizar de manera obligatorio curso de sensibilizaci贸n, conocimientos y 
          consecuencias de la alcoholemia y drogadicci贸n en centros de rehabilitaci贸n 
          debidamente autorizados, por un m铆nimo de cuarenta (40) horas."""
    elif result_test >= 150:
        m_multa = """\n\t- Suspensi贸n entre cinco (5) y diez (10) a帽os de la Licencia de Conducci贸n 
        - Realizar de manera obligatorio curso de sensibilizaci贸n, conocimientos y 
          consecuencias de la alcoholemia y drogadicci贸n en centros de rehabilitaci贸n 
          debidamente autorizados, por un m铆nimo de ochenta (80) horas."""
    print("\nMulta:")
    print(mensaje_multa+m_multa)
