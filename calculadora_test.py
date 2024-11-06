# calculadora_test.py
import unittest
from calculadora import (
    somar_2302437_2301076_retificacao_,
    subtrair_2302437_2301076_retificacao_,
    multiplicar_2302437_2301076_retificacao,
    dividir_2302437_2301076_retificacao_,
)

class TestCalculadora(unittest.TestCase):
    def test_somar(self):
        self.assertEqual(somar_2302437_2301076_retificacao_(2, 3), 5)
        self.assertEqual(somar_2302437_2301076_retificacao_(-1, 1), 0)

    def test_subtrair(self):
        self.assertEqual(subtrair_2302437_2301076_retificacao_(10, 5), 5)
        self.assertEqual(subtrair_2302437_2301076_retificacao_(3, 3), 0)

    def test_multiplicar(self):
        self.assertEqual(multiplicar_2302437_2301076_retificacao(2, 5), 10)
        self.assertEqual(multiplicar_2302437_2301076_retificacao(-1, 3), -3)

    def test_dividir(self):
        self.assertEqual(dividir_2302437_2301076_retificacao_(10, 2), 5)
        with self.assertRaises(ValueError):
            dividir_2302437_2301076_retificacao_(10, 0)

if __name__ == '__main__':
    unittest.main()
