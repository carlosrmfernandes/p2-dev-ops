def somar (a,b):
    return a+b

def subtrair (a,b):
    return a-b

def multiplicar (a,b):    
    return a*b

def dividir (a,b):
    if b==0:
        raise ValueError("Divisão por 0 não existe")
    return a/b
