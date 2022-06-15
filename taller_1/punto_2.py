"""
Realizar un programa que le solicite a 3 usuarios ingresar por teclado 
información personal, la  información de  cada  usuario  se  debe guardar 
en  una  estructura  de colección  inmutable, luego  mostrar  por  pantalla
la  información  de  los  usuarios agrupada en unaestructura de colección 
mutable.
La información para solicitares:
    a.Nombres y apellidos.
    b.Ocupación.
    c.Edad.
    d.Ciudad.
    e.Número de contacto.
    f.Correo electrónico.
"""

# obteniendo datos de usuarios
user1 = {}
print("Usuario 1:")
nombre = input("Nombres y apellidos:")
ocupacion = input("Ocupacion:")
edad = int(input("Edad:"))
ciudad = input("Ciudad:")
telefono = input("Número de contacto:")
email = input("Correo electrónico:")

# guardando usuario en estructura de datos inmutable
user1 = (nombre,ocupacion,edad,ciudad,telefono,email)

print("Usuario 2:")
nombre = input("Nombres y apellidos:")
ocupacion = input("Ocupacion:")
edad = int(input("Edad:"))
ciudad = input("Ciudad:")
telefono = input("Número de contacto:")
email = input("Correo electrónico:")

# guardando usuario en estructura de datos inmutable
user2 = (nombre,ocupacion,edad,ciudad,telefono,email)

print("Usuario 3:")
nombre = input("Nombres y apellidos:")
ocupacion = input("Ocupacion:")
edad = int(input("Edad:"))
ciudad = input("Ciudad:")
telefono = input("Número de contacto:")
email = input("Correo electrónico:")

# guardando usuario en estructura de datos inmutable
user3 = (nombre,ocupacion,edad,ciudad,telefono,email)

# pasando a una estructura de datos mutable
list_users = list((user1,user2,user3))

# imprimiendo los datos de los usuarios
print("")
print(f"Usuario 1:")
print(f"Nombres y apellidos: {list_users[0][0]}")
print(f"Ocupacion: {list_users[0][1]}")
print(f"Edad: {list_users[0][2]}")
print(f"Ciudad: {list_users[0][3]}")
print(f"Número de contacto: {list_users[0][4]}")
print(f"Correo electrónico: {list_users[0][5]}")

print("")
print("Usuario 2:")
print(f"Nombres y apellidos: {list_users[1][0]}")
print(f"Ocupacion: {list_users[1][1]}")
print(f"Edad: {list_users[1][2]}")
print(f"Ciudad: {list_users[1][3]}")
print(f"Número de contacto: {list_users[1][4]}")
print(f"Correo electrónico: {list_users[1][5]}")

print("")
print("Usuario 3:")
print(f"Nombres y apellidos: {list_users[2][0]}")
print(f"Ocupacion: {list_users[2][1]}")
print(f"Edad: {list_users[2][2]}")
print(f"Ciudad: {list_users[2][3]}")
print(f"Número de contacto: {list_users[2][4]}")
print(f"Correo electrónico: {list_users[2][5]}")