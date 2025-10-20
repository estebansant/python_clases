from typing import Tuple

# Ejercicio 1

"""
1. problema pertenece (in s:seq⟨Z⟩, in e: Z) : Bool {
requiere: { T rue }
asegura: { (res = true) ↔(existe un i ∈ Z tal que 0 ≤ i < |s| ∧ s[i] = e) }
}
"""

def pertenece (s: list[int], e:int) -> bool:
    res: bool = False
    for i in range(0,len(s),1):
        if s[i] == e:
            res = True
    return res

print ("Pertenece", pertenece([1,2,3],3))


"""
2. problema divide a todos (in s:seq⟨Z⟩, in e: Z) : Bool {
requiere: { e̸ = 0 }
asegura: { (res = true) ↔ (para todo i ∈ Z si 0 ≤ i < |s| → s[i] mod e = 0) }
}
"""

def divide_a_todos(s:list[int], e:int) -> bool:
    res: bool = True
    for i in range(len(s)):
        if (s[i]%e != 0):
            res = False
    return res

print("Divide a todos", divide_a_todos([2,4,6,20], 2))

"""
3. problema suma total (in s:seq⟨Z⟩) : Z {
requiere: { T rue }
asegura: { res es la suma de todos los elementos de s }
}
"""

def suma_total(s: list[int]) -> int:
    res: int = 0
    for i in range(len(s)):
        res += s[i]
    return res

print("Suma total", suma_total([1,2,3,4]))

"""
4. problema maximo (in s:seq⟨Z⟩) : Z {
requiere: { |s| > 0 }
asegura: { res = al mayor de todos los n´umeros que aparece en s }
}
"""

def maximo(s:list[int]) -> int:
    res: int = s[0]
    for i in range(1,len(s),1):
        if (s[i]>res):
            res = s[i]
    return res

print("Maximo", maximo([1,2,3,9,10,100,40]))


"""
5. problema minimo (in s:seq⟨Z⟩) : Z {
requiere: { |s| > 0 }
asegura: { res = al menor de todos los n´umeros que aparece en s }
}
"""

def minimo(s:list[int]) -> int:
    res: int = s[0]
    for i in range(1,len(s),1):
        if (s[i]<res):
            res = s[i]
    return res

print("Minimo", minimo([1,2,3,9,10,100,0,-10]))

"""
6. problema ordenados (in s:seq⟨Z⟩) : Bool {
requiere: { T rue }
asegura: { res = true ↔(para todo i ∈ Z si 0 ≤ i < (|s| − 1) → s[i] < s[i + 1] }
}
"""

def ordenados(s:list[int]) -> bool:
    res: bool = True
    for i in range(0,len(s)-1,1):
        if (s[i]< s[i+1]) == False:
            res = False
    return res

print("Ordenados", ordenados([10,11,12,13,14]))

"""
7. problema pos maximo (in s:seq⟨Z⟩) : Z {
requiere: { T rue }
asegura: { (Si |s| = 0, entonces res = −1; si no, res = al ´ındice de la posici´on donde aparece el mayor elemento
de s (si hay varios es la primera aparici´on) }
}
"""

def pos_maximo(s:list[int]) -> int:
    res: int = 0
    if len(s)==0:
        res = -1
    else:
        for i in range(len(s)):
           if s[i]==maximo(s):
               res = i
               break
    return res

print("Posicion del maximo", pos_maximo([1,2,3,9,10,100,100,-10]))

"""

8. problema pos minimo (in s:seq⟨Z⟩) : Z {
requiere: { T rue }
asegura: { (Si |s| = 0, entonces res = −1; si no, res = al ´ındice de la posici´on donde aparece el menor elemento
de s (si hay varios es la ´ultima aparici´on) }
}
"""

def pos_minimo(s:list[int]) -> int:
    res: int = 0
    if len(s)==0:
        res = -1
    else:
        for i in range(len(s)):
           if s[i]==minimo(s):
               res = i
               break
    return res

print("Posicion del minimo", pos_minimo([-1,2,0,-2]))


