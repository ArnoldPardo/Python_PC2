# Inicializamos una lista para almacenar los números ingresados
numeros_ingresados = []
contador_pares = 0
contador_impares = 0

# Variable para controlar el bucle
continuar = True

while continuar:
    respuesta = input("¿Desea ingresar un número? (SI/NO): ")
    
    if respuesta.upper() == 'SI':
        try:
            numero = int(input("Ingrese el número: "))
            numeros_ingresados.append(numero)
            
            if numero % 2 == 0:
                contador_pares += 1
            else:
                contador_impares += 1
                
        except ValueError:
            print("Error: Debes ingresar un número entero.")
    
    elif respuesta.upper() == 'NO':
        continuar = False
        
    else:
        print("Respuesta inválida. Por favor, responda con 'SI' o 'NO'.")

# Mostrar resultados
print(f"Números ingresados: {numeros_ingresados}")
print(f"Cantidad de números pares: {contador_pares}")
print(f"Cantidad de números impares: {contador_impares}")

