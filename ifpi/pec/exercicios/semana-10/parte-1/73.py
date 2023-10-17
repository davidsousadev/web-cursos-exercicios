'''
Escreva um programa que leia um conjunto 100 números inteiros e exiba o valor médio dos mesmos (com duas casas decimais).
'''
def media():
    media = 0
    for i in range(1,101):
        x = int(input())
        media += x
def main():
    print(media/100)


if __name__ == '__main__':
    main()