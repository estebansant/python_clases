# Dicts y archivos
from typing import TextIO

#Ejercicio 3.16

def promedio_estudiante(notas:list[tuple[str,float]], estudiante:str) -> float:
    res: float = 0
    suma_notas: float = 0
    cantidad_notas: int = 0
    for nombre,nota in notas:
        if nombre == estudiante:
            cantidad_notas += 1
            suma_notas += nota
    res = suma_notas/cantidad_notas
    return res

def calcular_promedio_por_estudiante(notas: list[tuple[str,float]]) -> dict[str, float]:
    res: dict[str,float]={}
    for estudiante, nota in notas:
        if estudiante not in res:
            res[estudiante] = promedio_estudiante(notas, estudiante)


    return res

print("El promedio del estudiante A es:", promedio_estudiante([("A",10), ("B",8), ("A",7)], "A"))
print("el promedio por estudiant es:", calcular_promedio_por_estudiante([("A",10), ("B",8), ("A",7), ("C", 2), ("B", 6)]))

# Ejercicio 19.1

def contar_lineas(nombre_archivo: str) -> int:
    archivo:TextIO = open(nombre_archivo, "r", encoding="utf-8")
    lineas: list[str] = archivo.readlines()
    archivo.close()
    return len(lineas)

archivo:str = "ejemplo.txt"
print("Cantidad de lineas del archivo:", contar_lineas(archivo))

# Ejercicio 22

def clonar_sin_comentarios(nombre_archivo_entrada: str, nombre_archivo_salida:str) -> None:
    archivo:TextIO = open(nombre_archivo_entrada, "r", encoding="utf-8")
    lineas: list[str] = archivo.readlines()
    archivo.close()
    lineas_nuevas: str = ""
    print(lineas)
    for i in range(len(lineas)):
        print(lineas[i][0])
        linea_limpia:str = lineas[i].strip()
        print(linea_limpia)
        if (linea_limpia[0] != "#"):
            lineas_nuevas += lineas[i]
    archivo_nuevo: TextIO = open(nombre_archivo_salida, "w", encoding="utf-8")
    archivo_nuevo.write(lineas_nuevas)
    archivo_nuevo.close()

archivo_entrada: str = "ejemplo.txt"
archivo_salida: str = "output.txt"

clonar_sin_comentarios(archivo_entrada, archivo_salida)
