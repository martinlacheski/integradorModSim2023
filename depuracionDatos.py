import os
from datetime import datetime

# Obtener la ruta del directorio actual
current_dir = os.getcwd()

# Unir la ruta del directorio actual con el nombre de la carpeta "datos"
directory = os.path.join(current_dir, 'datos')

# Nombre del archivo de salida de humedad de posadas
output_file_historico = 'datos_extraidos_humedad.txt'

# Nombre del archivo de salida de promedios de humedad por dia
output_file_promedio = 'datos_extraidos_promedios_humedad.txt'

# Nombre del archivo de salida de diferencia de humedad por dia con respecto del dia anterior
output_file_diferencia = 'datos_extraidos_diferencia_humedad.txt'

# Función para convertir el formato de fecha str a datetime
def str_to_date(fecha):
    return datetime.strptime(fecha[0], '%Y-%m-%d')

# Creamos una lista de tuplas con la fecha, hora, humedad y Localidad y los valores necesarios
data = []

# Abrimos el archivo de salida en modo escritura
with open(output_file_historico, 'w') as outfile:
    # Iteramos sobre cada archivo de texto en el directorio
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            # Intentamos abrir el archivo de texto actual con la codificación "ISO-8859-1"
            try:
                with open(os.path.join(directory, filename), 'r', encoding='ISO-8859-1') as infile:
                    lines = infile.readlines()
            except UnicodeDecodeError:
                # Si falla, intentamos abrir el archivo con la codificación "Windows-1252"
                with open(os.path.join(directory, filename), 'r', encoding='Windows-1252') as infile:
                    lines = infile.readlines()

            # Iteramos sobre cada línea
            for line in lines:
                
                # Separamos la línea por espacios en blanco
                values = line.strip().split()

                # Verificamos que hay suficientes valores en la lista
                if len(values) >= 8:
                    # Extraemos los valores necesarios
                    fechaSTR = values[0]
                    fecha = datetime.strptime(fechaSTR, '%d%m%Y').strftime('%Y-%m-%d')
                    hora = values[1]
                    hum = values[3]
                    nombre = values[7]
                    
                    # Comprobamos si el valor de NOMBRE es igual a "POSADAS" y de ser asi guardamos al listado
                    if nombre.strip() == "POSADAS":
                        data.append((fecha, hora, hum, nombre))                  
            
                    
    # Ordenamos la lista por fecha        
    data_ordenada = sorted(data, key=lambda x: x[0])
                                    
    # Escribimos los valores ordenados en el archivo de salida
    for fecha, hora, hum, nombre in data_ordenada:
        outfile.write(fecha + ',' + hora + ',' +  hum + ',' +  nombre + '\n')
        

# Creamos un diccionario vacío para almacenar los valores de humedad por fecha
hum_por_fecha = {}

# Iteramos sobre la lista de datos y agregar los valores de humedad al diccionario
for fecha, hora, hum, nombre in data_ordenada:
    if fecha not in hum_por_fecha:
        # Inicializamos la suma de hum y el contador en 0
        hum_por_fecha[fecha] = [0, 0]  
        
    hum_por_fecha[fecha][0] += float(hum)
    hum_por_fecha[fecha][1] += 1

# Calculamos el promedio de humedad para cada fecha
promedios_hum = []

for fecha, (suma_hum, contador) in hum_por_fecha.items():
    promedio = round(suma_hum / contador,0)
    promedios_hum.append((fecha, promedio))


# Abrimos el archivo de salida en modo escritura
with open(output_file_promedio, 'w') as outfile:
    # Escribir los valores ordenados en el archivo de salida
    for fecha, promedio in promedios_hum:
        outfile.write(fecha + ',' + str(promedio) + '\n')

# Generamos la diferencia de Humedad entre los dias para poder obtener los datos necesarios para generar los numeros pseudoaleatorios

diferencias_hum = []

# Guarda el primer promedio como valor anterior

anterior = promedios_hum[0][1]  

# Iteramos sobre los demás promedios

#for fecha, promedio in promedios_hum[1:]:  
    
    # Calculamos la diferencia
    
    #diferencia = promedio - anterior  
    
    # Guardamos la fecha y la diferencia en la lista
    #diferencias_hum.append((fecha, diferencia))  
    
    # Actualizamos el valor anterior con el promedio actual
    #anterior = promedio  

# Generamos una nueva lista para almacenar las diferencias de Humedad
diferencias = []

# Iteramos para sacar las diferencias (Notese que empezamos desde la posicion UNO y no CERO porque nos interesa saber a partir del mes de JULIO)
for i in range(1, len(promedios_hum)):
    
    # Obtenemos la Fecha de la posicion
    fecha_actual = promedios_hum[i][0]
    
    #Realizamos la diferencia de humedad entre la fecha actual y la fecha anterior
    diferencia = int(promedios_hum[i][1]) - int(promedios_hum[i-1][1])
    #print(f'{fecha_actual} : {(promedios_hum[i][1])} - {(promedios_hum[i-1][1])} = {diferencia} ')
    
    #Agregamos la diferencia a la lista
    diferencias.append((fecha_actual, diferencia))

# Abrimos el archivo de salida en modo escritura
with open(output_file_diferencia, 'w') as outfile:
    # Escribir los valores ordenados en el archivo de salida
    for fecha_actual, diferencia in diferencias:
        outfile.write(fecha_actual + ',' + str(diferencia) + '\n')