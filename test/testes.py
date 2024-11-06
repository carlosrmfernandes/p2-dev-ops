import unittest
from calculadora import somar_2303325_2303366, subtrair_2303325_2303366, mutiplicar_2303325_2303366, dividir_2303325_2303366

class TestFuncoesMatematicas(unittest.TestCase):
    
    def test_somar(self):
        self.assertEqual(somar_2303325_2303366(10, 5), 15)
        self.assertEqual(somar_2303325_2303366(-1, 1), 0)
        self.assertEqual(somar_2303325_2303366(-1, -1), -2)

    def test_subtrair(self):
        self.assertEqual(subtrair_2303325_2303366(10, 5), 5)
        self.assertEqual(subtrair_2303325_2303366(-1, 1), -2)
        self.assertEqual(subtrair_2303325_2303366(-1, -1), 0)

    def test_multiplicar(self):
        self.assertEqual(mutiplicar_2303325_2303366(10, 5), 50)
        self.assertEqual(mutiplicar_2303325_2303366(-1, 1), -1)
        self.assertEqual(mutiplicar_2303325_2303366(-1, -1), 1)

    def test_dividir(self):
        self.assertEqual(dividir_2303325_2303366(10, 5), 2)
        self.assertEqual(dividir_2303325_2303366(-1, 1), -1)
        self.assertEqual(dividir_2303325_2303366(-1, -1), 1)
        with self.assertRaises(ZeroDivisionError):
            dividir_2303325_2303366(1, 0)

if __name__ == '__main__':
    unittest.main()
