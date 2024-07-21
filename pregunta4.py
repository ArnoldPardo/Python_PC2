# Función para ingresar los datos de un alumno y sus calificaciones
def ingresar_alumno():
    alumno = input("Ingrese el nombre del alumno: ")
    nota1 = float(input("Ingrese la primera calificación: "))
    nota2 = float(input("Ingrese la segunda calificación: "))
    nota3 = float(input("Ingrese la tercera calificación: "))
    return {'Alumno': alumno, 'Notas': [nota1, nota2, nota3]}

# Lista para almacenar los datos de los alumnos
lista_alumnos = []

# Solicitar al usuario la cantidad de alumnos a ingresar
n = int(input("Ingrese la cantidad de alumnos: "))

# Bucle para ingresar los datos de cada alumno
for i in range(n):
    print(f"Ingresando datos del alumno {i+1}:")
    alumno = ingresar_alumno()
    lista_alumnos.append(alumno)

# Mostrar el listado completo de alumnos y sus calificaciones
print("\nListado completo de alumnos y calificaciones:")
for alumno in lista_alumnos:
    print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")
