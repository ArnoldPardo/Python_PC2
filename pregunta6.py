# Inicializar los primeros dos números de la serie de Fibonacci
a, b = 0, 1

# Imprimir el primer número de la serie de Fibonacci (que es 0)
print(a)

# Generar y mostrar los siguientes números de la serie de Fibonacci hasta llegar a 50
while b <= 50:
    print(b)
    a, b = b, a + b