"""
9. Dada una lista de palabras (seq⟨seq⟨Char⟩⟩), devolver verdadero si alguna palabra tiene longitud mayor a 7. Ejemplo:
[“termo”, “gato”, “tener”, “jirafas”], devuelve falso.
problema long mayorASiete (in s:seq⟨seq⟨Char⟩⟩) : Bool {
requiere: { T rue }
asegura: { (res = true) ↔ (existe i ∈ Z tal que (0 ≤ i < (|s| − 1)) y (|s[i]| > 7) }
}
"""

def long_mayorASiete(s: list[str]) -> bool:
    res: bool = False
    for i in range(len(s)):
        if len(s[i])>7:
            res = True
    return res

print("Longitud mayor a 7", long_mayorASiete(["termo", "gato", "tener", "jirafas", "cacatuas"]))


"""
10. Dado un texto en formato string, devolver verdadero si es pal´ındromo (se lee igual en ambos sentidos), falso en caso
contrario. Las cadenas de texto vac´ıas o con 1 s´olo elemento son pal´ındromo.
problema es palindroma (in s:seq⟨Char⟩) : Bool {
requiere: { T rue }
asegura: { (res = true) ↔ (s es igual a su reverso) }
}
"""
def es_palindromo(s: list[str]) -> bool:
    res: bool = False
    lista_reverso: list[str] = []
    if len(s) <= 1:
        res = True
    else:
        for i in range(len(s),0,-1):
            lista_reverso.append(s[i-1])
            print(lista_reverso)
        if (lista_reverso == s):
            res = True
    return res    

print("Es palindromo", es_palindromo(["s","a","l","a","s"]))

"""
11. Recorrer una seq⟨Z⟩ y devolver verdadero si hay 3 n´umeros iguales consecutivos, en cualquier posici´on y False en caso
contrario.
problema iguales consecutivos (in s:seq⟨Z⟩) : Bool {
requiere: { T rue }
asegura: { (res = true) ↔ (existe i, j, k ∈ Z tal que (0 ≤ i, j, k < (|s| − 1)) y (i + 2 = j + 1 = k) y
(s[i] = s[j] = s[k])) }
}
"""

def iguales_consecutivos(s:list[int]) -> bool:
    res: bool = False
    for i in range(len(s)-2):
        if (s[i] == s[i+1]) and (s[i]==s[i+2]):
            res = True
    return res

print("Iguales 3 Numeros Consecutivos", iguales_consecutivos([0,1,1,1,78,5,5,5,8,9,0]))

"""
12. Recorrer una palabra en formato string y devolver True si ´esta tiene al menos 3 vocales distintas y False en caso
contrario.
problema vocales distintas (in s:seq⟨Char⟩) : Bool {
requiere: { T rue }
asegura: { (res = true) ↔ (existe i, j, k ∈ Z tal que (0 ≤ i, j, k < (|s| − 1)) y (s[i]̸ = s[j]̸ = s[k]) y
(s[i], s[j], s[k] ∈ {‘a‘, ‘e‘, ‘i‘, ‘o‘, ‘u‘})) }
}
"""

def vocales_distintas(s:list[str])-> bool:
    res: bool = False
    vocales: list[str] = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vocales_en_palabra: list[str] = []
    for i in range(len(s)):
        if (s[i] in vocales):
            vocales_en_palabra.append(s[i])
        print(vocales_en_palabra)
    for j in range(len(vocales_en_palabra)-2):
        if (vocales_en_palabra[j] != vocales_en_palabra[j+1]) and (vocales_en_palabra[j]!=vocales_en_palabra[j+2]) and (vocales_en_palabra[j+1] != vocales_en_palabra[j+2]):
            res = True
            
    return res

print("3 vocales distintas", vocales_distintas(['S','e','b','a','s','t','i','a','n']))

"""
13. Recorrer una seq⟨Z⟩ y devolver la posici´on donde inicia la secuencia de n´umeros ordenada m´as larga. Si hay dos
subsecuencias de igual longitud devolver la posici´on donde empieza la primera. La secuencia de entrada es no vac´ıa.
problema pos secuencia ordenada mas larga (in s:seq⟨Z⟩) : Z {
requiere: { |s| > 0 }
asegura: { (res = i) ↔ (existe i, j ∈ Z tal que (0 ≤ i, j < (|s| − 1)) y i ≤ j y (para todo k tal que i ≤ k < j →
s[k] ≤ s[k + 1]) y j-i+1 es m´aximo e i es el m´ınimo valor que lo cumple) }
}
"""




