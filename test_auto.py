import os
from algoritmo_greedy import problema_monedas

def test_autogenerated():
    path = "tests_cases/autogenerated"
    for file in os.listdir(path):
        if file.endswith(".txt"):
            with open(f"{path}/{file}", 'r') as f:
                lines = f.readlines()
                valores = list(map(int, lines[0].strip().split(';')))
                sophia, mateo, esperados = problema_monedas(valores)
            
                if sum(sophia) > sum(mateo):
                    print(f"Testing {file} Resultado: Sophia ganó")
                else:
                    print(f"Testing {file} Resultado: Mateo ganó")

if __name__ == "__main__":
    test_autogenerated()