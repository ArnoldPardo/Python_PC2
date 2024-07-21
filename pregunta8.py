def factorial(n):
    """Calcula el factorial de un número entero no negativo 'n'."""
    if n < 0:
        return None  # No se puede calcular el factorial de números negativos
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Ejemplos de uso
numero = 5
resultado = factorial(numero)
if resultado is not None:
    print(f"El factorial de {numero} es: {resultado}")
else:
    print("No se puede calcular el factorial de un número negativo.")

