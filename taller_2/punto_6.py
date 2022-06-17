"""
Dadas dos listas, se debe crear un programa que genere una tercera lista  con  
los  elementos  que  se  repiten  en  las  dos  anteriores  listas sin repetirse 
ningún elemento en la nueva lista.
    Lista 1: [‘h’, ‘e’, ‘l’, ‘l’, ‘o’, ‘ ‘, ‘t’, ‘e’, ‘a’, ‘m’]
    Lista 2: [‘h’, ‘e’, ‘l’, ‘l’, ‘o’, ‘ ‘, ‘w’, ‘o’, ‘r’, ‘l’, ‘d’]
"""

# iniciando las listas
lista_1 = ["h", "e", "l", "l", "o", " ", "t", "e", "a", "m"]
lista_2 = ["h", "e", "l", "l", "o", " ", "w", "o", "r", "l", "d"]
lista_3 = []

# creando copia de las listas
lista_1_aux = lista_1.copy()
lista_2_aux = lista_2.copy()

# organizando los elementos de la listas
lista_1_aux.sort()
lista_2_aux.sort()

# comparando un elemento con el siguiente y agregando los repetidos en la lista_3
for i in range(len(lista_1_aux)):
    if (i+1) < len(lista_1_aux):
        if lista_1_aux[i] == lista_1_aux[i+1]:
            posicion = lista_1_aux.index(lista_1_aux[i])
            lista_3.append(lista_1_aux.pop(posicion))

for i in range(len(lista_2_aux)):
    if (i+1) < len(lista_2_aux):
        if lista_2_aux[i] == lista_2_aux[i+1]:
            posicion = lista_2_aux.index(lista_2_aux[i])
            lista_3.append(lista_2_aux.pop(posicion))

for i in range(len(lista_3)):
    if (i+1) < len(lista_3):
        if lista_3[i] == lista_3[i+1]:
            posicion = lista_3.index(lista_3[i])
            lista_3.pop(posicion)

print(f"Lista 1: {lista_1}")
print(f"Lista 2: {lista_2}")
print(f"Lista 3: {lista_3}")