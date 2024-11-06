## Testes das funcoes da calculadora
import unittest
from calculadora0 import somar, subtrair, multiplicar, dividir

class TestCalculadora(unittest.TestCase):

    def test_somar(self):
        # teste positivo
        positivo = somar(100, 150) # 250
        self.assertEqual(positivo, 250)
        # teste negativo
        negativo = somar(33.5, 20) # 55.5
        self.assertNotEqual(negativo, 55)
        # teste de quebra - formato nao esperado, tratamento de erro
        quebra = somar('a', 12) # ValueError
        self.assertEqual(quebra, ValueError)
        # teste zero
        zero = somar(0, 0) # 0
        self.assertEqual(zero, 0)

    def test_subtrair(self):
        # teste positivo
        positivo = subtrair(530, 30) # 500
        self.assertEqual(positivo, 500)
        # teste negativo
        negativo = subtrair(-992, 12) # -994
        self.assertNotEqual(negativo, 994)
        # teste quebra
        quebra = subtrair(25.5, list)
        self.assertEqual(quebra, ValueError) # ValueError
        # teste zero
        zero = subtrair(0, 0) # 0
        self.assertEqual(zero, 0)

    def test_multiplicar(self):
        # teste positivo
        positivo = multiplicar(12, 10) # 120
        self.assertEqual(positivo, 120)
        # teste negativo
        negativo = multiplicar(2, -4) # -8
        self.assertNotEqual(negativo, 8)
        # teste quebra
        quebra = multiplicar(object, str) # ValueError
        self.assertEqual(quebra, ValueError)
        # teste zero
        zero = multiplicar(0, 0) # 0
        self.assertEqual(zero, 0)

    def test_dividir(self):
        # teste positivo
        positivo = dividir(-5, 2) # -2.5
        self.assertEqual(positivo, -2.5)
        # teste negativo
        negativo = dividir(100, -25) # -4
        self.assertNotEqual(negativo, 4)
        # teste quebra
        quebra = dividir(12.5, '4') # ValueError
        self.assertEqual(quebra, ValueError)
        # teste zero
        zero = dividir(0, 0) # ZeroDivisionError
        self.assertEqual(zero, ZeroDivisionError)


if __name__ == '__main__':
    unittest.main()