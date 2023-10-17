'''
Escreva um programa que leia um conjunto de 100 números inteiros positivos e determine o maior deles.
'''
maior = 0
for i in range(1,101):
    x = int(input())
    if(x>=maior):
        maior = x
print(maior)



if __name__ == '__main__':
    main()