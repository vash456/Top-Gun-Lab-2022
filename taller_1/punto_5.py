""" Programa para calcular la nota media de un estudiante """

print("Calculo de nota media:")
print(" Ingrese 3  notas  y  el  valor porcentual de cada nota")

nota1 = float(input("Nota 1:"))
nota1_por = float(input("Nota 1 porcentaje:"))

nota2 = float(input("Nota 2:"))
nota2_por = float(input("Nota 2 porcentaje:"))

nota3 = float(input("Nota 3:"))
nota3_por = float(input("Nota 3 porcentaje:"))

# calculando nota media
nota_promedio = (nota1*nota1_por + nota2*nota2_por + nota3*nota3_por) / 100

print(f"Nota media: {nota_promedio:.2f}")
