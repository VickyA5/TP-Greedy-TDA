# Problema del juego de las monedas
# sophia y Mateo juegan a un juego en el que tienen que elegir una moneda de una fila de monedas.
# Cada moneda tiene un valor asociado. Sofia empieza a jugar y luego juegan alternativamente.
# El juego termina cuando no quedan monedas en la fila.
# Sofia quiere maximizar la suma de los valores de las monedas que elige.
# Mateo quiere minimizar la suma de los valores de las monedas que elige.
# Implementa la función problema_monedas(fila) que recibe una lista de enteros fila con los valores de las monedas en la fila.
# La función debe devolver dos listas, la primera con los valores de las monedas que elige Sofia y la segunda con los valores de las monedas que elige Mateo.
from collections import deque
import os
import sys


def problema_monedas(fila):
    sophia = []
    mateo = []
    esperados = []

    fila = deque(fila)

    while len(fila) > 0:
        # Turno de Sophia
        if fila[0] > fila[-1]:
            sophia.append(fila[0])
            fila.popleft()
            esperados.append("Primera moneda para Sophia")
        else:
            sophia.append(fila[-1])
            fila.pop()
            esperados.append("Última moneda para Sophia")

        if len(fila) == 0:
            break

        # Turno de Mateo
        if fila[0] > fila[-1]:
            mateo.append(fila[-1])
            fila.pop()
            esperados.append("Última moneda para Mateo")
        else:
            mateo.append(fila[0])
            fila.popleft()
            esperados.append("Primera moneda para Mateo")

    return sophia, mateo, esperados


def tests(file_path):
    output_folder = "outputs"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    try:
        with open(file_path, "r") as file:
            first_line = file.readline().strip()
            if first_line.startswith("#"):
                fila = list(int(i) for i in file.readline().strip().split(";") if i)
            else:
                fila = list(int(i) for i in first_line.split(";") if i)
            
            sophia, mateo, esperados = problema_monedas(fila)
            ganancia_sophia = sum(sophia)
            ganancia_mateo = sum(mateo)

            print(f"Archivo {file_path}\nGanancia Sophia: {ganancia_sophia}")
            print(f"Ganancia Mateo: {ganancia_mateo}")
            if ganancia_sophia > ganancia_mateo:
                print("Resultado: Sophia ganó.")
            else:
                print("Resultado: Sophia perdió.")

            print("")

            output_filename = os.path.basename(file_path).replace(".txt", "_resultado.txt")
            with open(f"{output_folder}/{output_filename}", "w") as output_file:
                output_file.write(f"Esperados: {'; '.join(map(str, esperados))}\n")
    except Exception as e:
        print(f"Error al procesar el archivo {file_path}: {e}")

        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Argumentos incorrectos.\nUso: python3 problema.py <archivo_set_de_datos.txt>")
    else:
        file_path = sys.argv[1]
        tests(file_path)
