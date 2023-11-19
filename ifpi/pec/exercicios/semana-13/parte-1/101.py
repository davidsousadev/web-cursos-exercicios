'''
Leia uma lista de 10 (dez) números inteiros, mostre os números, sua soma e a multiplicação.'''
lista = [0,0,0,0,0,0,0,0,0,0]
soma = 0
multiplicacao = 1
for x in range(10):
    n = int(input())
    lista[x] = n
    #lista.append(n)
    soma += n
    multiplicacao *= n
print(lista, soma, multiplicacao, sep='\n')