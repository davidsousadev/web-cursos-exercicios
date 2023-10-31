'''Você tem uma poupança de 10 mil reais, que rende 0,7% ao mês. Você deseja comprar um carro, mas o preço do carro sobe a taxa de 0,4% ao mês. Escreva um programa que leia o preço de um carro hoje e calcule em quantos meses, com o dinheiro dessa aplicação, você terá dinheiro suficiente para comprar o carro à vista.'''

l = 10000
c = 0
x = int(input())
while x > l:
    l = l + (l/100) * 0.7 
    x = x + (x/100) * 0.4
    c += 1 
print(c)