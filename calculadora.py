
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
