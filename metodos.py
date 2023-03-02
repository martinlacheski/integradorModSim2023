import collections
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import nbformat
import math
from scipy.stats import chi2, chisquare
from scipy.interpolate import interp1d
from datetime import datetime, timedelta

def fibonacci(v1,v2,K,n):
    if v1 < 0:
        print('Valor inválido v1, tiene que ser mayor que CERO')
    elif v2 < 0:
        print('Valor inválido de v2, tiene que ser mayor que CERO')
    elif v2 < v1:
        print('Valor inválido, v2 es menor que v1')
    elif K < 0:
        print('Valor inválido de K para Fibonacci, tiene que ser mayor que CERO')
    else:
        list = []
        list.append(v1)
        list.append(v2)
        for i in range(n):
            if (v1 + v2) <= K:
                total = v1 + v2 + (0 * K)
            else:    
                total = v1 + v2 + (-1 * K)
                
            # Reasignamos las variables
            
            v1 = v2
            v2 = total
            
            # Agregamos el numero nuevo
            
            list.append(total)

        # Retornamos el listado de numeros aleatorios concatenados 
        
        return(list)    

def congruencia_fundamental(numeros_fibonacci, a, c, K_Congruencias, m, n, marcas_clase, probabilidades):
    if a <= 0:
        print('Valor inválido de A, tiene que ser mayor que CERO')
    elif c <= 0:
        print('Valor inválido de C, tiene que ser mayor que CERO')
    elif m <= 0:
        print('Valor inválido de M, tiene que ser mayor que CERO')    
    elif m < a:
        print('Valor inválido, M debe ser mayor que A')
    elif K_Congruencias < 0:
        print('Valor invalido de K para congruencias, tiene que ser mayor que CERO')
    else:
        list = []
        for i in range(n):
            nro = ((a * numeros_fibonacci[i-1] + c * numeros_fibonacci[i-K_Congruencias]) % m)
            acum_prob = 0
            for j in range(len(marcas_clase)):
                prob = probabilidades[j]
                acum_prob += prob
                if nro/m < acum_prob:
                    minimo = marcas_clase[j][0]
                    maximo = marcas_clase[j][1]
                    numero_aleatorio = minimo + nro % (maximo - minimo + 1)
                    list.append(int(numero_aleatorio))
                    break
        return list
       
def test_poker(numeros, minimo, maximo):
   
    a = 0
    i = 0
    grupos = []
    tipos = [0, 0, 0, 0, 0, 0, 0]
    cant_grupos = len(numeros) // 5

    # Agrupamos de a 5 elementos
    while a < cant_grupos:
        grupo = []
        for j in range(5):
            grupo.append((numeros[i] - minimo) / (maximo - minimo))
            i += 1
        grupos.append(grupo)
        a += 1

    # Clasificamos los grupos (obtener frecuencia observada)
    for item in grupos:
        apariciones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        valor = 1

        for i in range(10):
            apariciones[i] += item.count(i)

        for i in range(10):
            if apariciones[i] > 0:
                valor = valor * apariciones[i]

        if valor == 1:
            tipos[0] += 1
        elif valor == 2:
            tipos[1] += 1
        elif valor == 3:
            tipos[3] += 1
        elif valor == 4:
            if 4 in apariciones:
                tipos[5] += 1
            else:
                tipos[2] += 1
        elif valor == 5:
            tipos[6] += 1
        elif valor == 6:
            tipos[4] += 1
        else:
            return "error"

    # Calculo de fe
    fe = [0, 0, 0, 0, 0, 0, 0]
    fe[0] = cant_grupos * 0.3024
    fe[1] = cant_grupos * 0.504
    fe[2] = cant_grupos * 0.108
    fe[3] = cant_grupos * 0.072
    fe[4] = cant_grupos * 0.009
    fe[5] = cant_grupos * 0.0045
    fe[6] = cant_grupos * 0.0001

    # Calculo de x0
    x0 = 0
    for i in range(7):
        x0 += ((fe[i] - tipos[i]) ** 2) / fe[i]

    return x0

