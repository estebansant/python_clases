from queue import LifoQueue as Pila
from typing import Tuple
import random

# Ejercicio 1
'''
problema generar nros al azar (in cantidad: Z, in desde: Z, in hasta: Z) : Pila[Z] {
requiere: {cantidad ≥ 0}
requiere: {desde ≤ hasta}
asegura: {El tamaño de res es igual a cantidad}
asegura: {Todos los elementos de res son valores entre desde y hasta (ambos inclusive), seleccionados aleatoriamente
con probabilidad uniforme}
}
Para generar números en un rango con probabilidad uniforme, pueden usar la función random.randint(< desde >, < hasta >)
que devuelve un número en el rango indicado. Recuerden importar el módulo random con import random. Además, pueden usar
la clase LifoQueue() que es un ejemplo de una implementación básica de una pila:
from queue import LifoQueue as Pila # importa LifoQueue y le asigna el alias Pila
p = Pila () # crea una pila
p . put (1) # apila un 1
elemento = p . get () # desapila
p . empty () # devuelve true si y solo si la pila est á vac ı́ a
'''

def imprimir_pila(pila: Pila) -> list[int]:
    res: list[int] = []
    pilaCopy: Pila = Pila()
    while not pila.empty():
        item = pila.get()
        res.append(item) 
        pilaCopy.put(item)
    while not pilaCopy.empty():
        pila.put(pilaCopy.get())
    return res

def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Pila[int]:
    res: Pila[int] = Pila()
    cont: int = 0
    while cont < cantidad:
        res.put(random.randint(desde,hasta))
        cont +=1
    return res


print("Generar numero al azar:", imprimir_pila(generar_nros_al_azar(10,1,10)))


# Ejercicio 2
'''
problema cantidad elementos (in p: Pila) : Z {
requiere: {True}
asegura: {res es igual a la cantidad de elementos que contiene p}
}
No se puede utilizar la función LifoQueue.qsize(). Tener en cuenta que, al usar get() para recorrer la pila, se modifica el
parámetro de entrada, ya que los elementos se eliminan al accederse. Dado que la especificación lo define como de tipo in, debe
restaurarse posteriormente.
'''

def cantidad_elementos(p: Pila) -> int:
    res: int = 0
    pCopy: Pila = Pila()
    while not p.empty():
        pCopy.put(p.get())
        res += 1
    while not pCopy.empty():
        p.put(pCopy.get())
    print("Pila copia", imprimir_pila(pCopy))
    print("Pila de la funcion", imprimir_pila(p))

    return res

p = Pila()
p.put(1)
p.put(2)
p.put(3)
p.put(4)
p.put(5)
p.put(3)
p.put(["bla bla bla"])
print("Cantidad de elementos", cantidad_elementos(p))
print("Esta es la Pila original", imprimir_pila(p))


# Ejercicio 3
'''
problema buscar el maximo (in p: Pila[Z]) : Z {
requiere: {p no está vacı́a}
asegura: {res es un elemento de p}
asegura: {res es mayor o igual a todos los elementos de p}
}
'''

def buscar_el_maximo(p: Pila[int]) -> int:
    res: int = p.get()
    pCopia: Pila[int] = Pila()
    pCopia.put(res)
    while not p.empty():
        elemento: int = p.get()
        pCopia.put(elemento)
        if res>=elemento:
            res = res
        else:
            res = elemento
    while not pCopia.empty():
        p.put(pCopia.get())
    print("Pila dentro de la funcion", imprimir_pila(p))
    return res

pila2: Pila[int] = Pila()
pila2.put(0)
pila2.put(100)
pila2.put(10)
pila2.put(10)
pila2.put(70)

print("Pila antes de la funcion", imprimir_pila(pila2))
print("El maximo de la pila es:", buscar_el_maximo(pila2))
print("Pila despues de la funcion", imprimir_pila(pila2))


# Ejercicio 4
'''
problema buscar nota maxima (in p: Pila[seq⟨Char⟩×Z]) : seq⟨Char⟩ ×Z {
requiere: {p no está vacı́a}
requiere: {los elementos de p no tienen valores repetidos en la segunda posición de las tuplas}
asegura: {res es una tupla de p}
asegura: {No hay ningún elemento en p cuya segunda componente sea mayor que la segunda componente de res }
}
'''

