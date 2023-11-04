'''Escreva um programa que calcule o fatorial de um número inteiro lido, sabendo-se que: N ! = 1 x 2 x 3 x ... x N-1 x N 0 ! = 1'''

n = int(input())
fatorial = 1
if n!=1:
    while n > 0:
        fatorial *= n
        n -= 1

    print(fatorial)