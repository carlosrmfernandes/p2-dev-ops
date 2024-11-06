import unittest
from calculadora import somar, subtrair, multiplicar, dividir

class TesteCalculadora(unittest.TestCase):

    def teste_somar(self):
        self.assertEqual(somar(2,3),5)
        self.assertEqual(somar(1,6),7)

    def teste_subtrair(self):
        self.assertEqual(subtrair(10,5),5)
        self.assertEqual(subtrair(8,1),7)

    def teste_multiplicar(self):
        self.assertEqual(multiplicar(3,3),9)
        self.assertEqual(multiplicar(10,4),40)

    def teste_dividir(self):
        self.assertEqual(dividir(4,4),1)
        self.assertEqual(dividir(60,6),10)

