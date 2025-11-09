from queue import Queue as Cola

# Ejercicio 1


def promedio_camas(piso: list[bool]) -> float:
    res: float = 0
    cont: int = 0
    for cama in piso:
        if cama == True:
            cont+=1
    
    res = cont/len(piso)
    return res

def nivel_de_ocupacion(camas_por_piso: list[list[bool]]) -> list[float]:
    res: list[float] = []

    for i in range(len(camas_por_piso)):
        ratio_camas: float = promedio_camas(camas_por_piso[i])
        res.append(ratio_camas)
    return res

camas_por_piso = [[True, False, True], [False, False, True],[True, True, True]]

print(nivel_de_ocupacion(camas_por_piso))

# Ejercicio 2

def cambiar_matriz(A:list[list[int]]) -> None:
    for i in range(len(A)):
        primer_valor = A[i][0]
        for j in range(len(A[i])):
            if (j == (len(A[i])-1)):
                A[i][j] = primer_valor
            else:
                A[i][j] = A[i][j+1]
        

A = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]

cambiar_matriz(A)

print(A)

# Ejercicio 3

def promedio_listas(s: list[int]) -> float:
    res: float = 0
    suma_items: int = 0
    for i in range(len(s)):
        suma_items += s[i]
    
    res = (suma_items / len(s))
    return res

def promedio_de_salidas(registro: dict[str, list[int]]) -> dict[str, tuple[int, float]]:
    res: dict[str, tuple[int,float]] = {}
    for amigo, salas in registro.items():
        cant_salas: int = 0
        tiempos_validos: list[int] = []
        promedio_de_salas: float = 0

        for i in salas:
            if (i >0) and (i < 61):
                tiempos_validos.append(i)
                cant_salas +=1

        print("Tiempos validos:" , tiempos_validos)

        if cant_salas>0:
            promedio_de_salas = promedio_listas(tiempos_validos)

        print(f"Promedio para {amigo}:", promedio_de_salas)
        res[amigo] = (cant_salas, promedio_de_salas)
    
    return res
            


print(promedio_de_salidas({"a":[61,60,59,58], "b":[1,2,3,0], "c": [14,13,15,28], "d": [0,0,0,0], "e": [61,61,61,61], "f": [1,0,0,60], "g": [0,0,0,60], "h": [1,0,0,61] }))

#Ejercicio 4

def reordenar_cola_priorizando_vips(filaClientes: Cola[tuple[str,str]]) -> Cola[str]:
    res: Cola[str] = Cola()
    copiaClientes: Cola[tuple[str,str]] = Cola()
    recoleccion_comunes: Cola(tuple[str,str]) = Cola()
    recoleccion_vip: Cola(tuple[str,str]) = Cola()

    ordenados_vip: Cola(tuple[str,str]) = Cola()
    ordenados_comun: Cola(tuple[str,str]) = Cola()

    while not filaClientes.empty():
        cliente = filaClientes.get()
        copiaClientes.put(cliente)
        if cliente[1] == "común":
            recoleccion_comunes.put(cliente)
        if cliente[1] == "vip":
            recoleccion_vip.put(cliente)
    
    while not copiaClientes.empty():
        cliente = copiaClientes.get()
        filaClientes.put(cliente)

    while not recoleccion_vip.empty():
        res.put(recoleccion_vip.get())
    
    while not recoleccion_comunes.empty():
        res.put(recoleccion_comunes.get())
    
    print("cola antes de salir de la funcion", imprimir_cola(filaClientes))
    return res
    
filaClientes: Cola(tuple[str,str]) = Cola()
filaClientes.put(("a", "común"))
filaClientes.put(("b", "vip"))
filaClientes.put(("c", "vip"))
filaClientes.put(("d", "común"))
filaClientes.put(("e", "vip"))
filaClientes.put(("f", "común"))


def imprimir_cola(cola: Cola) -> list:
    res: list = []
    colaCopia: Cola = Cola()
    while not cola.empty():
        item = cola.get()
        colaCopia.put(item)
        res.append(item)
        
    while not colaCopia.empty():
        item = colaCopia.get()
        cola.put(item)
    
    return res

print("cola original", imprimir_cola(filaClientes))
print("Cola reordenada", imprimir_cola(reordenar_cola_priorizando_vips(filaClientes)))
print("cola despues", imprimir_cola(filaClientes))

