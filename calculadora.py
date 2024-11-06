
feature/checkout_2302692_2303304
def somar_2302692_2303304(a,b):
    return a+b
def subtrair_2302692_2303304(a,b):
    return a-b
def dividir_2302692_2303304(a,b):
    return a/b
def multiplicar_2302692_2303304(a,b):
    return a*b

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


def somar(numero1,numero2):
    return numero1+numero2

def subtrair(numero1, numero2):
    return numero1 - numero2

def dividir(numero1, numero2):
    return numero1/numero2


def multuplicar(numero1,numero2):
    return numero1*numero2



def soma_2303142_2302304(n1,n2):
    return n1+n2

def subtrair_2303142_2302304(n1,n2):
    return n1-n2
    
def multiplicar_2303142_2302304(n1,n2):
    return n1*n2
    
def dividir_2303142_2302304(n1,n2):
    return n1/n2

def calcular_2302273_2302995(a, b, operacao):
    if operacao == '1': 
        return a + b
    elif operacao == '2':  
        return a - b
    elif operacao == '3':  
        return a * b
    elif operacao == '4':  
        if b == 0:
            raise ValueError("Não é possível dividir por zero")
        return a / b
    else:
        raise ValueError("Operação inválida")


def soma_2302994_2303258(som1,som2):
    return som1 + som2

def subtrair_2302994_2303258(sub1,sub2):
    return sub1 - sub2

def multiplicar_2302994_2303258(mul1,mul2):
    return mul1 * mul2

def dividir_2302994_2303258(div1,div2):
    return div1 / div2


soma_2302994_2303258(5,7)
subtrair_2302994_2303258(10,5)
multiplicar_2302994_2303258(5,9)
dividir_2302994_2303258(10,2)

## Calculadora com funcoes somar, subtrair, multiplicar, dividir
# usar RA dos participantes nos testes ex: somar(ra1, ra2)

def somar(ra1, ra2):
    try:
        return ra1 + ra2
    except:
        return ValueError
    

def subtrair(ra1, ra2):
    try:
        return ra1 - ra2
    except:
        return ValueError


def multiplicar(ra1, ra2):
    try:
        return ra1 * ra2
    except:
        return ValueError


def dividir(ra1, ra2):
    if ra1 == 0 or ra2 == 0:
        return ZeroDivisionError
    else:
        try:
            return ra1 / ra2
        except:
            return ValueError


if __name__ == '__main__':
    ra1 = 2302754
    ra2 = 2302177
    
    somar(ra1, ra2)
    subtrair(ra1, ra2)
    multiplicar(ra1, ra2)
    dividir(ra1, ra2)

