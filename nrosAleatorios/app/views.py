from django.shortcuts import render

# Create your views here.
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
    
def congruencia_fundamental(a,c,K_Congruencias,m,n,numeros_fibonacci):
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
        # Creamos un Array auxiliar de K para el método con la secuencia Fibonacci
        aux = numeros_fibonacci
                       
        # Ejecutamos el metodo de congruencia fundamental
        list = []
        for i in range(n):
            nro = ((a * aux[i-1] + c * aux[i-K_Congruencias]) % m)
            list.append(nro)
            
        # Retornamos el listado de numeros aleatorios
        return(list)