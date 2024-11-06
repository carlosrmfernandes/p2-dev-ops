import unittest

from calculadora0 import somar_2302692_2303304
from calculadora0 import subtrair_2302692_2303304
from calculadora0 import multiplicar_2302692_2303304
from calculadora0 import dividir_2302692_2303304  

from calculadora0 import somar_2302692_2303304
from calculadora0 import subtrair_2302692_2303304
from calculadora0 import multiplicar_2302692_2303304
from calculadora0 import dividir_2302692_2303304  

class testSomar(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(somar_2302692_2303304(2,3), 5)
        self.assertEqual(somar_2302692_2303304(-1,1), 0)
        self.assertEqual(somar_2302692_2303304(7,2), 9)
        self.assertEqual(somar_2302692_2303304(0,-1), -1)

class testSubtrair(unittest.TestCase):
    def test_subtracao(self):
        self.assertEqual(subtrair_2302692_2303304(5,3), 2)
        self.assertEqual(subtrair_2302692_2303304(10,-1), 11)
        self.assertEqual(subtrair_2302692_2303304(2,5), -3)
        self.assertEqual(subtrair_2302692_2303304(7,0), 7)

class testMultiplicar(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(multiplicar_2302692_2303304(2,3), 6)
        self.assertEqual(multiplicar_2302692_2303304(2,1), 2)
        self.assertEqual(multiplicar_2302692_2303304(9,2), 18)
        self.assertEqual(multiplicar_2302692_2303304(178,0), 0)

class testDividir(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(dividir_2302692_2303304(6,3), 2)
        self.assertEqual(dividir_2302692_2303304(8,2), 4)
        self.assertEqual(dividir_2302692_2303304(12,4), 3)
        self.assertEqual(dividir_2302692_2303304(10,2), 5)

if __name__ == '__main__':
    unittest.main()