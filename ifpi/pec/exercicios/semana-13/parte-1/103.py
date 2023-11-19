# Escreva um programa que leia um número n. Considere uma lista com n posições, e então: a) preencha com valores reais lidos pelo teclado e imprima na ordem inversa. Considere até 4 (quatro) casas decimais. b) preencha com n notas lidas pelo teclado e imprima as notas e a média na tela. Considere 1 (uma) casa decimal. c) preencha com n letras lidas pelo teclado e imprima quantas vogais foram lidas. Imprima as consoantes.
def prencherListaInputReverso(n, r):
    while True:
        for x in range(n):
            c = round(float(input()), 4)
            r.insert(0, c)
        if (n > 0):
            return r
            break


def prencherListaInput(n, i):
    media = 0
    if (n == 0):
        print(f"SEM NOTAS")
    else:
        while True:
            for x in range(n):
                c = round(float(input()), 1)
                media += c
                i.append(c)
            media = media/n    
            if (n > 0):
                return i, media
                break


def prencherListaInputCaractere(n, ca):
    vogais = "aeiouAEIOU"
    contVogais = 0
    while True:
        for x in range(n):
            c = str(input()[0])
            ca.append(c) 
            if c in vogais: 
                contVogais += 1
                ca.remove(c)
                 
        if (n > 0):
            return ca, contVogais
            break


def main():
    n = int(input())
    c = 0
    r = []
    i = []
    ca = []
    if n==0:
        print(r,i,"SEM NOTAS",c,ca, sep='\n')
    else:
        
        listaReverso = prencherListaInputReverso(n, r)
        print(listaReverso)
        listaInput, media = prencherListaInput(n, i)
        print(listaInput, media, sep='\n')
        listaInputCarartere, contVogais = prencherListaInputCaractere(n, ca)
        print(contVogais)
        print(listaInputCarartere)

if __name__ == '__main__':
    main()