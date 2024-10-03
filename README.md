# Teoría de Algoritmos - TP1

Trabajo Práctico N°1 de la materia Teoría de Algoritmos del curso Buchwald-Genender, Facultad de Ingeniería de la Universidad de Buenos Aires (FIUBA).


## Integrantes:
- Victoria Avalos - 108434 
- Santiago Tissoni - 103856  
- Facundo Monpelat - 92716 


## Instrucciones de uso

### Ejecución con un archivo
Desde la carpeta base del trabajo ejecutar el siguiente comando:

`python3 algoritmo_greedy.py <ruta_archivo_txt>`

Dentro de la carpeta `tests_cases` se encuentran, separados por carpetas, tanto los casos proporcionados por la cátedra como tests propios. 

Para correr el programa con el set que se desee, se debe ingresar la ruta del archivo desde la carpeta base. Por ejemplo: 

`python3 algoritmo_greedy.py tests_cases/catedra/25.txt`

El usuario puede agregar un archivo con su propio set de monedas en la carpeta de tests_cases y ejecutarlo de la siguiente forma:

`python3 algoritmo_greedy.py tests_cases/<nombre_archivo.txt>`

El archivo debe contener los valores de las monedas uno al lado del otro separados únicamente por un punto y coma (`";"`). Se desestima el caso de que haya una cantidad par de monedas de mismo valor. Soporta tener un comentario en la primera línea que comience únicamente con `"#"`. No debe contener espacios ni líneas extra. 

Los resultados de las acciones individuales de cada jugador se guardarán en la carpeta `outputs`.

### Ejecución automatizada de los tests de la cátedra

Para ejecutar de forma automática todos los tests de la cátedra mediante el uso de la librería `unittest`, correr desde la carpeta root:

`python3 run_tests.py`
