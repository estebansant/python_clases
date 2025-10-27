# Parte 2: Colas
from queue import Queue as Cola
from typing import Tuple
import random

# Ejercicio 8
'''
problema generar nros al azar (in cantidad: Z, in desde: Z, in hasta: Z) : Cola[Z] {
requiere: {cantidad ≥ 0}
requiere: {desde ≤ hasta}
asegura: {El tamaño de res es igual a cantidad}
asegura: {Todos los elementos de res son valores entre desde y hasta (ambos inclusive), seleccionados aleatoriamente
con probabilidad uniforme}
}
Para generar números en un rango con probabilidad uniforme, pueden usar la función random.randint(< desde >, < hasta >)
que devuelve un número en el rango indicado. Recuerden importar el módulo random con import random. Pueden usar la clase
Queue() que es un ejemplo de una implementación básica de una Cola:
from queue import Queue as Cola # importa Queue y le asigna el alias Cola
c = Cola () # creo una
c . put (1) # encolo el
elemento = c . get () #
c . empty () # devuelve
cola
1
desencolo
true si y solo si la cola est á vac ı́ a
'''
def imprimir_cola(cola: Cola) -> list:
    elementos: list = []
    cola_copia: Cola = Cola()
    
    # Primera pasada: Vaciar la original, guardar en lista y en copia
    while not cola.empty():
        elemento = cola.get()
        elementos.append(elemento)
        cola_copia.put(elemento)
        
    # Segunda pasada: Restaurar la cola original
    while not cola_copia.empty():
        cola.put(cola_copia.get())
        
    return elementos

def generar_numeros_al_azar(cantidad:int, desde:int, hasta: int) -> Cola[int]:
    res: Cola[int] = Cola()
    cont: int = 0
    while cont< cantidad:
        res.put(random.randint(desde,hasta))
        cont += 1
    print(imprimir_cola(res))
    return res

print("Numeros al azar", imprimir_cola(generar_numeros_al_azar(10,1,100)))



# Ejercicio 9
'''
problema cantidad elementos (in c: Cola) : Z {
requiere: {True}
asegura: {res es igual a la cantidad de elementos que contiene c}
}
No se puede utilizar la función Queue.qsize().
Comparar el resultado con la implementación utilizando una pila en lugar de una cola.
'''

def cantidad_elementos_cola(c: Cola) -> int:
    res: int = 0
    cCopia: Cola = Cola()
    while not c.empty():
        cCopia.put(c.get())
        print(imprimir_cola(cCopia))
        res+=1
    while not cCopia.empty():
        c.put(cCopia.get())
        print("Cola c recomposicion", imprimir_cola(c))
    return res

cola: Cola = Cola()
cola.put(1)
cola.put(2)
cola.put(3)
cola.put(4)
cola.put(5)

cantidad_elementos_cola(cola)
print("Cola de verdad", imprimir_cola(cola))



# Ejercicio 10

'''
problema buscar el maximo (in c: Cola[Z]) : Z {
requiere: {c no está vacı́a}
asegura: {res es un elemento de c}
asegura: {res es mayor o igual a todos los elementos de c}
}
Comparar con la versión usando pila.
'''

def buscar_el_maximo(c: Cola[int]) -> int:
    res: int = c.get()
    cCopia: Cola[int] = Cola()
    cCopia.put(res)
    while not c.empty():
        elem: int = c.get()
        if elem > res:
            res = elem
        cCopia.put(elem)
    while not cCopia.empty():
        c.put(cCopia.get())
    print("Cola antes de salir", imprimir_cola(c))
    return res
c: Cola[int] = Cola()
c.put(0)
c.put(10)
c.put(1)
c.put(80)
c.put(45)

print("Cola antes de entrar a la funcion", imprimir_cola(c))
print("El maximo de la cola es:", buscar_el_maximo(c))
print("Cola antes despues de la funcion", imprimir_cola(c))


# Ejercicio 11
'''
problema buscar nota minima (in c: Cola[seq⟨Char × Z⟩]) : (seq⟨Char × Z⟩) {
requiere: {c no está vacı́a}
requiere: {los elementos de c no tienen valores repetidos en la segunda componente de las tuplas}
asegura: {res es una tupla de c}
asegura: {No hay ningún elemento en c cuya segunda componente sea menor que la de res }
}
'''

def buscar_nota_minima(c: Cola[Tuple[str,int]]) -> Tuple[str,int]:
    res: Tuple[str,int] = c.get()
    cCopia: Cola[Tuple[str,int]] = Cola ()
    cCopia.put(res)
    while not c.empty():
        elem: Tuple[str,int] = c.get()
        if res[1] > elem[1]:
            res = elem
            print(res)
        cCopia.put(elem)
    while not cCopia.empty():
        c.put(cCopia.get())
    print("Cola antes de salir de la funcion", imprimir_cola(c))
    return res

