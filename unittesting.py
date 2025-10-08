def suma(a:int,b:int) -> int:
    res:int = a+b
    return res

def test_suma_positiva(self):
    self.assertEqual(suma(2,3),5)

def es_multiplo_de(n:int, m: int) -> bool:
    if n%m == 0:
        return True
    else:
        return False
    
def devolver_el_doble_si_es_par(n:int)->int:
    if n%2==0:
        res: int= n*2
    else:
        res: int = n
    return res

def fahrenheit_a_celsius(temp_far:float) -> float:
    return ((temp_far-32)*(5/9))

"""
Ejercicio 2. Implementar y escribir casos de test para la funcion
es primo (n: int)-> bool, que toma como entrada un entero y
devuelve si es primo o no.
"""

def es_primo(n:int)->bool:
    for i in range (n-1, 0, -1):
        if (n%i==0 and i!=1):
            return False
        else:
            return True

print(es_primo(10))
