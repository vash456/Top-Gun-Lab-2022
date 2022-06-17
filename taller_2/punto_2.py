"""
El funcionamiento de los radares de velocidad se basa en un principio básico 
de la cinética que establece 𝑣=𝑥/𝑡, donde:
    v:velocidad
    x:posición - distancia
    t:tiempo
El  radar  envía  dos  haces  de  luz  en ciertotiempo(en  segundos)  y obtiene 
la distancia del vehículo al radar en cada haz de luz enviado, así puede calcular 
la velocidad del vehículo y establecer si está en los límites  permitidos  o  
por  el  contrario  debe  ser  multado.  El  radar  toma estos datos en metros.
Dadas las dos distancias obtenidas del vehículo y el tiempo, calcular si debe 
pagar una multa de acuerdo con la siguiente tabla:

    Velocidad (km/h)    Multa
    De 1 a 20           Llamado de atención por baja velocidad.
    De 21 a 60          Normal
    De 61 a 80          Llamado de atención por alta velocidad.
    De 81 a 120         Multa tipo I
    Más de 120          Multa tipo II e inmovilización del vehículo.
    
En caso de tener multapor velocidad, se le practica un examen de alcoholemia al 
conductor  que  acarrea  multas   adicionales de acuerdo conla siguiente norma:

    •Entre 20 y 39 mg de etanol/l00 ml  de sangre total, además de las  sanciones
    previstas  en  la  presente  ley,  se  decretará  la suspensión  de  la  
    licencia  de  conducción  entre  seis  (6)  y  doce (12) meses.

    •Primer grado de embriaguez entre 40 y 99 mg de etanol/100 ml de   sangre   
    total,   adicionalmente   a   la   sanción   multa,   se decretará  la  
    suspensión  de  la  Licencia  de  Conducción  entre uno (1) y tres (3) años.

    •Segundo   grado   de   embriaguez   entre   100   y   149   mg   de 
    etanol/100  ml  de  sangre  total,  adicionalmente  a  la  sanción multa, se 
    decretará la suspensión de la Licencia de Conducción entre tres (3) y 
    cinco (5) años, y la obligación de realizar curso de   sensibilización,   
    conocimientos   y   consecuencias   de   la alcoholemia   y   drogadicción  
    en   centros   de   rehabilitación debidamente  autorizados,  por  un  
    mínimo  de  cuarenta  (40) horas.

    •Tercer  grado  de  embriaguez,  desde  150  mg  de  etanol/100  ml de 
    sangre total en adelante, adicionalmente a la sanción de la sanción de multa,
    se decretará la suspensión entre cinco (5) y diez (10) años de la Licencia 
    de Conducción, y la obligación de realizar curso de sensibilización, 
    conocimientos y consecuencias de la alcoholemia y drogadicción en centros de 
    rehabilitación debidamente  autorizados,  por  un  mínimo  de  ochenta
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
    print("Llamado de atención por baja velocidad.")
elif speed >= 21 and speed <= 60:
    print("Normal")
elif speed >= 61 and speed <= 80:
    print("Llamado de atención por alta velocidad.")
elif speed >= 81 and speed <= 120:
    mensaje_multa = "\t- Multa tipo I."
    multa = True
elif speed > 120:
    mensaje_multa = "\t- Multa tipo II e inmovilización del vehículo."
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
        m_multa = "\n\t- Suspensión de la licencia de conducción entre seis (6) y doce (12) meses."
    elif result_test >= 40 and result_test < 100:
        m_multa = "\n\t- Suspensión  de  la  Licencia  de  Conducción  entre uno (1) y tres (3) años."
    elif result_test >= 100 and result_test < 150:
        m_multa = """\n\t- Suspensión de la Licencia de Conducción entre tres (3) y cinco (5) años."
        - Realizar de manera obligatorio curso de sensibilización, conocimientos y 
          consecuencias de la alcoholemia y drogadicción en centros de rehabilitación 
          debidamente autorizados, por un mínimo de cuarenta (40) horas."""
    elif result_test >= 150:
        m_multa = """\n\t- Suspensión entre cinco (5) y diez (10) años de la Licencia de Conducción 
        - Realizar de manera obligatorio curso de sensibilización, conocimientos y 
          consecuencias de la alcoholemia y drogadicción en centros de rehabilitación 
          debidamente autorizados, por un mínimo de ochenta (80) horas."""
    print("\nMulta:")
    print(mensaje_multa+m_multa)
