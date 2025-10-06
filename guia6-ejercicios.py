# Ejercicio 1: Definir las siguientes funciones y procedimientos:

import numpy as np
import math

# 1)

def imprimir_hola_mundo():
    print("Hola, Mundo!")

imprimir_hola_mundo()

# 2)

def imprimir_un_verso():
    print("If you wanna roll me \nThen you gotta roll me all night long \nAnd if you wanna use me \nThen you gotta use me 'til I'm gone")

imprimir_un_verso()

# 3)
def raizDe2() -> float:
    return(round(math.sqrt(2),4))

print(raizDe2())

# 4)
def factorial_de_dos() ->int:
    return(math.factorial(2))

print( factorial_de_dos())

# 5)
def perimetro() -> float:
    print( 2*math.pi)

perimetro()

# Ejercicio 2: Definir las siguientes funciones y procedimientos con parámetros

# 1)

def imprimir_saludo(nombre: str):
    print("Hola", nombre)

imprimir_saludo("Esteban")

# 2)
def raiz_cuadrada_de(n:float) -> float:
    return (np.sqrt(n))

print(raiz_cuadrada_de(9))

# 3)

def fahrenheit_a_celsius(temp_far:float) -> float:
    return ((temp_far-32)*(5/9))

print(fahrenheit_a_celsius(72))

# 5)
def es_multiplo_de(n:int, m: int) -> bool:
    if n%m == 0:
        return True
    else:
        return False

print(es_multiplo_de(6,4))

# 6)

def es_par(n:int) -> bool:
    return es_multiplo_de(n,2) == True

print(es_par(7))

# 7
def cantidad_de_pizzas(comensales:int, min_cant_de_porciones:int) -> int:
    porciones_pizza:int = 8
    porciones_comidas: int = comensales * min_cant_de_porciones
    res: int = math.ceil((porciones_comidas)/porciones_pizza)
    if(porciones_comidas % porciones_pizza ==0):
        res = res + 1
        print("Para que sobren pedazos de pizza")
    else:
        res=res
    return res

print("La cantidad de pizzas necesarias para que todos coman es:", cantidad_de_pizzas(8,3))
