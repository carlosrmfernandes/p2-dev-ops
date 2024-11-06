# Função de soma
def soma(a, b):
    return a + b

# Função de subtração
def subtracao(a, b):
    return a - b

# Função de multiplicação
def multiplicacao(a, b):
    return a * b

# Função de divisão
def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

print(soma(5, 3))         # Saída: 8
print(subtracao(5, 3))    # Saída: 2
print(multiplicacao(5, 3)) # Saída: 15
print(divisao(5, 3))      # Saída: 1.666...
print(divisao(5, 0))      # Saída: Erro: divisão por zero!

import unittest
class TestOperacoesMatematicas(unittest.TestCase):
    
    def test_soma(self):
        self.assertEqual(soma(5, 3), 8)
        self.assertEqual(soma(-2, 2), 0)
        self.assertEqual(soma(0, 0), 0)

    def test_subtracao(self):
        self.assertEqual(subtracao(5, 3), 2)
        self.assertEqual(subtracao(-2, 2), -4)
        self.assertEqual(subtracao(0, 0), 0)

    def test_multiplicacao(self):
        self.assertEqual(multiplicacao(5, 3), 15)
        self.assertEqual(multiplicacao(-2, 2), -4)
        self.assertEqual(multiplicacao(0, 5), 0)

    def test_divisao(self):
        self.assertEqual(divisao(6, 3), 2)
        self.assertEqual(divisao(-6, 3), -2)
        self.assertEqual(divisao(0, 5), 0)
        self.assertEqual(divisao(5, 0), "Erro: divisão por zero!")  # Teste de divisão por zero

# Executa os testes
if __name__ == '__main__':
    unittest.main()