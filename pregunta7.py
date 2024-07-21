def encontrar_numeros_perfectos(maximo):
    numeros_perfectos = []

    # Iteramos sobre cada número hasta el máximo dado
    for numero in range(2, maximo):
        suma_divisores = 1  # Iniciamos la suma con 1 porque 1 siempre es divisor propio

        # Buscamos los divisores propios del número
        for i in range(2, numero):
            if numero % i == 0:
                suma_divisores += i

        # Si la suma de los divisores propios es igual al número, es perfecto
        if suma_divisores == numero:
            numeros_perfectos.append(numero)

    return numeros_perfectos


numeros_perfectos = encontrar_numeros_perfectos(1000)

print("Números perfectos menores que 1000:")
for numero in numeros_perfectos:
    print(numero)
