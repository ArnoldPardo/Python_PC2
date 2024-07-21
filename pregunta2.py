
num_filas = 5

# Parte superior del patrón (líneas ascendentes)
for i in range(1, num_filas + 1):
    # Imprime i asteriscos en cada línea
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# Parte inferior del patrón (líneas descendentes)
for i in range(num_filas - 1, 0, -1):
    # Imprime i asteriscos en cada línea
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
