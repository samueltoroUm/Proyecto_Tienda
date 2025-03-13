
import random
import math

def es_inteligente(num):
    """un numero es inteligente si es un cuadrado perfecto"""
    raiz = math.isqrt(num)  # calcular raiz cuadrasda
    return raiz * raiz == num #profe utilice este algoritmo pq segun busque un numero es un numero inteligente si es un cuadrado perfecto 

cantidad = int(input("ingrese la cantidad de números a validar: "))

numeros = [random.randint(1, 100) for _ in range(cantidad)]


print("numeros generados:", ", ".join(map(str, numeros)))

for num in numeros:
    print(f"{num}: {'Si' if es_inteligente(num) else 'No'}")