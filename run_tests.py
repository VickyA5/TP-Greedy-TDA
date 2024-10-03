import unittest
from algoritmo_greedy import problema_monedas

class TestProblemaMonedas(unittest.TestCase):
    def leer_archivo(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            valores = list(map(int, lines[1].strip().split(';')))
        return valores

    def test_20(self):
        valores = self.leer_archivo('tests_cases/catedra/20.txt')
        resultado_esperado = 7165
        resultado = problema_monedas(valores)
        self.assertEqual(sum(resultado[0]), resultado_esperado)

    def test_25(self):
        valores = self.leer_archivo('tests_cases/catedra/25.txt')
        resultado_esperado = 9635
        resultado = problema_monedas(valores)
        self.assertEqual(sum(resultado[0]), resultado_esperado)

    def test_50(self):
        valores = self.leer_archivo('tests_cases/catedra/50.txt')
        resultado_esperado = 17750
        resultado = problema_monedas(valores)
        self.assertEqual(sum(resultado[0]), resultado_esperado)

    def test_100(self):
        valores = self.leer_archivo('tests_cases/catedra/100.txt')
        resultado_esperado = 35009
        resultado = problema_monedas(valores)
        self.assertEqual(sum(resultado[0]), resultado_esperado)

    def test_1000(self):
        valores = self.leer_archivo('tests_cases/catedra/1000.txt')
        resultado_esperado = 357814
        resultado = problema_monedas(valores)
        self.assertEqual(sum(resultado[0]), resultado_esperado)

    def test_10000(self):
        valores = self.leer_archivo('tests_cases/catedra/10000.txt')
        resultado_esperado = 3550307
        resultado = problema_monedas(valores)
        self.assertEqual(sum(resultado[0]), resultado_esperado)

    def test_20000(self):
        valores = self.leer_archivo('tests_cases/catedra/20000.txt')
        resultado_esperado = 7139357
        resultado = problema_monedas(valores)
        self.assertEqual(sum(resultado[0]), resultado_esperado)

if __name__ == '__main__':
    unittest.main()