def res_test_poker(numeros, resultado, confianza):
    
    grados_libertad = len(numeros) - 1

    valor_chi2 = chi2.ppf(confianza, grados_libertad)
        
    if valor_chi2 > resultado:
        print(f'{resultado} < {valor_chi2}\n')
        print(f'El resultado del test de Poker para Fibonacci + Congruencia Fundamental es VERDADERO para {confianza} de confianza y {grados_libertad} grados de libertad \n')
    else:
        print(f'{resultado} > {valor_chi2}\n')
        print(f'El resultado del test de Poker para Fibonacci + Congruencia Fundamental es FALSO para {confianza} de confianza y {grados_libertad} grados de libertad \n')
        
def test_jicuadrado(numeros):
    x0 = 0
    fi = [0] * (max(numeros) - min(numeros) + 1)

    # Cálculo de fi
    for item in numeros:
        fi[item - min(numeros)] += 1

    # Cálculo de npi
    npi = len(numeros) / len(fi)

    # Cálculo de x0
    for i in range(len(fi)):
        x0 += ((fi[i] - npi) ** 2) / npi

    return x0

def res_test_chi(numeros, resultado, confianza): 

    grados_libertad = len(numeros) - 1

    valor_chi2 = chi2.ppf(1 - confianza, grados_libertad)
                
    #Comparamos si el resultado es menor o mayor al correspondiente en la tabla
    
    if (valor_chi2 > resultado ):
        print(f'{resultado} < {valor_chi2}\n')
        print(f'El resultado del test de Ji Cuadrado para Fibonacci + Congruencia Fundamental es VERDADERO para {confianza} de confianza y {grados_libertad} grados de libertad\n')
        return
    else:
        print(f'{resultado} > {valor_chi2}\n')
        print(f'El resultado del test de Ji Cuadrado para Fibonacci + Congruencia Fundamental es FALSO para {confianza} de confianza y {grados_libertad} grados de libertad\n')
        return

def distribucion_bernoulli(numeros, minimo, maximo):
    
    mitad = (maximo + minimo) / 2
    
    valores = np.array(numeros)
    
    binarios = np.where(valores >= mitad, 1, 0)
    
    return binarios

def distribucion_bernoulli_grafico(distribucion):
    
    # Usamos plotly para hacer un diagrama de barras interactivo con la distribución de los datos

    # Contamos los valores CERO y UNO

    datos = {}

    for valor in distribucion:
        if valor in datos:
            datos[valor] += 1
        else:
            datos[valor] = 1
            
    print(f'Distribucion de los datos: {datos}\n')

    fig = go.Figure(data=[go.Pie(labels=list(datos.keys()), values=list(datos.values()))])
    fig.show()

def distribucion_normal(numeros):
    # Utilizamos los numeros aleatorios obtenidos por la congruencia fundamental

    datos = np.array(numeros)

    # Calculamos la media y la desviación estándar

    mu = np.mean(numeros)

    print(f'la media es: {mu}\n')

    sigma = np.std(datos)

    print(f'la desviación estandar es: {sigma}\n')

    # Creamos un rango de valores x para la distribución normal

    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)

    # Calculamos la distribución normal para los valores x

    y = (1/(sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu)/sigma)**2)

    # Creamos un histograma de los datos

    n, bins, patches = plt.hist(datos, bins=10, density=True, color='lightblue', alpha=0.5)

    # Creamos la curva de distribución normal

    plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
            np.exp(- (bins - mu)**2 / (2 * sigma**2)),
            linewidth=2, color='red')

    # Configuramos la leyenda

    plt.legend(['Distribución normal', 'Frecuencia Observada'])

    # Mostramos el gráfico
    plt.show()


