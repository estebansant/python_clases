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


# Ejercicio 3
'''
problema buscar el maximo (in p: Pila[Z]) : Z {
requiere: {p no está vacı́a}
asegura: {res es un elemento de p}
asegura: {res es mayor o igual a todos los elementos de p}
}
'''

# Ejercicio 4
'''
problema buscar nota maxima (in p: Pila[seq⟨Char⟩×Z]) : seq⟨Char⟩ ×Z {
requiere: {p no está vacı́a}
requiere: {los elementos de p no tienen valores repetidos en la segunda posición de las tuplas}
asegura: {res es una tupla de p}
asegura: {No hay ningún elemento en p cuya segunda componente sea mayor que la segunda componente de res }
}
'''


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
