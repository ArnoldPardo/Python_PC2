def omitir_vocales(cadena):
    # Definimos las vocales a omitir en forma de conjunto para una búsqueda eficiente
    vocales = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    
    # Inicializamos una lista para almacenar los caracteres modificados
    resultado = []
    
    # Iteramos sobre cada carácter en la cadena
    for caracter in cadena:
        # Si el carácter no está en el conjunto de vocales, lo añadimos al resultado
        if caracter not in vocales:
            resultado.append(caracter)
    
    # Convertimos la lista de caracteres resultante de vuelta a una cadena y la devolvemos
    return ''.join(resultado)

# Solicitar al usuario que ingrese una cadena de texto
entrada = input("Ingrese una cadena de texto: ")

# Aplicar la función para omitir las vocales y mostrar el resultado
resultado = omitir_vocales(entrada)
print(f"Texto sin vocales: {resultado}")
