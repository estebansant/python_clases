# Pilas y Colas
from queue import Queue as Cola
from queue import LifoQueue as Pila
import random

# Ejercicio 6.4

def ordenados(s:list[int]) -> bool:
    res: bool = True
    for i in range(0,len(s)-1,1):
        if (s[i]< s[i+1]) == False:
            res = False
    return res

print(ordenados([10,11,12,13,14]))

def devuelve_columna(m: list[list[int]], c: int) -> list[int]:
    res: list[int] = []
    for i in range(len(m)):
        res.append(m[i][c])
    return res

print(devuelve_columna([
    [1,2,2,3,4],
    [2,3,1000,1,7],
    [9,8,7,4,8],
    [1,2,3,4,10],
    [8,9,10,20,30]
], -1))

def columnas_ordenadas(m: list[list[int]]) -> list[bool]:
    res: list[bool]=[]
    for c in range(0,len(m[0]),1):
        columna: list[int] = devuelve_columna(m,c)
        if (ordenados(columna)):
            res.append(True)
        else:
            res.append(False)
    return res

print(columnas_ordenadas([
    [1,2,2,3,4],
    [2,3,1000,1,7],
    [9,8,7,4,8],
    [1,2,3,4,10],
    [8,9,10,20,30]
]))

# Ejercicio 1 de Colas

def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Cola[int]:
    res = Cola()
    while (cantidad>0):
        num: int = random.randint(desde,hasta)
        res.put(num)
        cantidad -= 1
    return res

numeros = generar_nros_al_azar(10, 0, 10)
azar = []  # Para almacenar los números extraídos de la cola

# Extraemos los números de la cola
while not numeros.empty():
    azar.append(numeros.get())  # Usamos .get() para sacar elementos de la cola

print("Numeros al azar:", azar) 

# Ejercicio 2 de Colas

def buscar_el_maximo(p:Pila[int]) -> int:
    maximo: int = p.get()
    pCopia: Pila[int] = Pila()
    pCopia.put(maximo)
    while not p.empty():
        actual: int = p.get()
        pCopia.put(actual)
        if actual > maximo:
            maximo = actual

    while not pCopia.empty():
        elem: int = pCopia.get()
        p.put(elem)
        
    return maximo

p:Pila[int] = Pila()
p.put(5)
p.put(15)
p.put(0)

print("Esta vaico p?", p.empty())
n:int = buscar_el_maximo(p)
print("El maximo numero de la fila es:", n)
# Dentro de la funcion estoy modificando la pila, deberia volverla a construir antes de salir de la funcion
print("Esta vaico p?", p.empty())

