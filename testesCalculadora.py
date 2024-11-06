import unittest  
from calculadora import somar, dividir, subtrair, multuplicar

class TestMeuCodigo(unittest.TestCase):
    def test_soma(self):
        positivo = somar(1,2)
        self.assertEqual(positivo, 3)

    def test_subtrrair(self):
        positivo = subtrair(2,2)
        self.assertEqual(positivo, 0)

    def test_dividir(self):
        positivo = dividir(4,2)
        self.assertEqual(positivo,2)
    
    def teste_multiplicar(self):
        positivo = multuplicar(3,3)
        self.assertAlmostEqual(positivo, 9)

if __name__ == '__main__':
    unittest.main()