"""
14. Cantidad de d´ıgitos impares.
problema cantidad digitos impares (in s:seq⟨Z⟩) : Z {
requiere: { Todos los elementos de n´umeros son mayores o iguales a 0 }
asegura: { res es la cantidad total de d´ıgitos impares que aparecen en cada uno de los elementos de n´umeros }
}
Por ejemplo, si la lista de n´umeros es [57, 2383, 812, 246], entonces el resultado esperado ser´ıa 5 (los d´ıgitos impares
son 5, 7, 3, 3 y 1)
"""

def cantidad_digitos_impares(s:list[int]) -> int:
    res: int = 0
    digitos_impares: list[str] = ["1", "3", "5", "7", "9"]
    for i in range(len(s)):
        numero: str = str(s[i])
        print(numero)
        for j in numero:
            if j in digitos_impares:
                res +=1
    return res

print("cantidad de numeros impares:", cantidad_digitos_impares([57, 2383, 812, 246,1,3,5,6,8,9,7]))



# Ejercicio 2

"""
1. problema CerosEnPosicionesPares (inout s:seq⟨Z⟩) {
requiere: { T rue }
modifica: { s }
asegura: { (|s| = |s@pre|) y (para todo i entero, con 0 <= i < |s|, si i es impar entonces s[i] = s@pre[i] y, si i
es par, entonces s[i] = 0) }
}
"""

def CerosEnPosicionesPares(s: list[int]) -> None:
    for i in range(len(s)):
        if i%2==0:
            s[i]=0
    print("S con ceros en sus posiciones pares:", s)

CerosEnPosicionesPares([1,2,3,4,5,6,7,8])

"""
2. problema CerosEnPosicionesPares2 (in s:seq⟨Z⟩) : seq⟨Z⟩ {
requiere: { T rue }
asegura: { (|s| = |res|) y (para todo i entero, con 0 <= i < |res|, si i es impar entonces res[i] = s[i] y, si i es
par, entonces res[i] = 0) }
}
"""

def CerosEnPosicionesPares2(s:list[int])->list[int]:
    res: list[int] = s.copy()
    for i in range(0,len(s),1):
        if i%2==0:
            res[i] = 0
        else:
            res[i]=s[i]
    print("Esta es la lista original", s)
    return res

print("S' con ceros en sus posiciones pares:", CerosEnPosicionesPares2([1,2,3,4,5,6,7,8]))

"""
3. Dada una cadena de caracteres devuelva una cadena igual a la anterior, pero sin las vocales. No se agregan espacios,
sino que borra la vocal y concatena a continuaci´on.
problema sin vocales (in s:seq⟨Char⟩) : seq⟨Char⟩ {
requiere: { T rue }
asegura: { res es la subsecuencia de s que se obtiene al quitarle las vocales a s }
}

Nota: Una subsecuencia de una cadena es una nueva secuencia que se crea eliminando algunos elementos de la cadena
original, conservando el orden de los elementos restantes.
"""

def sin_vocales(s:list[str]) -> list[str]:
    res: list[str] = []
    vocales: list[str] = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in range(len(s)):
        if s[i] in vocales:
            pass
        else:
            res.append(s[i])
    print("Lista original", s)
    return res

print("devolver sin vocales", sin_vocales(['S','e','b','a','s','t','i','a','n']))

"""
4. problema reemplaza vocales (in s:seq⟨Char⟩) : seq⟨Char⟩ {
requiere: { T rue }
asegura: { |res| = |s| }
asegura: { Para todo i ∈ Z, si 0 ≤ i < |res| → (pertenece(<‘a’,‘e’,‘i’,‘o’,‘u’>, s[i]) ∧ res[i] = ‘ ’) ∨
(¬ pertenece(<‘a’,‘e’,‘i’,‘o’,‘u’>, s[i]) ∧ res[i] = s[i])) }
}
"""

