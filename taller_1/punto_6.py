"""
La siguiente matriz (o lista con listas anidadas) debe cumplir que el cuarto 
elemento de cada fila se la suma de los tres primeros elementos de la fila 
respectiva. Si nota las sumas que se encuentran están erróneas, debe modificarlas 
dando 2 soluciones, una con append y otra con slicing.
"""

# matriz a corregir
matriz =[
    [2, 4, 3, 6],
    [8, 3, 4, 5],
    [7, 1, 3, 10],
    [9, 2, 1, 4]
]

### solucion con append ###
matriz_app =[
    [2, 4, 3],
    [8, 3, 4],
    [7, 1, 3],
    [9, 2, 1]
]

# se suma los elementos de la fila y se agrega el resultado al 
# final de cada fila
matriz_app[0].append(sum(matriz_app[0]))
matriz_app[1].append(sum(matriz_app[1]))
matriz_app[2].append(sum(matriz_app[2]))
matriz_app[3].append(sum(matriz_app[3]))

print("Solucion con append: ")
print(matriz_app)

### solucion con slicing ###
matriz[0][3] = sum(matriz[0][:3])
matriz[1][3] = sum(matriz[1][:3])
matriz[2][3] = sum(matriz[2][:3])
matriz[3][3] = sum(matriz[3][:3])

print("Solucion con slicing:")
print(matriz)