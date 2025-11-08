from queue import LifoQueue as Pila
# Parte 3: Dicts

# EJercicio 16
'''
problema calcular promedio por estudiante (in notas: seq⟨seq⟨Char⟩ × R⟩) : Diccionario ⟨ seq⟨Char⟩, R⟩ {
requiere: {El primer componente de las tuplas de notas no es una cadena vacı́a}
requiere: {El segundo componente de las tuplas de notas está en el rango [0, 10]}
asegura: {Todas las claves de res son nombres que aparecen en notas (primer componente)}
asegura: {Todos los nombres de notas (primer componente) son clave en res}
asegura: {El valor de cada clave de res es el promedio de todas las notas que obtuvo el estudiante (segundo componente
de notas)}
}
Cada nota de la lista recibida como parámetro es una tupla que tiene como primer componente el nombre del estudiante y,
como segundo, la nota que se sacó en un examen.
Por ejemplo:
notas: list[tuple[str, float]] = [("Sole", 9.5), ("Maxi", 8.0), ("Sole", 9.0)]
calcular promedio por estudiante(notas) debe devolver {"Sole": 9.25, "Maxi": 8.0}
'''

def calcular_promedio_por_estudiante(notas: list[tuple[str,float]]) -> dict[str,float]:
    res: dict[str,float]= {}
    registro: dict[str, list[float]] = {}
    for estudiante, nota in notas:
        if estudiante in registro:
            registro[estudiante].append(nota)
        else:
            registro[estudiante] = [nota]

    print(registro)

    for estudiante in registro:
        suma_notas: float = 0
        for nota in registro[estudiante]:
            suma_notas += nota

        res[estudiante] = suma_notas/len(registro[estudiante])

    return res

print(calcular_promedio_por_estudiante([("Maria", 10), ("Juan", 6), ("Mateo", 7), ("Juan", 8), ("Rodolfo", 2), ("Mateo", 5)]))


# Ejercicio 17
'''
Ejercicio 17. Se debe desarrollar un navegador web muy simple que debe llevar un registro de los sitios web visitados por los
usuarios del sistema. El navegador debe permitir al usuario navegar hacia atrás en la historia de navegación.

1. Crea un diccionario llamado historiales que almacenará el historial de navegación para cada usuario. Las claves del
diccionario serán los nombres de usuario y los valores serán pilas de String.
'''

pila_juan: Pila[str] = Pila()
pila_juan.put("google.com")
pila_juan.put("amazon.com")

pila_julio: Pila[str] = Pila()
pila_julio.put("instagram.com")
pila_julio.put("facebook.com")

historiales: dict[str,Pila[str]] = {
    "Juan": pila_juan,
    "Julio": pila_julio
}

'''
2. Implementar una solución para el siguiente problema.
problema visitar sitio (inout historiales: Diccionario⟨seq⟨Char⟩, P ila[seq⟨Char⟩]⟩, in usuario: seq⟨Char⟩, in sitio: seq⟨Char⟩)
{
requiere: {Ninguno de los Strings de los parámetros es vacı́o}
asegura: {Si usuario es una de las claves de historiales@pre, entonces se agrega sitio a su pila de historia-
les@pre[usuario]}
asegura: {Si usuario no es una de las claves de historiales@pre, entonces historiales[usuario] es igual a la pila
que tiene solo el elemento sitio}
asegura: {No se modifica ningún otro historial salvo, si existe, el de usuario}
asegura: {Todos los pares clave-valor de historiales@pre están en historiales}
asegura: {Todos los pares clave-valor de historiales están en historiales@pre, salvo historiales[usuario] que podrı́a
no existir en historiales@pre}
}
'''

def imprimir_pila(pila: Pila) -> list:
    res: list[int] = []
    pilaCopy: Pila = Pila()
    while not pila.empty():
        item = pila.get()
        res.append(item) 
        pilaCopy.put(item)
    while not pilaCopy.empty():
        pila.put(pilaCopy.get())
    return res

def visitar_sitio(historiales: dict[str, Pila[str]], usuario:str, sitio:str) -> None:
    if usuario in historiales.keys():
        historiales[usuario].put(sitio)
    else:
        historiales[usuario]: Pila[str] = Pila()
        historiales[usuario].put(sitio)

def imprimir_dict(historiales):
    for usuario, value in historiales.items():
        contenido_pila = imprimir_pila(value)
        print(f"{usuario}: {contenido_pila}")

visitar_sitio(historiales, "Juan", "ikea.com")
print("Juan visita Ikea")
imprimir_dict(historiales)
visitar_sitio(historiales, "Amalia", "ikea.com")
print("Aparece Amalia")
imprimir_dict(historiales)



'''
3. Implementar una solución para el siguiente problema.
problema navegar atras (inout historiales: Diccionario⟨ seq⟨Char⟩, Pila[ seq⟨Char⟩, in usuario: seq⟨Char⟩⟩) : seq⟨Char⟩
{
requiere: {Ninguno de los Strings de los parámetros es vacı́o}
requiere: {usuario es una clave de historiales}
requiere: {La pila asociada a usuario no está vacı́a}
asegura: {res es igual al tope de historiales@pre[usuario]}
asegura: {historiales[usuario] es igual a historiales@pre[usuario] quitando el tope de la pila de
historiales@pre[usuario]}
asegura: {En historiales, salvo la pila asociada a usuario, no se modifica ningún otro por clave-valor}
}
'''

