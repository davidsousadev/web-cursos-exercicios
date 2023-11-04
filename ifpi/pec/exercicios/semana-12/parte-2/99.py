'''Um número é, por definição, primo se ele não tem divisores, exceto 1 e ele próprio. Escreva um programa que leia um número e determine se ele é ou não primo.

'''
n = int(input())
primo = True
if n <= 1:
    primo = False
else:
    i = 2
    while i <= n**0.5:
        if n % i == 0:
            primo = False
            break
        i += 1
if primo:
    print(True)
else:
    print(False)