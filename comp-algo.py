# Ejercicio 4
# Ítem 2
def producto_1(n: int) -> int:
    res: int = 1 #1 OE
    i: int = 1 #1 OE
    while i <= n: #n + 1 OE donde n veces el ciclo while da True, y 1 vez da False
        res = res * i #2 OE (se ejecuta n veces)
        i = i + 1 #2 OE (se ejecuta n veces)
    return res #1 OE

# T_producto1(n) = 1+1+(n+1) + 2n + 2n +1 
#                = 4 + 5n

# Ítem 4
def producto_3(n: int) -> int:
    res: int = 1 #1 OE
    i: int = 1 #1 OE
    while i <= n: #n+1 OE
        j: int = 1 #1 OE (n veces)
        while j <= n: #n+1 OE (n*n veces da True, n veces da False)
            res = res * i * j #3 OE (n*n veces)
            j = j + 1 #2 OE (n*n veces)
        i = i + 1 #2 OE (n veces)
    return res #1 OE

# T_producto_3(n) = 1+1+n*(1+1+n*(1+3+2)+1+2)+1+1
#                 = 4 + 5n + 6*(n**2)

# Ítem 7
def producto_6(n: int) -> int:
    res: int = 1 #1 OE
    i: int = 1 #1 OE
    while i <= 2**n: #n+2+1 OE
        producto: int = 1 # 1 OE n veces
        j: int = 1 # 1 OE n veces
        while j <= n: # n+1 OE n veces
            if (i // (2 ** (j-1))) % 2 == 1:
                producto = producto * j
            else:
                producto = producto * 1
            j = j + 1
        i = i + 1
        res = res * producto
    return res


# Ejercicio 5.5
# Requiere: es matriz cuadrada (#filas = #columnas)
def diagonal_principal_v1(m: list[list[int]]) -> list[int]:
    res: list[int] = [] #1 OE
    n: int = len(m) #1 + T_len(m) OE
    i: int = 0 #1 OE
    while i < n: # n+1 veces -> (n veces true, 1 vez false)
        j: int = 0 # 1 OE n veces
        while j < n: # n+1 veces -> (n veces true, 1 vez false)
            if i == j: # 1 OE n*n veces
                res.append(m[i][j]) # 2*T_[.](m) + T_append(i)
            j = j + 1 # 2 OE n*n veces
        i = i + 1 # 2 OE n veces
    return res # 1 OE

# T_diagonal_principal(m) = 1+1+T_len(m) +1+ n*(1+1+n*(1+1*(2*T_[.](m) + T_append(i))+2)+2)+1
#                         = T_len(m) + 4 + n*(4+n*(3+(2*T_[.](m) + T_append(i))))
#                         = T_len(m) + 4 + 4n + 3(n**2) + sum{i->n}*(2*T_[.](m) + T_append(i))


# Requiere: es matriz cuadrada (#filas = #columnas)
def diagonal_principal_v2(m: list[list[int]]) -> list[int]:
    res: list[int] = []
    n: int = len(m)
    i: int = 0
    while i < n:
        res.append(m[i][i])
        i = i + 1
    return res


# Ejercicio 6.1
def contar_pares(s: list[int]) -> int:
    res: int = 0
    i: int = 0
    while i < len(s):
        if s[i] % 2 == 0:
            res = res + s[i]
        i = i + 1
    return res


# Ejercicio 6.2
def suma_hasta_umbral(s: list[int], umbral: int) -> int:
    res: int = 0
    i: int = 0
    while i < len(s) and s[i] < umbral:
        res = res + s[i]
        i = i + 1
    return res
