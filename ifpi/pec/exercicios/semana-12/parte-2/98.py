'''Calcular H =1 + 1/2 + 1/3 + 1/4 + ... + 1/n, escreva um programa para calcular o valor de H com 4 (quatro) casas decimais. O número n é lido.'''
n = int(input())
h = 0
for i in range(1, n + 1):     
    h += 1 / i
h = round(h, 4)
print(f"{h:.4f}")