def reemplaza_vocales(s:list[str]) -> list[str]:
    res: list[str] = []
    vocales: list[str] = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in range(len(s)):
        if s[i] in vocales:
            res.append("_")
        else:
            res.append(s[i])
    print("Lista original", s)
    return res

print("Reemplazar vocales", reemplaza_vocales(['S','e','b','a','s','t','i','a','n']))

"""
5. problema da vuelta str (in s:seq⟨Char⟩) : seq⟨Char⟩ {
requiere: { T rue }
asegura: { |res| = |s| }
asegura: { Para todo i ∈ Z si 0 ≤ i < |res| → res[i] = s[|s| − i − 1] }
}
"""

def da_vuelta_str(s: list[str]) ->  list[str]:
    res: list[str] = []
    for i in range(len(s),0,-1):
            res.append(s[i-1])
    return res    

print("Dar vuelta al string", da_vuelta_str(["s","a","l","s","a"]))


"""
6. problema eliminar repetidos (in s:seq⟨Char⟩) : seq⟨Char⟩ {
requiere: { T rue }
asegura: { (|res| ≤ |s|) ∧ (para todo i ∈ Z si 0 ≤ i < |s| → pertenece(s[i], res)) ∧ (para todo i, j ∈ Z si
(0 ≤ i, j < |res| ∧ i̸ = j) → res[i]̸ = res[j]) }
}
"""

# pertenece([1,2,3],3)

def eliminar_repetidos(s:list[str]) -> list[str]:
    res: list[str] = []
    for i in range(len(s)):
        if pertenece(res, s[i]) == False:
            res.append(s[i])
    return res

print("Palabra sin elementos repetidos:", eliminar_repetidos(["m","a","n","z","a","n","a"]))

#Ejercicio 3

"""
Ejercicio 3. Implementar una funci´on para conocer el estado de aprobaci´on de una materia a partir de las notas obtenidas
por un/a alumno/a cumpliendo con la siguiente especificaci´on:
problema resultadoMateria (in notas: seq⟨Z⟩) : Z {
requiere: { |notas| > 0 }
requiere: { Para todo i ∈ Z si 0 ≤ i < |notas| → 0 ≤ notas[i] ≤ 10) }
asegura: { res = 1 ↔ todos los elementos de notas son mayores o iguales a 4 y el promedio es mayor o igual a 7 }
asegura: { res = 2 ↔ todos los elementos de notas son mayores o iguales a 4 y el promedio est´a entre 4 (inclusive) y 7 }
asegura: { res = 3 ↔ alguno de los elementos de notas es menor a 4 o el promedio es menor a 4 }
}
"""

def mayor_igual_a_4(s:list[int]) -> bool:
    res: bool = True
    for i in range(len(s)):
        if s[i] < 4:
            res= False
    return res

def resultadoMateria(notas: list[int]) -> int:
    res: int = 0
    if mayor_igual_a_4(notas) and (suma_total(notas)/len(notas) > 7):
        res=1
    elif mayor_igual_a_4(notas) and (4 <= suma_total(notas)/len(notas) < 7):
        res = 2
    elif (mayor_igual_a_4(notas)==False) or (suma_total(notas)/len(notas) < 4):
        res=3
    return res

print("La nota de la materia es:", resultadoMateria([7,5,4,6]))

# Ejercicio 4

"""
Ejercicio 4. Dada una lista de tuplas, que representa un historial de movimientos en una cuenta bancaria, devolver el saldo
actual. Asumir que el saldo inicial es 0. Las tuplas tienen una letra que nos indica el tipo de movimiento “I” para ingreso
de dinero y “R” para retiro de dinero, y adem´as el monto de cada operaci´on. Por ejemplo, si la lista de tuplas es [(‘‘I’’,
2000), (‘‘R’’, 20),(‘‘R’’, 1000),(‘‘I’’, 300)] entonces el saldo actual es 1280.
problema saldoActual (in movimientos: seq⟨Char × Z⟩) : Z {
requiere: { Para todo i ∈ Z si 0 ≤ i < |movimientos| → movimientos[i]0 ∈ {“I”,“R”} y movimientos[i]1 > 0 }
asegura: { res = Pingresos
i movimientos[i]1 − Pretiros
i movimientos[i]1 }
}
"""