def navegar_atras(historiales: dict[str, Pila[str]], usuario: str) -> str:
    res: str = ""
    if usuario in historiales:
        res = historiales[usuario].get()
    return res

print("Sitio del que sale Juan:", navegar_atras(historiales, "Juan"))
print("Juan deja Ikea")
imprimir_dict(historiales)

navegar_atras(historiales, "Amalia")
imprimir_dict(historiales)
historiales.pop("Amalia")
imprimir_dict(historiales)



# Ejercicio 18.1
'''
Ejercicio 18. Se debe desarrollar un sistema de gestión de inventario para una tienda de ropa. Este sistema debe permitir llevar
un registro de los productos en el inventario y realizar operaciones como agregar nuevos productos, actualizar las existencias y
calcular el valor total del inventario.
Para resolver este problema vamos a utilizar un diccionario llamado inventario que almacenará la información de los
productos. En este diccionario, cada clave será el nombre de un producto, y su valor asociado será otro diccionario con los
atributos del producto. Este segundo diccionario tendrá dos claves posibles: ’precio’y ’cantidad’, cuyos valores serán de tipo float
e int, respectivamente.
Un ejemplo de inventario, con un solo producto, es: {“remera”: {“precio”: 999.99, “cantidad”: 3}}).
Implementar una solución para cada uno de los siguientes problemas. Agregar en las funciones los tipos de datos correspondientes
(ver nota al final de la primera especificación).

1. problema agregar producto (inout inventario: Diccionario⟨ seq⟨Char⟩, Diccionario⟨ seq⟨Char⟩, T ⟩⟩, in nombre: seq⟨Char⟩,
in precio: R, in cantidad: Z) {
requiere: {T ∈ [Z, R]}
requiere: {cantidad ≥ 0}
requiere: {precio ≥ 0}
requiere: {Ninguno de los Strings de los parámetros es vacı́o}
requiere: {nombre no es una clave de inventario }
asegura: {Todas los pares clave-valor de inventario@pre están tal cual en inventario}
asegura: {Todas los pares clave-valor de inventario están en inventario@pre y, además, hay una nueva con clave
igual a nombre y como valor tendrá un diccionario con los pares clave-valor (“precio”, precio) y (“cantidad”,
cantidad)}
}
Se necesitará un diccionario cuyas claves son de tipo String (“precio” y “cantidad”) y cuyos valores serán de tipo float
y enteros respectivamente. Para declarar los tipos de este diccionario mediante anotaciones en Python, se procede de la
siguiente manera:
En Python 3.9:
Es necesario importar Union desde el módulo typing para indicar que los valores pueden ser de más de un tipo.
from typing import Union
mi diccionario: dict[str, Union[int, float]]
En Python 3.10 o superior:
No es necesario importar Union, ya que se puede usar el operador | para representar una unión de tipos.
mi diccionario: dict[str, int | float]
'''

# Ejercicio 18.2
'''
2. problema actualizar stock (inout inventario: Diccionario ⟨ seq⟨Char⟩, Diccionario⟨ seq⟨Char⟩, T ⟩⟩, in nombre: seq⟨Char⟩,
in cantidad: R) {
requiere: {T ∈ [Z, R]}
requiere: {cantidad ≥ 0}
requiere: {nombre es una clave existente en el inventario}
requiere: {Ninguno de los Strings de los parámetros es vacı́o}
asegura: {Todos los pares clave-valor de inventario@pre están tal cual en inventario, con excepción del que tiene
como clave nombre}
asegura: {Todos los pares clave-valor de inventario están en inventario@pre}
asegura: {En inventario, el valor asociado a la clave nombre, tendrá el mismo precio que antes y la cantidad será
cantidad}
}
'''


# Ejercicio 18.3
'''
3. problema actualizar precio (inout inventario: Diccionario⟨ seq⟨Char⟩, Diccionario⟨ seq⟨Char⟩, T ⟩⟩, in nombre:seq⟨Char⟩,
in precio: R) {
requiere: {T ∈ [Z, R]}
requiere: {precio ≥ 0}
requiere: {nombre es una clave existente en el inventario}
requiere: {Ninguno de los Strings de los parámetros es vacı́o}
asegura: {Todos los pares clave-valor de inventario@pre están tal cual en inventario, con excepción del valor que
tiene como clave nombre}
asegura: {Todos los pares clave-valor de inventario están en inventario@pre}
asegura: {En inventario el diccionario asociado a nombre, tendrá la misma cantidad que antes y el precio será
precio}
}
'''

# Ejercicio 18.4
'''
4. problema calcular valor inventario (in inventario: Diccionario ⟨ seq⟨Char⟩, Diccionario ⟨ seq⟨Char⟩, T ⟩⟩) : R {
requiere: {T ∈ [Z, R]}
requiere: {Ninguno de los Strings del inventario es vacı́o}
asegura: {res es la suma, para cada producto, del precio multiplicado por la cantidad}
}
Ejemplo de uso:
inventario = {}
agregar_producto(inventario, "Camisa", 20.0, 50)
agregar_producto(inventario, "Pantalón", 30.0, 30)
actualizar_stock(inventario, "Camisa", 10)
valor_total = calcular_valor_inventario(inventario)
print("Valor total del inventario:", valor_total) # Deberı́a imprimir 1100.0
'''