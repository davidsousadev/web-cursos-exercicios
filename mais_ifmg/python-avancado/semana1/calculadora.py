def calcula(expr):
    try:
        return eval(expr)
    except:
        print('Expressão inválida!')
    return None

def somar(a,b):
    return calcula(f"{a}+{b}")

def subitrair(a,b):
    return calcula(f"{a}-{b}")