MiTupla = Tuple[str, int]

def saldoActual(movimientos: list[Tuple[str, int]]) -> int:
    res: int = 0
    for operacion, monto in movimientos:
        if operacion == "R":
            res -= monto
        elif operacion == "I":
            res += monto
    return res

listaMovimientos: list[Tuple[str,int]] = [
    ("I",2000), ("R",20), ("R",1000), ("I",300)
]
print("El saldo actual de la cuenta es:", saldoActual(listaMovimientos))

# Ejercicio 5

"""
1. problema pertenece a cada uno version 1 (in s:seq⟨seq⟨Z⟩⟩, in e:Z, out res: seq⟨Bool⟩) {
requiere: { T rue }
asegura: { |res| ≥ |s| }
asegura: { Para todo i ∈ Z si 0 ≤ i < |s| → (res[i] = true ↔ pertenece(s[i], e)) }
}

Nota: Reutilizar la funci´on pertenece() implementada previamente para listas.
"""
# pertenece([1,2,3],3)

def pertenece_a_cada_uno_v1(s:list[int], e:int) -> list[bool]:
    res:list[bool] = []
    numero_a_lista: list[int] = []
    for i in range(len(s)):
        numero_a_lista.append(s[i])
        print("Primer print", numero_a_lista)
        if pertenece(numero_a_lista,e):
            res.append(True)
        else:
            res.append(False)
        numero_a_lista.remove(s[i])
        print("Primer print", numero_a_lista)
    print(s) 
    return res

print("Pertenece a cada uno version 1", pertenece_a_cada_uno_v1([1,2,3], 3))

"""
2. problema pertenece a cada uno version 2 (in s:seq⟨seq⟨Z⟩⟩, in e:Z, out res: seq⟨Bool⟩) {
requiere: { T rue }
asegura: { |res| = |s| }
asegura: { Para todo i ∈ Z si 0 ≤ i < |s| → (res[i] = true ↔ pertenece(s[i], e)) }
}
"""

def pertenece_a_cada_uno_v2(s:list[int], e:int) -> list[bool]:
    res:list[bool] = []
    numero_a_lista: list[int] = []
    for i in range(len(s)):
        numero_a_lista.append(s[i])
        print("Primer print", numero_a_lista)
        if pertenece(numero_a_lista,e):
            res.append(True)
        else:
            res.append(False)
        numero_a_lista.remove(s[i])
        print("Primer print", numero_a_lista)
    print(s) 
    return res

print("Pertenece a cada uno version 2", pertenece_a_cada_uno_v2([1,2,3], 3))


"""
3. problema pertenece a cada uno version 3 (in s:seq⟨seq⟨Z⟩⟩, in e:Z) : seq⟨Bool⟩ {
requiere: { T rue }
asegura: { |res| = |s| }
asegura: { Para todo i ∈ Z si 0 ≤ i < |s| → (res[i] = true ↔ pertenece(s[i], e)) }
}
"""

#PREGUNTAR: SON EL MISMO PROBLEMA PERO CON ESPECIFICACIONE SCRITA DISTINTA? EL out DE LA ESPECIFICACION ES EQUIVALENTE A HACER UN RETURN?

def pertenece_a_cada_uno_v3(s:list[int], e:int) -> list[bool]:
    res:list[bool] = []
    numero_a_lista: list[int] = []
    for i in range(len(s)):
        numero_a_lista.append(s[i])
        print("Primer print", numero_a_lista)
        if pertenece(numero_a_lista,e):
            res.append(True)
        else:
            res.append(False)
        numero_a_lista.remove(s[i])
        print("Primer print", numero_a_lista)
    print(s) 
    return res

print("Pertenece a cada uno version 3", pertenece_a_cada_uno_v3([1,2,3], 3))

# Ejercicio 6

"""
1. problema es matriz (in s:seq⟨seq⟨Z⟩⟩) : Bool {
requiere: { T rue }
asegura: { res = true ↔ (|s| > 0) ∧ (|s[0]| > 0) ∧ (Para todo i ∈ Z si 0 ≤ i < |s| → |s[i]| = |s[0]|) }
}
"""

