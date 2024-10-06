import unittest
from algoritmo_greedy import problema_monedas

class TestProblemaMonedas(unittest.TestCase):
    def leer_archivo(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            valores = list(map(int, lines[1].strip().split(';')))
        return valores
    
    def obtener_resultado_esperado(self, test_name):
        with open('ResultadosEsperados.txt', 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                if line.strip().startswith(test_name):
                    while i < len(lines) and not lines[i].startswith("Ganancia de Sophia:"):
                        i += 1
                    if i < len(lines):
                        return int(lines[i].split(":")[1].strip())
            return None

    def test_20(self):
        valores = self.leer_archivo('tests_cases/catedra/20.txt')
        resultado_esperado = self.obtener_resultado_esperado("20.txt") #7165
        resultado = problema_monedas(valores)
        self.assertEqual(sum(resultado[0]), resultado_esperado)

    def test_25(self):
        valores = self.leer_archivo('tests_cases/catedra/25.txt')
        resultado_esperado = self.obtener_resultado_esperado("25.txt") #9635
        resultado = problema_monedas(valores)
        self.assertEqual(sum(resultado[0]), resultado_esperado)

    def test_50(self):
        valores = self.leer_archivo('tests_cases/catedra/50.txt')
        resultado_esperado = self.obtener_resultado_esperado("50.txt") #17750
        resultado = problema_monedas(valores)
        self.assertEqual(sum(resultado[0]), resultado_esperado)

    def test_100(self):
        valores = self.leer_archivo('tests_cases/catedra/100.txt')
        resultado_esperado = self.obtener_resultado_esperado("100.txt") #35009
        resultado = problema_monedas(valores)
        self.assertEqual(sum(resultado[0]), resultado_esperado)

    def test_1000(self):
        valores = self.leer_archivo('tests_cases/catedra/1000.txt')
        resultado_esperado = self.obtener_resultado_esperado("1000.txt") #357814
        resultado = problema_monedas(valores)
        self.assertEqual(sum(resultado[0]), resultado_esperado)

    def test_10000(self):
        valores = self.leer_archivo('tests_cases/catedra/10000.txt')
        resultado_esperado = self.obtener_resultado_esperado("10000.txt") #3550307
        resultado = problema_monedas(valores)
        self.assertEqual(sum(resultado[0]), resultado_esperado)

    def test_20000(self):
        valores = self.leer_archivo('tests_cases/catedra/20000.txt')
        resultado_esperado = self.obtener_resultado_esperado("20000.txt") #7139357
        resultado = problema_monedas(valores)
        self.assertEqual(sum(resultado[0]), resultado_esperado)

if __name__ == '__main__':
    unittest.main()