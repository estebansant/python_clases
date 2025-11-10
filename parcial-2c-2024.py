from queue import Queue as Cola

# Ejercicio 1 (2,25 puntos)
# Implementar la función subsecuencia_mas_larga especificada (todos_consecutivos no es testeado)

# problema subsecuencia_mas_larga (in v: seq⟨Z⟩) : ZxZ {
#   requiere: { La longitud de v es distinto de 0 }
#   asegura: { Sea x la primera subsecuencia más larga en v tal que vale todos_consecutivos(x), la primera componente de res es igual a |x| y la segunda es igual al índice en v donde comenzaría x }
# }

# problema todos_consecutivos (in v: seq⟨Z⟩) : Bool {
#   asegura: { res == True <==> cada par de elementos adyacentes en v son números consecutivos, es decir, que su diferencia es igual a 1 }
# }

def todos_consecutivos(v:list[int]) -> bool:
    res: bool = True
    for i in range(1,len(v)):
        if v[i] != v[i-1] + 1:
            res = False
    return res


def subsecuencia_mas_larga(v:list[int]) -> tuple[int,int]:
    mejor_longitud: int = 1
    mejor_inicio: int = 0

    for i in range(len(v)):
        subsecuencia_actual: list[int] = []

        for j in range(i, len(v)):
            subsecuencia_actual.append(v[j])

            if todos_consecutivos(subsecuencia_actual):
                
                longitud_actual = len(subsecuencia_actual)
                
                if longitud_actual > mejor_longitud:
                    mejor_longitud = longitud_actual
                    mejor_inicio = i

    return (mejor_longitud, mejor_inicio)

        
print(subsecuencia_mas_larga([1,2,3,4,7,6,8,9,10,11,12,13,14,15,20,21,22]))
print(subsecuencia_mas_larga([1,2,3,20,21,22,8,9,10,13]))


# Ejercicio 2 (2,25 puntos)
# Ana tiene exámenes de respuesta Verdadero ó Falso. Ella sabe que en cada examen la cantidad 
# de respuestas correctas cuyo valor es Falso es igual a la cantidad de respuestas correctas 
# cuyo valor es Verdadero. Tenemos el historial de las respuestas de cada exámen dados por Ana 
# en una cola. En cada uno Ana respondió todas las preguntas.

# problema mejor_resultado_de_ana (in examenes: Cola⟨ seq⟨Bool⟩ ⟩) : seq⟨Z⟩ {
#   requiere:{ Cada elemento de examenes es no vacío y tiene longitud par }
#   asegura: { res tiene la misma cantidad de elementos que examenes }
#   asegura: { res[i] es igual a la máxima cantidad de respuestas correctas que Ana podría haber respondido en el i-ésimo exámen resuelto en examenes, para 0 <= i < cantidad de elementos de examenes }
# }

def imprimir_cola(cola: Cola) -> list:
    res: list = []
    colaCopia: Cola= Cola()

    while not cola.empty():
        colaCopia.put(cola.get())

    while not colaCopia.empty():
        item = colaCopia.get()
        cola.put(item)
        res.append(item)

    return res

examenes: Cola[list[bool]] = Cola()
examenes.put([True, False])
examenes.put([False, False])
examenes.put([True, False])
examenes.put([True, True])
examenes.put([False, True])
examenes.put([True, False])

print("Examenes", imprimir_cola(examenes))

def mejor_resultado_de_ana(examenes: Cola[list[bool]]) -> list[int]:
    res: list[int] = []
    examenesCopia: Cola[list[bool]] = Cola()

    while not examenes.empty():
        item = examenes.get()
        examenesCopia.put(item)
        if item[0] != item [1]:
            res.append(2)
        else:
            res.append(1)
    
    while not examenesCopia.empty():
        examenes.put(examenesCopia.get())

    return res
    
print("Mejores resultados de examenes posibles:", mejor_resultado_de_ana(examenes))



# Ejercicio 3 (2,25 puntos)
# problema cambiar_matriz(inout A: seq⟨seq⟨Z⟩⟩) {
#   requiere: { Todas las filas de A tienen la misma longitud }
#   requiere: { El mínimo número que aparece en A es igual a 1 }
#   requiere: { El máximo número que aparece en A es igual a #filas de A por #columnas de A }
#   requiere: { No hay enteros repetidos en A }
#   requiere: { Existen al menos dos enteros distintos en A }
#   modifica: { A }
#   asegura: { A tiene exactamente las mismas dimensiones que A@pre }
#   asegura: { El conjunto de elementos que aparecen en A es igual al conjunto de elementos que aparecen en A@pre }
#   asegura: { A[i][j] != A@pre[i][j] para todo i, j en rango }
# }

def cambiar_matriz(A:list[list[int]]) -> None:
    for i in range(len(A)):
        primer_elemento: int = A[i][0]
        for j in range(len(A[i])):
            if (j == (len(A[i])-1)):
                A[i][len(A[i])-1] = primer_elemento
            else:
                A[i][j] = A[i][j+1]

A:list[list[int]]= [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print("Matriz antes",A)
cambiar_matriz(A)
print("Matriz despues", A)



# Ejercicio 4 (2,25 puntos)
# Tenemos un texto que contiene palabras. Por simplicidad, las palabras están separadas únicamente por uno o más espacios.

# problema palabras_por_vocales (in texto: string): Diccionario⟨Z,Z⟩ {
#   requiere: { Si existe una letra vocal en texto, esta no lleva tildes, diéresis, ni ningún otro símbolo }
#   asegura: { Si existe una palabra en texto con x vocales en total, x es clave de res }
#   asegura: { Las claves de res representan la cantidad total de vocales de una palabra, y cada valor corresponde a la cantidad de palabras en texto con ese número de vocales. }
#   asegura: { Los valores de res son positivos }
# }

def separar_palabras(texto: str) -> list[str]:
    res: list[str] = []
    palabra_actual: str = ""

    for i in range(len(texto)):
        if texto[i] == " ":
            if palabra_actual != "":
                res.append(palabra_actual)
            palabra_actual = ""
        else:
            palabra_actual += texto[i]
    
    if palabra_actual != "":
        res.append(palabra_actual)

    return res


def palabras_por_vocales(texto: str) -> dict[int, int]:
    res: dict[int,int] = {}
    vocales: list[str] = ["a", "e", "i", "o", "u"]
    cant_vocales: list[int] = []
    llaves: list[int] = []
    valores: list[int] = []

    palabras: list[str] = (separar_palabras(texto))

    for palabra in palabras:
        cont_actual: int = 0

        for letra in palabra:
            if letra in vocales:
                cont_actual += 1
        
        if cont_actual > 0:
            cant_vocales.append(cont_actual)

    print(cant_vocales)

    for num in cant_vocales:
        if num not in llaves:
            llaves.append(num)
    
    print(llaves)

    for llave in llaves:
        cont_llave: int = 0
        for cantidad in cant_vocales:
            if llave == cantidad:
                cont_llave +=1
        valores.append(cont_llave)

    print(valores)

    if len(valores) == len(llaves):
        cont_long: int = 0
        while cont_long < len(llaves):
            res[llaves[cont_long]] = valores[cont_long]
            cont_long += 1

    return res
        


texto: str = "esto es una oracion que puede ir   en texto perfectamente y sin problemas"
print(separar_palabras(texto))
print(palabras_por_vocales(texto))



