# Problema del juego de las monedas
# sophia y Mateo juegan a un juego en el que tienen que elegir una moneda de una fila de monedas.
# Cada moneda tiene un valor asociado. Sofia empieza a jugar y luego juegan alternativamente.
# El juego termina cuando no quedan monedas en la fila.
# Sofia quiere maximizar la suma de los valores de las monedas que elige.
# Mateo quiere minimizar la suma de los valores de las monedas que elige.
# Implementa la función problema_monedas(fila) que recibe una lista de enteros fila con los valores de las monedas en la fila.
# La función debe devolver dos listas, la primera con los valores de las monedas que elige Sofia y la segunda con los valores de las monedas que elige Mateo.
from collections import deque


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


def tests():
    output_folder = "outputs"

    # Tests de la cátedra
    catedra_folder = "tests_cases/catedra"
    test_files = ["20", "25", "50", "100", "1000", "10000", "20000"]
    for i in range(0, len(test_files)):
        with open(f"{catedra_folder}/{test_files[i]}.txt", "r") as file:
            file.readline()
            fila = list(int(i) for i in file.readline().split(";"))
            sophia, mateo, esperados = problema_monedas(fila)
            ganancia_sophia = sum(sophia)
            ganancia_mateo = sum(mateo)

            print(f"Test {test_files[i]}\nGanancia Sophia: {ganancia_sophia}")
            print(f"Ganancia Mateo: {ganancia_mateo}")
            if ganancia_sophia > ganancia_mateo:
                print("Resultado: Sophia ganó.")
            else:
                print("Resultado: Sophia perdió.")

            print("")

            with open(f"{output_folder}/resultado_catedra_test_{i+1}.txt", "w") as output_file:
                output_file.write(f"Esperados: {'; '.join(esperados)}\n")
    # Tests propios
    test_folder = "tests_cases"
    test_files_propios = [
        "test1", "test2", "test3", "test4", "test5",
        "test6", "test7", "test8", "test9", "test10"
    ]
    print("")
    for i, test_file in enumerate(test_files_propios):
        with open(f"{test_folder}/{test_file}.txt", "r") as file:
            file.readline()
            fila = list(int(i) for i in file.readline().split(";"))
            sophia, mateo, esperados = problema_monedas(fila)
            ganancia_sophia = sum(sophia)
            ganancia_mateo = sum(mateo)

            print(f"Test propio {i+1}\nGanancia Sophia: {ganancia_sophia}")
            print(f"Ganancia Mateo: {ganancia_mateo}")
            if ganancia_sophia > ganancia_mateo:
                print("Resultado: Sophia ganó.")
            else:
                print("Resultado: Sophia perdió.")

            print("")

            with open(f"{output_folder}/resultado_test_propio{i+1}.txt", "w") as output_file:
                output_file.write(f"Esperados: {'; '.join(esperados)}\n")

if __name__ == "__main__":
    tests()
