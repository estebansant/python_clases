""" Parcial de Python del primer cuatrimestre de 2025. """

from queue import LifoQueue as Pila

"""
* Ejercicio 1

Implementar la función prefijo_que_mas_suma:

problema prefijo_que_mas_suma (in s: secuencia<Entero>) : Entero {
  requiere: { |s| > 0 }
  asegura: { res = sumatoria de s[i] (desde i=0 hasta k) para algún k tal que 0 <= k < |s|}
  asegura: { res >= sumatoria de s[i] (desde i=0 hasta k) para todos los k tales que 0 <= k < |s|}
}

* NOTA: 1.62 / 2.00

"""

def prefijo_que_mas_suma(s:list[int]) -> int:
  suma_actual: int = 0
  res: int = s[0]

  for i in range(len(s)):
    suma_actual += s[i]

    if suma_actual > res:
      res = suma_actual

  return res

print(prefijo_que_mas_suma([-10,-12,-1, 12,5,6,100,-90]))


"""
* Ejercicio 2

Todavía existen materias en la cuales los exámenes se entregan en papel. A medida que los estudiantes van entregando, van apoyando (apilando!) sobre el escritorio del docente sus exámenes, y en la primera hoja indican su nombre y la cantidad de hojas entregadas (además del enunciado). Esta información se almacena en una Pila de String x Entero. Nos intersa conocer el nombre de la primera persona que entregó un examen en blanco (es decir, entregó 0 hojas además del enunciado).

problema primera_entrega_en_blanco (in examenes: Pila<String x Entero>) : String {
  requiere:{ Las primeras componentes de examenes son strings no vacíos y todos distintos entre sí }
  requiere:{ Existe al menos un elemento p dentro de la pila examenes tal que p1=0 }
  asegura: { Sea p el primer elemento insertado en la pila examenes tal que p1=0. Entonces, res = p0 }
}

* NOTA: 0.00/2.00
"""

def imprimir_pila(pila: Pila) -> list:
  res: list = []
  copiaPila: Pila = Pila ()
  while not pila.empty():
    elemento = pila.get()
    copiaPila.put(elemento)
    # res.append(elemento)

  while not copiaPila.empty():
    elemento = copiaPila.get()
    pila.put(elemento)
    res.append(elemento)
  return res
  

def primera_etrega_en_blanco(examenes: Pila[tuple[str,int]]) -> str:
  res: str = ""
  print("longitud str vacio", len(res))
  pilaCopia: Pila[tuple[str,int]] = Pila()
  while not examenes.empty():
    pilaCopia.put(examenes.get())
    
  while not pilaCopia.empty():
    elemento = pilaCopia.get()
    examenes.put(elemento)
    if ((elemento[1] == 0) and (len(res) == 0)):
      res = elemento[0]
  return res



examenes: Pila[tuple[str,int]] = Pila()
examenes.put(("Roberto", 3))
examenes.put(("Alejandro", 1))
examenes.put(("Alicia", 4))
examenes.put(("Pepe", 9))
examenes.put(("Carlos", 0))
examenes.put(("Mariana", 2))
examenes.put(("Perez", 0))

print("PILA DE EXAMENES", imprimir_pila(examenes))
print(primera_etrega_en_blanco(examenes))


"""
* Ejercicio 3

Implementar la función desplazar_columna_hacia_arriba:

problema desplazar_columna_hacia_arriba(inout A: secuencia<secuencia<Entero>>, in col: Entero) {
  requiere: { Todas las filas de A tienen la misma longitud (estrictamente positiva)}
  requiere: { |A| > 0}
  requiere: { 0 <= col < |A[0]| }
  modifica: { A }
  asegura: { A tiene exactamente las mismas dimensiones que A@pre }
  asegura: { A[i][j] = A@pre[i][j] para todo i, j en rango tal que col != j }
  asegura: { A[i][col] = A@pre[i+1][col] para todo i tal que 0 <= i < |A|-1 }
  asegura: { A[|A|-1][col] = A@pre[0][col] }
}

* NOTA: 2.00/2.00
"""

def desplazar_columna_hacia_arriba(A: list[list[int]], col: int) -> None:
    cantidad_filas: int = len(A)

    if cantidad_filas <= 1:
      return

    primer_valor:int = A[0][col]

    for i in range(0,len(A)-1):
      A[i][col] = A[i+1][col]
    
    A[cantidad_filas - 1][col] = primer_valor

    return



