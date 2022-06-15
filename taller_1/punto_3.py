"""Programa para pasar de Fahrenheit a grados centigrados"""


fahrenheit = float(input("Ingrese los grados Fahrenheit:"))

# convirtiendo de Fahrenheit a grados centigrados
centigrados = (fahrenheit-32) * (5/9)

print(f"Grados centigrados: {centigrados:.4f} °C")
