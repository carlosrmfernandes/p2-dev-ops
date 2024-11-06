import unittest
from calculadora import soma_2302994_2303258,subtrair_2302994_2303258,multiplicar_2302994_2303258,dividir_2302994_2303258

class TestCalculadora(unittest.TestCase):
    def test_soma_2302994_2303258(self):
        self.assertEqual(soma_2302994_2303258(25,25), 50)
        self.assertNotEqual(soma_2302994_2303258(10,10), 30)

    def test_subtrair_2302994_2303258(self):
        self.assertEqual(subtrair_2302994_2303258(60,30), 30)
        self.assertNotEqual(subtrair_2302994_2303258(50,25), 15)

    def test_multiplicar_2302994_2303258(self):
        self.assertEqual(multiplicar_2302994_2303258(7,7), 49)
        self.assertNotEqual(multiplicar_2302994_2303258(4,10), 100)

    def test_dividir_2302994_2303258(self):
        self.assertEqual(dividir_2302994_2303258(25,5), 5)
        self.assertNotEqual(dividir_2302994_2303258(8,4), 10)              