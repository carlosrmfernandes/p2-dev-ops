import unittest #uma biblioteca que vamos utizar para os testes
from calculadora import soma_2303142_2302304, subtrair_2303142_2302304, multiplicar_2303142_2302304, dividir_2303142_2302304 

#TESTE POSITIVO
class TestCalculo(unittest.TestCase):
    def  test_soma(self):
        self.assertEqual(soma_2303142_2302304(20,5),25) #validando o valor da soma se vai ser igual a 5
        self.assertEqual(soma_2303142_2302304(-3,3),0)
        
    def  test_subtrair(self):
        self.assertEqual(subtrair_2303142_2302304(12,6),6)
        self.assertEqual(subtrair_2303142_2302304(-32,30),-62)
        
    def  test_multiplicar(self):
        self.assertEqual(multiplicar_2303142_2302304(5,10),50)
        self.assertEqual(multiplicar_2303142_2302304(10,14),140)
        
    def  test_dividir(self):
        self.assertEqual(dividir_2303142_2302304(64,2),32)
        self.assertEqual(dividir_2303142_2302304(150,5),30)