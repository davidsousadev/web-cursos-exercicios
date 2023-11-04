'''A Sequência de Fibonacci é uma sequência de números inteiros, começando por 0 e 1, na qual, cada termo subsequente corresponde à soma dos dois anteriores (0, 1, 1, 2, 3, 5, 8, 13, ...). Escreva um programa que leia um número n, calcule e mostre os n primeiros termos da sequência de Fibonacci. O valor lido para n sempre será maior ou igual a 2.
'''

n = int(input())
fibonacci = 0
print(f"{fibonacci}", end="")
fibonacci = 1
a = 0
b = 1
x = 0
while fibonacci < n:
    x = a + b
    b = a
    a = x 
    
    fibonacci += 1  
    print(f", {x}", end="")
