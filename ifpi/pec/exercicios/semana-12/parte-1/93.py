'''Dado um país A, com taxa de natalidade de 2% ao ano, e um país B com uma taxa de natalidade de 3% ano. Sabe-se que, atualmente, o país A tem população maior que o país B. Faça um programa que leia a população de cada país e imprima o tempo necessário para que a população do país B ultrapasse a população do país A.'''

l = int(input())
c = 0
x = int(input())
while x > l:
    if(l > 0 and x > 0):
        l = l + (l/100) * 3 
        x = x + (x/100) * 2
        c += 1 
    else:
        break    
print(c)