notas: Cola[Tuple[str,int]] = Cola()
notas.put(("Alfredo", 10))
notas.put(("Nicolas", 8))
notas.put(("Jaime", 3))
notas.put(("Roberto", 5))

print("Cola antes de entrar a la funcion", imprimir_cola(notas))
print("La nota minima es:", buscar_nota_minima(notas))

# Ejercicio 12
'''
problema intercalar (in c1: Cola, in c2: Cola) : Cola {
requiere: {c1 y c2 tienen la misma cantidad de elementos}
asegura: {res solo contiene los elementos de c1 y c2}
asegura: {res contiene todos los elementos de c1 y c2, intercalados y respetando el orden original}
asegura: {El primer elemento de res es el primer elemento de c1}
asegura: {El tamaño de res es igual al doble del tamaño de c1}
}
'''

def intercalar(c1: Cola, c2: Cola) -> Cola:
    res: Cola = Cola()
    c1Copia: Cola = Cola()
    c2Copia: Cola = Cola()
    while not c1.empty():
        c1Copia.put(c1.get())
    while not c2.empty():
        c2Copia.put(c2.get())
    cont: int = 0
    while (not c1Copia.empty()) or (not c2Copia.empty()):
        if cont%2==0:
            elem = c1Copia.get()
            res.put(elem)
            c1.put(elem)
        else:
            item = c2Copia.get()
            res.put(item)
            c2.put(item)
        cont +=1
    print("C1 al finalizar el bucle", imprimir_cola(c1))
    print("C2 al finalizar el bucle", imprimir_cola(c2))
    return res

c1: Cola[int] = Cola()
c2: Cola[str] = Cola()
c1.put(1)
c1.put(2)
c1.put(3)
c1.put(4)
c2.put("H")
c2.put("o")
c2.put("l")
c2.put("a")

print("C1 original", imprimir_cola(c1))
print("C2 original", imprimir_cola(c2))
print("Resultado de intercalar colas C1 y C2", imprimir_cola(intercalar(c1,c2)))



# Ejercicio 13
'''
Ejercicio 13. Bingo: un cartón de bingo contiene 12 números al azar en el rango [0, 99]. Implementar una solución para cada
uno de los siguientes problemas.
1. problema armar secuencia de bingo () : Cola[Z] {
requiere: {True}
asegura: {res solo contiene 100 números del 0 al 99 inclusive, sin repetidos}
asegura: {Los números de res están ordenados al azar}
}
Para generar números pseudoaleatorios pueden usar la función random.randint(< desde >, < hasta >) que devuelve un
número en el rango indicado. Recuerden importar el módulo random con import random.
2. problema jugar carton de bingo (in carton: seq⟨Z⟩, in bolillero: Cola[Z]) : Z {
requiere: {carton solo contiene 12 números, sin repetidos, con valores entre 0 y 99, ambos inclusive}
requiere: {bolillero solo contiene 100 números, ordenados al azar, del 0 al 99, ambos inclusive, sin repetidos}
asegura: {res es la cantidad mı́nima de jugadas necesarias para que todos los números del carton hayan salido del
bolillero}
}
'''

def armar_secuencia_de_bingo() -> Cola[int]:
    res: Cola[int] = Cola()
    lista_de_numeros: list[int] = list(range(100))
    random.shuffle(lista_de_numeros)

    for numero in lista_de_numeros:
        res.put(numero)
        
    return res

print("Cola del bingo", imprimir_cola(armar_secuencia_de_bingo()))

def jugar_carton_de_bingo(carton: list[int], bolillero: Cola[int]) -> int:
    res: int = 0
    carton_marcado: list[int] = list(carton)
    jugadas_totales: int = 0
    bolilleroCopia: Cola[int] = Cola() 
    while not bolillero.empty():
        numero: int = bolillero.get()  
        jugadas_totales += 1
        if res == 0:
            if numero in carton_marcado:
                carton_marcado.remove(numero)
                if len(carton_marcado) == 0:
                    res = jugadas_totales
        bolilleroCopia.put(numero)
    while not bolilleroCopia.empty():
        bolillero.put(bolilleroCopia.get())
    return res

carton:list[int]= [10,3,65,73,2,17,9,43,77,1,88,99]
print("El numero de jugadas minimo es:", jugar_carton_de_bingo(carton, armar_secuencia_de_bingo()))


