'''Escreva um programa que leia dois valores inteiros (x e y) e mostre todos os números primos entre x e y.

'''
def numero_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True



def main():
    x = int(input())
    y = int(input())
    for n in range(x, y + 1):
        if numero_primo(n):
            print(f"{n}")


            
if __name__ == "__main__":
    main()