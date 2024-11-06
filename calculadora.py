def calcular(a, b, operacao):
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