# Ejercicio 14
'''
Ejercicio 14. Vamos a modelar una guardia de un hospital usando una cola donde se van almacenando los pedidos de atención
para los pacientes que van llegando. A cada paciente se le asigna una prioridad del 1 al 10 (donde la prioridad 1 es la más urgente
y requiere atención inmediata) junto con su nombre y la especialidad médica que le corresponde. Implementar una solución para
el siguiente problema.
problema pacientes urgentes (in c:Cola[Z× seq⟨Char⟩ × seq⟨Char⟩]) : Z {
requiere: {Todos los elementos de c tienen como primer componente de la tupla un entero positivo y menor a 11}
asegura: {res es la cantidad de elementos de c que tienen como primer componente de la tupla un número menor a 4}
}
'''

def pacientes_urgentes(c: Cola[tuple[int,str,str]]) -> int:
    res: int = 0
    cCopia: Cola[tuple[int,str,str]] = Cola()
    while not c.empty():
        paciente: tuple[int,str,str] = c.get()
        cCopia.put(paciente)
        if paciente[0] < 4:
            res +=1
    while not cCopia.empty():
        c.put(cCopia.get())
    return res

pacientes: Cola[tuple[int,str,str]] = Cola()
pacientes.put((1,"Pepe", "Traumatologo"))
pacientes.put((3,"John", "Traumatologo"))
pacientes.put((2,"Doe", "Traumatologo"))
pacientes.put((9,"Jane", "Traumatologo"))
pacientes.put((5,"Wilde", "Traumatologo"))
pacientes.put((4,"Rick", "Traumatologo"))
pacientes.put((7,"Strauss", "Traumatologo"))

print("El numero de pacientes urgentes a atender es:", pacientes_urgentes(pacientes))

# Ejercicio 15
'''
Ejercicio 15. La gerencia de un banco nos pide modelar la atención de los clientes usando una cola donde se van registrando
los pedidos de atención. Cada vez que ingresa una persona a la entidad, debe completar sus datos en una pantalla que está a la
entrada: Nombre y Apellido, DNI, tipo de cuenta (true si es preferencial o f alse en el caso contrario) y si tiene prioridad (true
o f alse) por ser adulto +65, embarazada o con movilidad reducida.
La atención a los clientes se da por el siguiente orden: primero las personas que tienen prioridad, luego las que tienen cuenta
bancaria preferencial y por último el resto. Dentro de cada subgrupo de clientes, se respeta el orden de llegada.
1. Dar una especificación para el problema planteado.
2. Implementar atencion a clientes(in c : Cola[tuple[str, int, bool, bool]]) → Cola[tuple[str, int, bool, bool]] que da-
da la cola de ingreso de clientes al banco devuelve la cola en la que van a ser atendidos.
'''

def atencion_a_clientes(c: Cola[tuple[str,int,bool,bool]]) -> Cola[tuple[str,int,bool,bool]]:
    res: Cola[tuple[str,int,bool,bool]] = Cola()
    cCopia: Cola[tuple[str,int,bool,bool]] = Cola()
    cSuperPrioridad: Cola[tuple[str,int,bool,bool]] = Cola()
    cPrioridad: Cola[tuple[str,int,bool,bool]] = Cola()
    cPreferencial: Cola[tuple[str,int,bool,bool]] = Cola()
    cComun: Cola[tuple[str,int,bool,bool]] = Cola()
    while not c.empty():
        persona: tuple[str,int,bool,bool] = c.get()
        cCopia.put(persona)
        if (persona[2] == True) and (persona[3] == True):
            cSuperPrioridad.put(persona)
        elif (persona[3] == True):
            cPrioridad.put(persona)
        elif (persona[2] == True):
            cPreferencial.put(persona)
        else:
            cComun.put(persona)
    while not cCopia.empty():
        c.put(cCopia.get())
    while not cSuperPrioridad.empty():
        res.put(cSuperPrioridad.get())
    while not cPrioridad.empty():
        res.put(cPrioridad.get())
    while not cPreferencial.empty():
        res.put(cPreferencial.get())
    while not cComun.empty():
        res.put(cComun.get())
    print("Res dentro de la funcion", imprimir_cola(res))
    return res

lista_de_clientes: Cola[tuple[str,int,bool,bool]] = Cola()
lista_de_clientes.put(("John", 18567142, True, False))
lista_de_clientes.put(("Amanda", 18567192, False, False))
lista_de_clientes.put(("Miranda", 18567191, True, True))
lista_de_clientes.put(("Ricardo", 18567193, False, True))

print("El orden de atencion es:", imprimir_cola(atencion_a_clientes(lista_de_clientes)))
