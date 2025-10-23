# Parte 4: Archivos

# Ejercicio 19.1
'''
1. problema contar lineas (in nombre archivo: seq⟨Char⟩) : Z {
requiere: {nombre archivo es el path con el nombre de un archivo existente y accesible}
asegura: {res es igual a la cantidad de lı́neas que contiene el archivo indicado por nombre archivo}
}
'''


# Ejercicio 19.2
'''
2. problema existe palabra (in nombre archivo: seq⟨Char⟩, in palabra: seq⟨Char⟩) : Bool {
requiere: {nombre archivo es el path con el nombre de un archivo existente y accesible}
requiere: {palabra no es vacı́a}
asegura: {res es verdadero si y solo si palabra aparece al menos una vez en el archivo indicado por nombre archivo}
}
'''


# Ejercicio 19.3
'''
3. problema cantidad de apariciones (in nombre archivo: seq⟨Char⟩, in palabra: seq⟨Char⟩) : Z {
requiere: {nombre archivo es el path con el nombre de un archivo existente y accesible}
requiere: {palabra no es vacı́a}
asegura: {res es la cantidad de veces que palabra aparece en el archivo indicado por nombre archivo}
}
'''


# Ejercicio 20

'''
problema agrupar por longitud (in nombre archivo: seq⟨Char⟩) : Diccionario⟨Z, Z⟩ {
requiere: {nombre archivo es el path con el nombre de un archivo existente y accesible}
asegura: {Para cada longitud n tal que existe al menos una palabra de longitud n en el archivo indicado por nombre archivo,
res[n] es igual a la cantidad de palabras de esa longitud}
asegura: {No hay otras claves en res que no correspondan a longitudes de palabras presentes en el archivo}
}
Por ejemplo, el diccionario
{
1: 2 ,
2: 10 ,
5: 4
}
indica que se encontraron 2 palabras de longitud 1, 10 palabras de longitud 2 y 4 palabras de longitud 5. Para este ejercicio
se consideran como palabras todas aquellas secuencias de caracteres delimitadas por espacios en blanco.
'''


# Ejercicio 21

'''
problema la palabra mas frecuente (in nombre archivo: seq⟨Char⟩) : seq⟨Char⟩ {
requiere: {nombre archivo es un archivo existente y accesible que tiene, por lo menos, una palabra}
asegura: {res es una palabra que aparece en el archivo nombre archivo}
asegura: {No hay ninguna palabra contenida en el archivo nombre archivo que aparezca más veces que la palabra res }
}
Para resolver el problema se aconseja utilizar un diccionario de palabras.
'''


# Ejercicio 22

'''
problema clonar sin comentarios (in nombre archivo entrada: seq⟨Char⟩, in nombre archivo salida: seq⟨Char⟩) {
requiere: {nombre archivo entrada es el path con el nombre de un archivo existente y accesible}
requiere: {nombre archivo salida es el path con el nombre de un archivo que, si existe, se puede modificar, y si no
existe, se puede crear}
asegura: {El archivo indicado por nombre archivo salida contiene las mismas lı́neas y en el mismo orden que el archivo
nombre archivo entrada, excepto aquellas que comienzan con el carácter #}
}
Para este ejercicio vamos a considerar que una lı́nea es un comentario si tiene un ‘#’como primer carácter de la lı́nea, o si no
es el primer carácter, se cumple que todos los anteriores son espacios.
Por ejemplo, si se llama a clonar sin comentarios con un archivo con este contenido:
# esto es un comentario
# esto tambien
esto no es un comentario # esto tampoco
nombre archivo salida solo contendrá la última lı́nea:
esto no es un comentario # esto tampoco
'''


# Ejercicio 23

