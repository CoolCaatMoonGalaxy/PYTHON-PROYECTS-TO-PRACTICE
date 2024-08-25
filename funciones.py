#Basicas

"""Sumas"""
def sumar(a, b):
    return a + b
"""Numeros pares"""
def es_par(num):
    return num % 2 == 0

print(es_par(4))  # Salida: True
print(es_par(7))  # Salida: False



print(sumar(5, 3))  # Salida: 8

"""Cadenas"""
def contar_caracteres(cadena):
    return len(cadena)

print(contar_caracteres("Hola Mundo"))  # Salida: 10

#intermedias 
"""Encontrar el maximo de una lista de numeros"""
def maximo(lista):
    return max(lista)

print(maximo([1, 3, 5, 2, 4]))  # Salida: 5

"""Función para calcular la suma de los números en una lista usando recursión"""
def suma_lista(lista):
    if not lista:
        return 0
    return lista[0] + suma_lista(lista[1:])

print(suma_lista([1, 2, 3, 4]))  # Salida: 10

"""Función para generar una lista de números pares hasta un límite dado"""
def pares_hasta(n):
    return [i for i in range(n) if i % 2 == 0]

print(pares_hasta(10))  # Salida: [0, 2, 4, 6, 8]

#Avanzado

"""Función para calcular el factorial de un número usando memoización:"""
def factorial(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return 1
    memo[n] = n * factorial(n - 1, memo)
    return memo[n]

print(factorial(5))  # Salida: 120

"""Función para realizar una búsqueda binaria en una lista ordenada"""
def busqueda_binaria(lista, objetivo):
    bajo, alto = 0, len(lista) - 1
    while bajo <= alto:
        medio = (bajo + alto) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    return -1

print(busqueda_binaria([1, 2, 3, 4, 5, 6], 4))  # Salida: 3

"""Listas conversion a un diccionario"""
def combinar_listas(keys, values):
    return [{keys[i]: values[i]} for i in range(len(keys))]

print(combinar_listas(['a', 'b', 'c'], [1, 2, 3]))  # Salida: [{'a': 1}, {'b': 2}, {'c': 3}]
