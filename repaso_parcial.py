# Ejercicios de Parciales

# Ejercicio 1
def promedio_camas_ocupadas(s:list[bool]) -> float:
    res: float = 0
    suma: int = 0
    for i in range(len(s)):
        if s[i] == True:
            suma += 1
    res = suma/len(s)
    return res

def nivel_de_ocupacion(camas_por_piso: list[list[bool]]) -> list[float]:
    res: list[float] = []
    for i in range(len(camas_por_piso)):
        print("Respuesta antes del append", res)
        res.append(promedio_camas_ocupadas(camas_por_piso[i]))
        print("Respuesta despues del append", res)
    print(camas_por_piso)
    return res

print(nivel_de_ocupacion([[True], [False, False, True], [True, True, True]]))

# Ejercicio 2

def reordenar_fila(s:list[int]) -> list[int]:
    res: list[int] = []
    if len(s)%2 == 0:
        for i in range(len(s)-1, -1, -1):
            print(s[i])
            res.append(s[i])
    else:
        for i in range(len(s)-1, -1, -1):
            print(s[i])
            res.append(s[i])
        elemento_del_medio: int = int(((len(res)+1)/2)-1)
        res.append(res[elemento_del_medio])
        elemento_del_medio_despues_del_append:int = int(((len(res)/2))-1)
        print(res)
        res.remove(res[elemento_del_medio_despues_del_append])
        print(res)
    return res

print("Reordenar fila", reordenar_fila([1,2,3,4,5,6,7]))

def reordenar_filas_par_a_par(s: list[int], m:list[int]) -> list[list[int]]:
    res: list[list[int]] = []
    res.append(m)
    res.append(s)
    return res

def cambiar_matriz(A:list[list[int]]) -> None:
    # if (len(A) > 1) and (len(A)%2 == 0):
    #     for elem in A:
    #         print(A)
    #         A.remove(elem)
    #         print(A)
    #         A.append(elem)
    #         print(A)
    #     print("le paso la ultima fila")
    #     A.append(reordenar_fila(A[-1]))
    #     print(A)
    #     A.remove(A[-2])
    #     print(A)
    # elif (len(A)>1) and (len(A)%2 != 0):
    #     for elem in A:
    #         print(A)
    #         A.remove(elem)
    #         print(A)
    #         A.append(elem)
    #         print(A)
    #     print("le paso la ultima fila")
    #     A.append(reordenar_fila(A[-1]))
    #     print(A)
    #     A.remove(A[-2])
    #     print(A)
    if len(A) > 1:
        for i in range(len(A)):
            for j in range(len(i)):
                print(A)
                reordenar_filas_par_a_par(A[i][j], A[i][(j+1)%len(A)]) # Me va a generar muchos problemas. Le agrego modulo de longitud para que en el ultimo valor i de la matriz, vuelvo al principio de A. Usar A[i+1] se pasa de la longitud de A. La misma logica aplica para en vez de modificar las columnas, modificar las filas. Toca aplicar la logica usando esta nueva forma de pensar la matriz. Lo mejor es intercambiar las filas.
    elif len(A) == 1:
        print(A)
        A.append(reordenar_fila(A[0]))
        print(A)
        A.remove(A[0])
        print(A)

A:list[list[int]] = [[1,2,3],[4,5,6],[7,8,9],[11,12,13]]
print("Cambiar matriz", cambiar_matriz(A))
print("Nuevos valores para A:", A)

# Puedo probar a agrupar las primeras 2 filas de la matriz en un lista e intercambiar posiciones entre ellas, luego hacer lo mismo para las filas 2 y 3, luego 3 y 4 y asi sucesivamente. Apendeo nueva lista con dos elemente [0] y despues el [1]