'''
problema invertir lineas (in nombre archivo entrada: seq⟨Char⟩, in nombre archivo salida: seq⟨Char⟩ ) {
requiere: {nombre archivo entrada es el path de un archivo de texto existente y accesible}
requiere: {nombre archivo salida es el path con el nombre de un archivo que, si existe, se puede modificar, y si no
existe, se puede crear}
asegura: {El archivo indicado por nombre archivo salida contiene las mismas lı́neas que el archivo nombre archivo entrada,
pero en orden inverso}
}
Por ejemplo, si el archivo contiene lo siguiente:
Esta es la primera linea .
Y esta es la segunda .
debe generar:
Y esta es la segunda .
Esta es la primera linea .
'''


# Ejercicio 24
'''
problema agregar frase al final (in nombre archivo: seq⟨Char⟩, in frase: seq⟨Char⟩ ) {
requiere: {nombre archivo es el path de un archivo existente y accesible}
requiere: {f rase no es vacı́a}
asegura: {f rase se agrega como una nueva lı́nea al final del archivo nombre archivo}
}
Este problema no crea una copia del archivo de entrada, sino que lo modifica.
'''


# Ejercicio 25
'''
Ejercicio 25. Dado un archivo de texto y una frase, implementar una función
agregar frase al principio(in nombre archivo : str, in frase : str), que agregue la frase al comienzo del archivo original
(similar al ejercicio anterior, sin hacer una copia del archivo).
problema agregar frase al principio (in nombre archivo: seq⟨Char⟩, in frase: seq⟨Char⟩ ) {
requiere: {nombre archivo es el path de un archivo existente y accesible}
requiere: {f rase no es vacı́a}
asegura: {f rase se agrega como primera lı́nea del archivo nombre archivo, desplazando las anteriores hacia abajo}
}
Este problema no crea una copia del archivo de entrada, sino que lo modifica.
'''



# Ejercicio 26
'''
Ejercicio 26. Implementar una solución para el siguiente problema.
problema listar textos de archivo (in nombre archivo: seq⟨Char⟩ ) : seq⟨seq⟨Char⟩⟩ {
requiere: {nombre archivo es el path de un archivo existente y accesible}
asegura: {res contiene exactamente los textos legibles que aparecen en el archivo nombre archivo}
}
Definimos un texto como legible si:
solo contiene secuencias de carácteres legibles (números, letras mayúsculas/minúsculas, espacios o ‘ ’(guión bajo)
tienen longitud >= 5
Referencia: https://docs.python.org/es/3/library/functions.html#open
Para resolver este ejercicio se puede abrir un archivo en modo binario ‘b’. Al hacer read() vamos a obtener
una secuencia de bytes, que al hacer chr(byte) nos va a devolver un carácter correspondiente al byte
leı́do.
Una vez implementada la función, probarla con diferentes archivos binarios (.exe, .zip, .wav, .mp3, etc).
'''



# Ejercicio 27

'''
problema calcular promedio por estudiante (in nombre archivo notas: seq⟨Char⟩, in nombre archivo promedios: seq⟨Char⟩)
{
requiere: {nombre archivo notas es el path de un archivo existente y accesible, con formato CSV: cada lı́nea tendrá
número de LU, materia, fecha y nota, todo separado por comas}
requiere: {nombre archivo promedios es el path de un archivo distinto, accesible para escritura}
asegura: {El archivo nombre archivo promedios contiene una lı́nea por estudiante del archivo nombre archivo notas,
con su LU y su promedio separados por una coma}
}
El contenido del archivo nombre archivo notas tiene el siguiente formato:
nro de LU ( str ) , materia ( str ) , fecha ( str ) , nota ( float )
Analizar el problema y modularizar el código apropiadamente. Una opción es implementar una función auxiliar que cumpla
la siguiente especificación.
problema promedio estudiante (in notas de estudiantes: seq⟨seq⟨Char⟩⟩, in lu: seq⟨Char⟩ ) : R {
requiere: {notas de estudiantes tiene el contenido del archivo de notas. Cada elemento de la lista es una lı́nea de ese
archivo, con formato CSV: tendrá número de LU, materia, fecha y nota, todo separado por comas}
requiere: {lu corresponde a una LU presente en notas de estudiantes}
asegura: {res es el promedio de las notas asociadas a lu en notas de estudiantes}
}
'''