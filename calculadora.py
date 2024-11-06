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