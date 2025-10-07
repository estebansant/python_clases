# Para activar el ambiente de desarrollo hacer: source ruta/bin/activate

import math
import numpy as np

def imprimir_hola_mundo():
    print("Hola, Mundo!")

imprimir_hola_mundo() 

print(math.sqrt(3))
print(np.sqrt(3))

print(math.ceil(9.2345215))
print(math.floor(9.2345215))
print(math.floor(9.6345215))
print(np.pi)

def perimetro() -> float:
    print( 2*math.pi)

perimetro()

def area_circulo(radio:float) -> float:
    return (2*np.pi*radio)

print("el area del circulo es:", area_circulo(2))

def volumen_esfera(r:float)->float:
    return((r**3)*(np.pi*4)/3)

print("el volumen de la esfera es:", volumen_esfera(3))

# Ejercicio 2: Es multiplo de

def es_multiplo_de(n:int, m: int) -> bool:
    if n%m == 0:
        return True
    else:
        return False

print(es_multiplo_de(6,4))

# Ejercicio 3: Es nombre largo

def es_nombre_largo(nombre: str) -> bool:
    return (3 <= len(nombre) and len(nombre) <= 8)

print(es_nombre_largo("Juan"))

#  Ejercicio 5

def devolver_el_doble_si_es_par(n:int)->int:
    if n%2==0:
        res: int= n*2
    else:
        res: int = n
    return res

print(devolver_el_doble_si_es_par(40))

# Ejercicio 6

def pares_entre_10_40() -> None:
    cont: int = 10
    while cont <=40:
        if cont%2==0:
            print(cont)
            cont +=1
        else:
            cont +=1

pares_entre_10_40()
