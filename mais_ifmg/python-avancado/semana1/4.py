def calcula(expr):
    try:
        return eval(expr)
    except:
        print('Expressão inválida!')
    return None


print(calcula("10+10"))