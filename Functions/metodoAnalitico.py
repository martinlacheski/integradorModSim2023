############### LIBRERIAS #################

import numpy as np

############### VARIABLES #################
#Variables Fibonacci

# primer parametro es "v1" que es el valor 1, 
v1 = 23

# para provocar falso
#v1 = 1

# segundo parametro "v2" que es el valor 2,
v2 = 67

# para provocar falso
#v2 = 4

# tercer parametro es "K" y que es requerido por la funcion para "(v1 + v2) <= K"
K_Fibonacci = 177

#Variables Congruencias Fundamental

# primer parametro es "a" que multiplica a Vi, 
a = 1

# segundo parametro "c" que multiplica a Vi-k, 
c = 2

# para provocar falso
# c = 4 # Falso test de Poker
# c = 3 # Falso test de Chi

# tercer parametro es "K" que es la cantidad de espacios a crear antes de los nros aleatorios
K_Congruencias = 16

# cuarto parametro es "m" que es el tope de numeros a generar
m = 10

# En Fibonacci y Congruencias el parametro "n" es la cantidad de numeros que queremos generar
n = 100

indice_chisquare = [0.001, 0.0025, 0.005, 0.01, 0.025, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 
                    0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 0.975, 0.99, 0.995, 0.9975, 0.999]

tabla_chisquare_test_poker = [22.4575, 20.2491, 18.5475, 16.8119, 14.4494, 12.5916, 10.6446, 9.4461, 8.5581, 
                              7.8408, 7.2311, 6.6948, 6.2108, 5.7652, 5.3481, 4.9519, 4.5702, 4.1973, 3.8276, 3.4546,
                               3.0701, 2.6613, 2.2041, 1.6354, 1.2373, 0.8721, 0.6757, 0.5266, 0.3810]

tabla_chisquare_test_chi = [27.8767, 25.462527, 23.5893, 21.6660, 19.0228, 16.9190, 14.6837, 13.2880, 12.2421, 
                            11.3887, 10.6564, 10.0060, 9.4136, 8.8632, 8.3428, 7.8434, 7.3570, 6.8763, 6.3933, 5.8988, 
                            5.3801, 4.8165, 4.1682, 3.3251, 2.7004, 2.0879, 1.7349, 1.4501, 1.1519]

confianza = 0.5                            

############### FUNCIONES #################

#Definimos la funcion para generar los numeros aleatorios de Fibonacci donde:

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
                
            #Reasignamos las variables
            v1 = v2
            v2 = total
            
            #agregamos el numero nuevo
            list.append(total)

        #retornamos el listado de numeros aleatorios concatenados 
        return(list)

#Definimos la funcion para generar los numeros aleatorios mediante la Congruencia fundamental y utilizando la serie de Fibonacci donde:

def congruencia_fundamental(a,c,K,m,n):
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
        #Creamos un Array auxiliar de K para el método con la secuencia Fibonacci
        aux = numeros_fibonacci
                       
        #Ejecutamos el metodo de congruencia fundamental
        list = []
        for i in range(n):
            nro = ((a * aux[i-1] + c * aux[i-K_Congruencias]) % m)
            list.append(nro)
            
        #retornamos el listado de numeros aleatorios
        return(list)

#Definimos la funcion para realizar el test de Poker

def test_poker(nros):
    # Test poker
    a = 0
    i = 0
    grupos = []
    tipos = [0, 0, 0, 0, 0, 0, 0]
    cant_grupos = len(nros) // 5

    # Agrupar de a 5 elementos
    while a < cant_grupos:
        grupos.append(nros[i:i + 5])
        a += 1
        i += 5

    # Clasificar grupos (obtener frecuencia observada)
    for item in grupos:
        apariciones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        valor = 1

        for i in range(10):
            apariciones[i] += str(item).count(str(i))

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

#Definimos la funcion para realizar el test de Ji Cuadrado

def test_jicuadrado(nros):

    x0 = 0
    fi = [0]*10

    # Cálculo de fi
    for item in nros:
        fi[item] += 1

    # Cálculo de npi
    npi = len(nros)/10

    '''
    fi = [7, 4, 5, 7, 4, 5, 4, 9, 5, 5]
    npi = 5.5
    '''

    # Cálculo de x0
    for i in range(len(fi)):
        x0 += ((fi[i] - npi)*(fi[i] - npi)) / npi

    return x0

# Definimos la funcion para validar si aprobo o no el test de Poker

def res_test_poker(resultado):
    i = 0
    
    #Buscamos el valor del indice segun el valor de confianza
    for i in range(len(indice_chisquare)):
        if confianza == indice_chisquare[i]:
            indiceJI = tabla_chisquare_test_poker[i]
            break
    
    #Comparamos si el resultado es menor o mayor al correspondiente en la tabla
    if tabla_chisquare_test_poker[i] > resultado :
        print(f"{resultado} < {indiceJI}")
        print('El resultado del test de Poker para Fibonacci + Congruencia Fundamental es VERDADERO')
        return
    else:
        print(f"{resultado} > {indiceJI}")
        print('El resultado del test de Poker para Fibonacci + Congruencia Fundamental es FALSO')
        return

# Definimos la funcion para validar si aprobo o no el test de Ji Cuadrado

def res_test_chi(resultado):
    i = 0
    
    #Buscamos el valor del indice segun el valor de confianza
    for i in range(len(indice_chisquare)):
        if confianza == indice_chisquare[i]:
            indiceJI = tabla_chisquare_test_chi[i]
            break
            
    #Comparamos si el resultado es menor o mayor al correspondiente en la tabla
    if (tabla_chisquare_test_chi[i] > resultado ):
        print(f"{resultado} < {indiceJI}")
        print('El resultado del test de Ji Cuadrado para Fibonacci + Congruencia Fundamental es VERDADERO')
        return
    else:
        print(f"{resultado} > {indiceJI}")
        print('El resultado del test de Ji Cuadrado para Fibonacci + Congruencia Fundamental es FALSO')
        return

# Definimos una funcion para convertir los numeros aleatorios en CERO y UNO para poder aplicar la Distribucion de Bernoulli

def distribucion_bernoulli(numeros):
    binarios = np.where(numeros >= 5, 1, 0)
    return binarios


############### EJECUCIONES #################

#Generamos el listado de numeros aleatorios aplicando Fibonacci

numeros_fibonacci = fibonacci(v1,v2,K_Fibonacci,n)

#Imprimos el array de fibonacci
print('Listado de numeros aleatorios aplicando Fibonacci:')
print(numeros_fibonacci)

#Generamos el listado de numeros aleatorios aplicando Congruencia Fundamental

numeros_congruencia = congruencia_fundamental(a,c,K_Congruencias,m,n)

print('Listado de numeros aleatorios aplicando Congruencia Fundamental:')
print(numeros_congruencia)

# Generamos el Test de Poker para los numeros aleatorios aplicando Congruencia Fundamental

# Se genera la impresion de los resultados en la funcion

resultado = test_poker(numeros_congruencia)

# Se genera la impresion de los resultados en la funcion

resultadoTest = res_test_poker(resultado)

# Generamos el Test de Ji Cuadrado para los numeros aleatorios aplicando Congruencia Fundamental

# Se genera la impresion de los resultados en la funcion

resultado = test_jicuadrado(numeros_congruencia)

# Se genera la impresion de los resultados en la funcion

resultadoTest = res_test_chi(resultado)

# Generamos la distribucion de Bernoulli sobre los numeros aleatorios

distribucion = distribucion_bernoulli

print(distribucion)