from array import *
def pertenece (s: list[int], e:int) -> bool:
    for i in range(0,len(s),1):
        if s[i] == e:
            res: bool = True
            break
        else:
            res: bool = False
    return res

print (pertenece([1,2,3],3))

def perteneceBis (s: list[int], e:int) -> bool:
    cont=0
    while cont <= len(s) -1:
        if s[cont] == e:
            res: bool = True
            break
        else:
            res: bool = False
            cont +=1
    return res

print (perteneceBis([1,2,3],0))


def suma_total (s: list[int]) -> int:
    suma_elementos:int = 0
    for i in range(0,len(s),1):
        suma_elementos += s[i]
    return suma_elementos

print(suma_total([1,2,3,5]))

# Esto es un procedimiento, pues no devuelve nada pero si modifica el valor de entrada que recibe

def CerosEnPosicionesPares(s:list[int]) -> None:
    for i in range(0,len(s),1):
        if i%2==0:
            s[i]=0
        else:
            s[i]=s[i]
    print(s)

CerosEnPosicionesPares([1,2,3,4,5,6,7,8])

def CerosEnPosicionesPares2(s:list[int])->list[int]:
    res: list[int] = s.copy()
    for i in range(0,len(s),1):
        if i%2==0:
            res[i] = 0
        else:
            res[i]=s[i]
    print("Esta es la lista original", s)
    return res

print(CerosEnPosicionesPares2([1,2,3,4,5,6,7,8]))
