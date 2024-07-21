def convertir_fecha(fecha):
    # Definimos los nombres de los meses en español
    meses = {
        "Enero": "01", "Febrero": "02", "Marzo": "03", "Abril": "04",
        "Mayo": "05", "Junio": "06", "Julio": "07", "Agosto": "08",
        "Septiembre": "09", "Octubre": "10", "Noviembre": "11", "Diciembre": "12"
    }
    
    # Verificamos si la fecha está en el formato mes-día-año (MM/DD/AAAA)
    if '/' in fecha:
        partes = fecha.split('/')
        if len(partes) != 3:
            return "Formato de fecha incorrecto."
        mes = int(partes[0])
        dia = int(partes[1])
        año = int(partes[2])
    else:
        # Verificamos si la fecha está en el formato mes día, año (Septiembre 8, 1636)
        partes = fecha.split()
        if len(partes) != 3:
            return "Formato de fecha incorrecto."
        mes = partes[0]
        dia = int(partes[1].replace(',', ''))
        año = int(partes[2])
    
    # Si el mes es un número, obtener su nombre completo
    if isinstance(mes, int):
        if mes < 1 or mes > 12:
            return "Mes fuera de rango."
        mes_nombre = list(meses.keys())[mes - 1]  # Indices en Python empiezan en 0
        mes_numero = meses[mes_nombre]
    else:
        # Si el mes ya es el nombre completo
        mes_nombre = mes
        mes_numero = meses[mes]
    
    # Formatear la fecha en AAAA-MM-DD
    fecha_iso = f"{año}-{mes_numero.zfill(2)}-{str(dia).zfill(2)}"
    
    return fecha_iso

# Ejemplos de uso
fecha1 = "9/8/1636"
fecha2 = "Septiembre 8, 1636"
fecha3 = "1/1/1970"

print(f"Input: {fecha1} | Output: {convertir_fecha(fecha1)}")
print(f"Input: {fecha2} | Output: {convertir_fecha(fecha2)}")
print(f"Input: {fecha3} | Output: {convertir_fecha(fecha3)}")
