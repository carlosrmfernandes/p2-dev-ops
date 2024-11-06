import unittest 
from calculadora import somar_2302437_2301076_retificacao, subtrair_2302437_2301076_retificacao, multiplicar_2302437_2301076_retificacao, dividir_2302437_2301076_retificacao

class TestCalculadora(unittest.TestCase):

    def test_somar(self):
        self.assertEqual(somar_2302437_2301076_retificacao(3, 2), 5)
        self.assertEqual(somar_2302437_2301076_retificacao(5, 5), 10)
        self.assertEqual(somar_2302437_2301076_retificacao(1, 1), 2)

    def test_subtrair(self):
        self.assertEqual(subtrair_2302437_2301076_retificacao(3, 2), 1)
        self.assertEqual(subtrair_2302437_2301076_retificacao(6, 3), 3)
        self.assertEqual(subtrair_2302437_2301076_retificacao(0, -5), 5)

    def test_multiplicar(self):
        self.assertEqual(multiplicar_2302437_2301076_retificacao(3, 2), 6)
        self.assertEqual(multiplicar_2302437_2301076_retificacao(6, 3), 18)
        self.assertEqual(multiplicar_2302437_2301076_retificacao(-5, 100), -500)

    def test_dividir(self):
        self.assertEqual(dividir_2302437_2301076_retificacao(6, 2), 3)
        self.assertEqual(dividir_2302437_2301076_retificacao(25, 5), 5)
        self.assertEqual(dividir_2302437_2301076_retificacao(1000, 10), 100)

if __name__ == '__main__':
    unittest.main()