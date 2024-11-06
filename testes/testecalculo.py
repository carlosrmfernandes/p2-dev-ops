import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
   
from src.calculadora import somar,subtrair,multiplicar,dividir

class TesteCalculo(unittest.TestCase):

    def test_somar(self):
        self.assertEqual(somar(2, 3), 5)
        self.assertEqual(somar(-1, 1), 0)

    def test_subtrair(self):
        self.assertEqual(subtrair(5, 3), 2)
        self.assertEqual(subtrair(0, 0), 0)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 3), 9)
        self.assertEqual(multiplicar(-1, 2), -2)

    def test_dividir(self):
        self.assertEqual(dividir(6, 3), 2)
        with self.assertRaises(ValueError):
            dividir(10, 0)

if __name__ == '__main__':
    unittest.main()