A: list[list[int]] = [
                      [1,2,3,4,5],
                      [6,7,8,9,10],
                      [11,12,13,14,15]
                    ]
desplazar_columna_hacia_arriba(A,2)
print(A)

"""
* Ejercicio 4

A lo largo del año se realizaron diversas competencias de programación, las cuales van otorgando puntos y permiten generar un ranking entre los competidores, con el objetivo de entregar premios al final del año. En cada una de las competencias se selecciona a los 3 participantes con mejor desempeño, y se define el podio para cada una. Luego, se asignan los puntajes de la siguiente manera:

    Quien sale en primer puesto recibe 3 puntos
    Quien sale en segundo puesto recibe 2 puntos
    Quien sale en tercer puesto recibe 1 punto

Nuestro objetivo es, dada una lista de competencias y sus resultados, conocer el ranking actual.

problema armar_ranking (in podios: secuencia<Diccionario<Entero,String>>): Diccionario<String,Entero> {
  requiere: { Cada diccionario de podios tiene como claves los valores 1, 2 y 3 (o algún subconjunto de los mismos)}
  requiere: { Sea d un diccionario de la secuencia podios , entonces d no contiene valores repetidos }
  asegura: { nom es clave de res si y sólo si existe un diccionario en podios tal que nom es valor de dicho diccionario}
  asegura: { Cada clave c de res tiene como valor la sumatoria de los puntos obtenidos por c en cada una de las competencias de podios (suma 3 puntos si salió primero, 2 puntos si salió segundo, 1 punto si salió tercero y 0 puntos si no estuvo en el podio de esa competencia)}
}

* NOTA: 2.50/2.50
"""

podios: list[dict[int,str]] = [
  {
    3: "Manuel",
    2: "Carlos",
    1: "Maria"
  },{
    3: "Pepe",
    2: "Alberto",
    1: "Carla"
  },{
    3: "Joaco",
    2: "Carla",
    1: "Pepe"
  },{
    3: "Julio",
    2: "Juan",
    1: "Maria"
  },{
    3: "Oscar",
    2: "Manuela",
    1: "Maria"
  },{
    3: "Clara",
    2: "Carlos",
    1: "Daniela"
  },{
    3: "Manuel",
    2: "Bernie",
    1: "Valeria"
  },
]

def armar_ranking(podios: list[dict[int,str]]) -> dict[str,int]:
  res: dict[str,int] = {}
  
  for podio in podios:
    for posicion in podio:
      puntaje: int = 0

      if posicion == 1:
        puntaje = 3
      elif posicion ==2:
        puntaje = 2
      elif posicion == 3:
        puntaje = 1

      nombre = podio[posicion]

      if nombre not in res:
        res[nombre] = puntaje
      else:
        res[nombre] += puntaje

  return res

print(armar_ranking(podios))

"""
* Ejercicio 5

Dada la siguiente especificación y una posible implementación de la misma, conteste marcando la opción correcta.

problema sumar_o_restar_uno (in n: Entero): Entero {
  requiere: { True }
  asegura: { Si n > 0, res = n+1}
  asegura: { Si n = 0, res = n}
  asegura: { Si n < 0, res = n-1}
}

def sumar_o_restar_uno(n: int) -> int:
   res: int = n
   if n > 0:
        res += 1
   else:
        res -= 1
   return res

[ ] El código es correcto, calcula lo pedido en la especificación para cualquier input
[ ] El código tiene un bug, y si hacemos un test suite que cubra todas las líneas lo detectaremos
[X] El código tiene un bug, pero es posible hacer un test suite que cubra todas las líneas y no detectar dicho bug

* NOTA: 0.75/0.75

* Ejercicio 6

Seleccione la opción correcta.

[ ] Si tengo 2 programas y los ejecuto con los mismos parámetros, el programa que tiene mayor cantidad de líneas de código ejecutará más operaciones que el que tiene menos líneas de código.
[ ] Dado un programa p que recibe una secuencia como parámetro, p([1]) ejecutará menos operaciones que p([0,1,2,3,4,5])
[X] No es posible afirmar ninguna de las opciones anteriores sin conocer el código de la/las función/funciones

* NOTA: 0.75/0.75
"""

def sumar_elementos(s: list[int]) -> int:
  res: int = 0
  for i in range(1, len(s)):
    res += s[i]
  return res

print(sumar_elementos([1,2]))