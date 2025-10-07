# Para activar el ambiente de desarrollo hacer: source ruta/bin/activate
# Ejercicio 1: Definir las siguientes funciones y procedimientos:

import numpy as np
import math

# 1)

def imprimir_hola_mundo():
    print("Hola, Mundo!")

imprimir_hola_mundo()

# 2)

def imprimir_un_verso():
    print("If you wanna roll me \nThen you gotta roll me all night long \nAnd if you wanna use me \nThen you gotta use me 'til I'm gone")

imprimir_un_verso()

# 3)
def raizDe2() -> float:
    return(round(math.sqrt(2),4))

print(raizDe2())

# 4)
def factorial_de_dos() ->int:
    return(math.factorial(2))

print( factorial_de_dos())

# 5)
def perimetro() -> float:
    print( 2*math.pi)

perimetro()

# Ejercicio 2: Definir las siguientes funciones y procedimientos con parámetros

# 1)

def imprimir_saludo(nombre: str):
    print("Hola", nombre)

imprimir_saludo("Esteban")

# 2)
def raiz_cuadrada_de(n:float) -> float:
    return (np.sqrt(n))

print(raiz_cuadrada_de(9))

# 3)

def fahrenheit_a_celsius(temp_far:float) -> float:
    return ((temp_far-32)*(5/9))

print(fahrenheit_a_celsius(72))

# 5)
def es_multiplo_de(n:int, m: int) -> bool:
    if n%m == 0:
        return True
    else:
        return False

print(es_multiplo_de(6,4))

# 6)

def es_par(n:int) -> bool:
    return es_multiplo_de(n,2) == True

print(es_par(7))

# 7
def cantidad_de_pizzas(comensales:int, min_cant_de_porciones:int) -> int:
    porciones_pizza:int = 8
    porciones_comidas: int = comensales * min_cant_de_porciones
    res: int = math.ceil((porciones_comidas)/porciones_pizza)
    if(porciones_comidas % porciones_pizza ==0):
        res = res + 1
        print("Para que sobren pedazos de pizza")
    else:
        res=res
    return res

print("La cantidad de pizzas necesarias para que todos coman es:", cantidad_de_pizzas(8,3))

# Ejercicio 3: Resuelva los siguientes ejercicios utilizando los operadores lógicos and, or, not . No use if.

#1)
def alguno_es_0(n1:int,n2:int) -> bool:
    return n1==0 or n2==0

print("Alguno es cero:", alguno_es_0(0,2))

#2)
def ambos_son_0(n1:int,n2:int) -> bool:
    return n1==0 and n2==0

print("Ambos son cero:", ambos_son_0(1,0))

#3)
def es_nombre_largo(nombre: str) -> bool:
    return (3 <= len(nombre) and len(nombre) <= 8)

print(es_nombre_largo("Juan"))

#4)

def es_bisiesto(anio:int)->bool:
    return (anio%4==0) and (anio%400==0 or not anio%100==0)

print("El año ingresado es bisiesto", es_bisiesto(2200))

#Ejercicio 4: Resolver este ejercicio usando las funciones de python min y max
#1) Definir la funcion peso_pino

def peso_pino(altura:float) -> float:
    altura_en_cm: float=altura*100
    if altura_en_cm <=300:
        peso: float = altura_en_cm*3
    else:
        ultimos_metros:float = altura_en_cm - 300
        peso:float = 3*300 + ultimos_metros*2
    return peso

print("Peso del pino es:", peso_pino(3.5))

# Los pinos se usan para llevarlos a una fábrica de muebles, a la que le sirven árboles de entre 400 y 1000 kilos, un pino fuera de este rango no le sirve a la fábrica.

#2) Definir la función es_peso_util , recibe un peso en kg y responde si un pino de ese peso le sirve a la fábrica.

# PREGUNTAR COMO ASIGNARLE UN TIPO A UNA FUNCION QUE SE PASA COMO PARAMETRO
def es_peso_util(peso_pino) -> bool:
    return (max(399,peso_pino) >= 400) and (min(1001,peso_pino) <= 1000)

print("El peso del pino le sirve a la fabrica:", es_peso_util(peso_pino(1.3333333334)))

# 3) Definir la función sirve_pino , recibe la altura de un pino y responde si un pino de ese peso le sirve a la fábrica.

