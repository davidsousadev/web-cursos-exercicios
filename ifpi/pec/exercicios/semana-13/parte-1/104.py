# Leia 20 números inteiros e armazene-os numa lista. Armazene os números pares na lista PAR e os números ímpares na lista IMPAR. Imprima as três listas



def main():
    n = []
    pares = []
    impares = []
    for i in range(20):
        num = int(input())
        n.append(num)
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

    print(n)
    print(pares)
    print(impares)



if __name__ == "__main__":
    main()