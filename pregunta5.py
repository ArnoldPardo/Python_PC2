
def es_primo(num):
    if num <= 1:
        return False
    if num == 2:
        return True  # 2 es primo
    if num % 2 == 0:
        return False  # Los números pares mayores que 2 no son primos
    
    # Verificar divisibilidad desde 3 hasta la raíz cuadrada de num
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2  # Solo verificar números impares (optimización)
    
    return True

# Inicializar la suma de los números primos menores que 100
suma_primos = 0


for numero in range(2, 100):
    if es_primo(numero):
        suma_primos += numero


print(f"La suma de todos los números primos menores que 100 es: {suma_primos}")
