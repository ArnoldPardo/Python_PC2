
numeros_cumplen_condicion = []

# Iteramos sobre el rango de 1500 a 2700 (ambos incluidos)
for num in range(1500, 2701):
    # Verificamos si el número es divisible por 7 y múltiplo de 5
    if num % 7 == 0 and num % 5 == 0:
        # Si cumple las condiciones, lo agregamos a la lista
        numeros_cumplen_condicion.append(num)

# Mostramos los números que cumplen las condiciones
print("Los números que son divisibles por 7 y múltiplos de 5 en el rango de 1500 a 2700 son:")
print(numeros_cumplen_condicion)