def es_matriz(s: list[list[int]]) -> bool:
    res: bool = True
    if (len(s) <= 0) or (len(s[0])<=0):
        res = False
    elif (len(s) > 0) and (len(s[0])>0):
        for i in range(len(s)):
            if ((len(s[0])>1) and (len(s) == 1)) or (len(s[i]) != len(s[0])):
                res = False
    return res

print("Es matriz", es_matriz([[0,1,2],[2,1,6],[]]))

"""
2. problema filas ordenadas (in m:seq⟨seq⟨Z⟩⟩, out res: seq⟨Bool⟩) {
requiere: { esM atriz(m) }
asegura: { Para todo i ∈ Z si 0 ≤ i < |res| → (res[i] = true ↔ ordenados(s[i])) }
}

Nota: Reutilizar la funci´on ordenados() implementada previamente para listas
"""

def filas_ordenadas(s:list[list[int]]) -> list[bool]:
    res: list[bool] = []
    for i in range(len(s)):
        res.append(ordenados(s[i]))
    return res

print("filas ordenadas de matriz", filas_ordenadas([
    [1,2,3,4,40],
    [2,3,1000,1,7],
    [9,8,7,4,8],
    [1,2,3,4,10],
    [8,9,10,20,30]
]))

"""
3. problema columna (in m:seq⟨seq⟨Z⟩⟩, in c: Z) : seq⟨Z⟩ {
requiere: { esM atriz(m) }
requiere: { c < |m[0]| }
requiere: { c ≥ 0 }
asegura: { Devuelve una secuencia con exactamente los mismos elementos de la columna c de la matriz m, en
el mismo orden que aparecen }
}
"""

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


"""
4. problema columnas ordenadas (in m:seq⟨seq⟨Z⟩⟩) : seq⟨Bool⟩ {
requiere: { esM atriz(m) }
asegura: { Para todo ´ındice de columna c: 0 ≤ c < |m[0]| → (res[c] = true ↔ ordenados(columna(m, c))) }
asegura: {|res| = |m[0]|}
}

Nota: Reutilizar la funci´on ordenados() implementada previamente para listas
"""

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

"""
5. problema transponer (in m:seq⟨seq⟨Z⟩⟩) : seq⟨seq⟨Z⟩⟩ {
requiere: { esM atriz(m) }
asegura: { Devuelve mt (o sea la matriz transpuesta) }
}

Nota: Usar columna() para ir obteniendo todas las columnas de la matriz.
"""

def trasponer(m:list[list[int]]) -> list[list[int]]:
    res: list[list[int]] = []
    for i in range(len(m)):
        res.append(devuelve_columna(m,i))
    return res

print("Matriz traspuesta", trasponer([
    [1,2,2,3,4],
    [2,3,1000,1,7],
    [9,8,7,4,8],
    [1,2,3,4,10],
    [8,9,10,20,30]
]))

"""
6. Ta-Te-Ti Tradicional:
problema quien gana tateti (in m:seq⟨seq⟨Char⟩⟩) : Z {
requiere: { esMatriz(m) }
requiere: { |m| = 3 }
requiere: { |m[0]| = 3 }
requiere: { En la matriz si hay 3 X alineadas verticalmente =⇒ no hay 3 O alineadas verticalmente }
requiere: { En la matriz si hay 3 O alineadas verticalmente =⇒ no hay 3 X alineadas verticalmente }
requiere: { En la matriz si hay 3 X alineadas horizontalmente =⇒ no hay 3 O alineadas horizontalmente }
requiere: { En la matriz si hay 3 O alineadas horizontalmente =⇒ no hay 3 X alineadas horizontalmente }
requiere: { Para todo i,j ∈ {0, 1, 2} =⇒ m[i][j] = X ∨ m[i][j] = O ∨ m[i][j] = ” ”}
asegura: { Si hay 3 O alineadas verticalmente, horizontalmente o en diagonal, devuelve 0 }
asegura: { Si hay 3 X alineadas verticalmente, horizontalmente o en diagonal, devuelve 1 }
asegura: { Si no hay ni 3 X, ni 3 O alineadas verticalmente, horizontalmente o en diagonal, devuelve 2 }
}
"""
