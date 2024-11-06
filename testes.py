import unittest 
from calculadora import calcular

class TestCalculadora(unittest.TestCase):

    def test_soma(self):
        resultado = calcular(3, 2, '1')
        self.assertEqual(resultado, 5)
    
    def test_subtracao(self):
        resultado = calcular(5, 3, '2')
        self.assertEqual(resultado, 2)
    
    def test_multiplicacao(self):
        resultado = calcular(4, 2, '3')
        self.assertEqual(resultado, 8)
    
    def test_divisao(self):
        resultado = calcular(6, 2, '4')
        self.assertEqual(resultado, 3)
    
    def test_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            calcular(6, 0, '4')
    
    def test_operacao_invalida(self):
        with self.assertRaises(ValueError):
            calcular(6, 2, '5')

if __name__ == '__main__':
    unittest.main()