def buscar_nota_maxima(p: Pila[Tuple[str, int]]) -> Tuple[str, int]:
    res: Tuple[str, int] = []
    notas: Pila[int] = Pila()
    pCopia: Pila[Tuple[str,int]] = Pila()
    while not p.empty():
        elemento: Tuple [str,int] = p.get()
        pCopia.put(elemento)

        # nombre:str = elemento[0]
        nota:int = elemento [1]
        notas.put(nota)
    maximo: int = buscar_el_maximo(notas)
    while not pCopia.empty():
        item: Tuple[str,int] = pCopia.get()
        notaMaxima:int = item [1]
        p.put(item)

        if notaMaxima == maximo:
            res = item
    print("Notas antes de salir de la funcion", imprimir_pila(p))
    return res


notas: Pila[Tuple[str,int]] = Pila()
notas.put(("Jaime",2000)) 
notas.put(("Giorgio",20))
notas.put(("Giovanni",100000))
notas.put(("Hector",300))

print("Notas antes de la funcion", imprimir_pila(notas))
print("La nota maxima es", buscar_nota_maxima(notas))
print("Notas despues de la funcion", imprimir_pila(notas))


# Ejercicio 5
'''
problema esta bien balanceada (in s: seq⟨Char⟩) : Bool {
requiere: {s solo puede tener números enteros, espacios y los sı́mbolos ’(’, ’)’, ’+’, ’-’, ’*’, ’/’}
asegura: {res = true ↔ (La cantidad de paréntesis de apertura ’(és igual a la de cierre ’)’) y (Para todo prefijo de ‘s‘, la
cantidad de paréntesis de cierre no supera a la de apertura)}
}
Por cada paréntesis de cierre debe haber uno de apertura correspondiente antes de él. Las fórmulas pueden tener:
números enteros
operaciones básicas +, −, ∗ y /
paréntesis
espacios
Entonces las siguientes son fórmulas aritméticas con sus paréntesis bien balanceados:
1 + (2 x 3 = (20 / 5))
10 * ( 1 + ( 2 * ( = 1)))
Y la siguiente es una fórmula que no tiene los paréntesis bien balanceados:
1 + ) 2 x 3 ( ()
'''


# Ejercicio 6
'''
Ejercicio 6. La notación polaca inversa, también conocida como notación postfix, es una forma de escribir expresiones ma-
temáticas en la que los operadores siguen a sus operandos. Por ejemplo, la expresión “3 + 4” se escribe como “3 4 +” en notación
postfix. Para evaluar una expresión en notación postfix, se puede usar una pila. Implementar una solución para el siguiente
problema.
problema evaluar expresion (in s: seq⟨Char⟩) : R {
requiere: {s solo contiene números enteros y los operadores binarios +, -, * y /}
requiere: {Todos los elementos (operandos y operadores) están separados por un único espacio}
requiere: {La expresión es sintácticamente válida: cada operador binario tiene exactamente dos operandos previos
disponibles en el momento de su evaluación.}
asegura: {res es el valor obtenido al evaluar la expresión postfija representada por s}
}
Para resolver este problema, se recomienda seguir el siguiente algoritmo:
1. Dividir la expresión en tokens (operandos y operadores) utilizando espacios como delimitadores.
2. Recorre los tokens uno por uno.
a) Si es un operando, agrégalo a una pila.
b) Si es un operador, saca los dos operandos superiores de la pila, aplı́cale el operador y luego coloca el resultado en la
pila.
3. Al final de la evaluación, la pila contendrá el resultado de la expresión.
Ejemplo de uso:
expresion = "3 4 + 5 * 2 -"
resultado = evaluar_expresion(expresion)
print(resultado) # Deberı́a imprimir 33
'''



# Ejercicio 7

'''
problema intercalar (in p1: Pila, in p2: Pila) : Pila {
requiere: {p1 y p2 tienen la misma cantidad de elementos}
asegura: {res solo contiene los elementos de p1 y p2}
asegura: {res contiene todos los elementos de p1 y p2, intercalados y respetando el orden original}
asegura: {El tope de la pila res es el tope de p2}
asegura: {El tamaño de res es igual al doble del tamaño de p1}
}
Nota: Ojo que hay que recorrer dos veces para que queden en el orden apropiado al final.
'''