def simulacion(muestrasHumedadRelativa, numeros_congruencia, marcas_clase):
    print(f'Las variaciones de humedad relativa observadas son:\n{muestrasHumedadRelativa}\n')

    print(f'Las variaciones de humedad relativa con la muestra de numeros pseudoaleatorios generados artificialmente son:\n{numeros_congruencia}\n')

    print(f'Las cantidad de muestras de humedad relativa artificial son: {len(muestrasHumedadRelativa)}\n')

    # Generamos las marcas de clases

    num_marcas = len(marcas_clase) # 184 posibles valores / 6 = 30,67 valores por cada muestra

    # Generamos los datos de frecuencias esperadas para el grafico segun los datos recolectados

    # Obtenemos la amplitud total (184)

    amplitud_total = max(muestrasHumedadRelativa) - min(muestrasHumedadRelativa)

    print(f'La amplitud total es: {amplitud_total}\n')

    print(f'Donde el valor minimo es: {min(muestrasHumedadRelativa)} y el valor maximo es {max(muestrasHumedadRelativa)}\n')

    # Obtenemos la amplitud por cada muestra (17)
    amplitud_marcas = amplitud_total / num_marcas

    limites_inferiores = [min(muestrasHumedadRelativa) + i * amplitud_marcas for i in range(num_marcas)]

    limites_superiores = [limite + amplitud_marcas for limite in limites_inferiores]

    marcas_clase = []
    frecuencia_esperada = []
    frecuencia_observada = []

    for i in range(num_marcas):
        valores_en_marca = [dato for dato in muestrasHumedadRelativa if limites_inferiores[i] <= dato <= limites_superiores[i]]
        frecuencia_esp = len(valores_en_marca)
        probabilidad_esp = frecuencia_esp / len(muestrasHumedadRelativa)
        valores_en_marca = [dato for dato in numeros_congruencia if limites_inferiores[i] <= dato <= limites_superiores[i]]
        frecuencia_obs = len(valores_en_marca)
        probabilidad_obs = frecuencia_obs / len(muestrasHumedadRelativa)
        print(f"Marca {i+1} - Rango Inferior - Superior: [{round(limites_inferiores[i],2)}, {round(limites_superiores[i],2)}] - Frecuencia Esperada: {frecuencia_esp} - Frecuencia Observada: {frecuencia_obs} - Probabilidad Esperada: {round(probabilidad_esp,5)} - Probabilidad Observada: {round(probabilidad_obs,5)}")
        marcas_clase.append(i+1)
        frecuencia_esperada.append(frecuencia_esp)
        frecuencia_observada.append(frecuencia_obs)
    
    plt.plot(marcas_clase, frecuencia_observada, color='blue')
    plt.plot(marcas_clase, frecuencia_esperada, color='red')

    # Configuramos la leyenda
    plt.legend(['Frecuencia Esperada', 'Frecuencia Observada'])
    plt.show()
    
def clasificar_numeros(numeros, marcas_clase):
    clasificacion = []
    for num in numeros:
        for i in range(len(marcas_clase)):
            if num >= marcas_clase[i][0] and num <= marcas_clase[i][1]:
                clasificacion.append(i+1)
                break
    return clasificacion

def curva_array(array_original, array_pseudoaleatorio):    
    array_final = []
    for elem in array_pseudoaleatorio:
        closest_val = None
        closest_dist = float('inf')
        for val in array_original:
            dist = abs(val - elem)
            if dist < closest_dist:
                closest_val = val
                closest_dist = dist
        array_final.append(closest_val)
    return array_final
    
def generacion_nueva_hum_rel(fecha_inicial, hum_rel_inicial, numeros):
    humedades = []
    fecha = datetime.strptime(fecha_inicial, '%Y-%m-%d')
    for i in range(1, len(numeros)):
        # Obtenemos la diferencia de la posicion
        diferencia = int(numeros[i][1])
        hum = hum_rel_inicial - diferencia 
        humedades.append((fecha.strftime('%Y-%m-%d'), hum))
        fecha += timedelta(days=1)
    return humedades

def calcular_valores_humedad(hum_rel_inicial, valores):
    resultado = []
    hum = hum_rel_inicial
    for diferencia in valores:
        hum = hum + diferencia
        resultado.append(hum)
    return resultado

def calcular_nuevos_valores_humedad(hum_rel_inicial, valores):
    resultado = []
    hum = hum_rel_inicial
    for diferencia in valores:
        hum = hum + diferencia
        if hum > 100:
            hum = 100 - (hum - 100)
        elif hum < 0:
            hum = -hum
        resultado.append(hum)
    return resultado

def escribir_humedad_relativa_simulada(fecha_inicio, humedadesNvas):
    fecha = datetime.strptime(fecha_inicio, '%Y-%m-%d').date()
    with open("datos_generados_nvas_humedades.txt", "w") as outfile:
        for humedad in humedadesNvas:
            outfile.write(str(fecha) + ',' + str(humedad) + '\n')
            fecha += timedelta(days=1)