def sirve_pino(altura: float) -> bool:
    return ((altura >= 1.3333333333333333334) and (altura <= 3.5))

print("El pino le sirve a la fabrica", sirve_pino(1.5))

# Ejercicio 5: Implementar los siguientes problemas de alternativa condicional (if/else).

# 1)

def devolver_el_doble_si_es_par(n:int)->int:
    if n%2==0:
        res: int= n*2
    else:
        res: int = n
    return res

print(devolver_el_doble_si_es_par(40))

# 2)

def devolver_valor_si_es_par_sino_el_que_sigue(n:int) -> int:
    if n%2==0:
        return n
    else:
        return n+1
print(devolver_valor_si_es_par_sino_el_que_sigue(39))

#3)
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(n:int)->int:
    if n%9==0:
        return n*3
    elif n%3==0:
        return n*2
    else:
        return n
print(devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(18))

#4) 

def lindo_nombre(nombre: str) -> str:
    if len(nombre)>=5:
        msg: str= "Tu nombre tiene muchas letras!"
    else:
        msg: str= "Tu nombre tiene menos de 5 caracteres"
    return msg

print(lindo_nombre("Esteban"))

#5)

def elRango(n:int) -> None:
    if n<5:
        print("Menor a 5")
    elif (n>10 and n<20):
        print("Entre 10 y 20")
    elif n>20:
        print("Mayor a 20")
    else:
        print("No hay rango definido")

elRango(12)

#6)

def a_laburar(sexo: str, edad:int) -> None:
    if (edad <18) or (edad >=60 and sexo=="F"):
        print("Andá de vacaciones")
    elif (edad <18) or (edad >=65 and sexo=="M"):
        print("Andá de vacaciones")
    else:
        print("Te toca trabajar")

a_laburar("M",65)
a_laburar("F",65)
a_laburar("F",18)
a_laburar("M",16)
a_laburar("M",22)
a_laburar("F",40)

#Ejercicio 6: Implementar las siguientes funciones usando repetición condicional while:

#1)

def imprimir_1_al_10() -> None:
    cont = 1
    while ((cont >=1) and (cont<=10)):
        print(cont)
        cont=cont+1

imprimir_1_al_10()

# 2)

def pares_entre_10_40() -> None:
    cont: int = 10
    while cont <=40:
        if cont%2==0:
            print(cont)
            cont +=1
        else:
            cont +=1

pares_entre_10_40()

#3)

def eco_10()->None:
    cont = 1
    while ((cont >=1) and (cont<=10)):
        print("eco")
        cont=cont+1
    
eco_10()

#4)

def cuenta_regresiva(t:int) -> None:
    while t >=1:
        print(t)
        t: int=t-1
    print("Despegue!")

cuenta_regresiva(40)

#5)

def viaje_temporal(partida:int,llegada:int) -> None:
    while partida > llegada:
        partida: int = partida - 1
        print("Viajó un año al pasado, estamos en el año:", partida)
    
viaje_temporal(2025,2000)

#6)

def viaje_aristoteles(partida:int) -> None:
    while partida > -384:
        partida: int = partida - 20
        print("Viajó 20 años al pasado, estamos en el año:", partida)
    
viaje_aristoteles(2025)

#Ejercicio 7: Funciones del ejercicio 6 pero usando for num in range (i,f,p)

def imprimir_1_al_10() -> None:
    for num in range (1,11,1):
        print(num)

imprimir_1_al_10()

# 2)

def pares_entre_10_40() -> None:
    for num in range(10,41,2):
        print(num)

pares_entre_10_40()

#3)

def eco_10()->None:
    for num  in range (1,11,1):
        print("eco")
    
eco_10()

#4)

def cuenta_regresiva(t:int) -> None:
    for num in range (t,0,-1):
        print(num)
    print("Despegue!")

cuenta_regresiva(40)

#5)

def viaje_temporal(partida:int,llegada:int) -> None:
    for num in range (partida, llegada-1,-1):
        print("Viajó un año al pasado, estamos en el año:", num)
    
viaje_temporal(2025,2000)

#6)

def viaje_aristoteles(partida:int) -> None:
    for num in range(partida-20, -384-20,-20):
        print("Viajó 20 años al pasado, estamos en el año:", num)
    
viaje_aristoteles(2025)


