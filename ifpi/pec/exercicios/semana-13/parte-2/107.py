#Escreva um programa que leia uma lista com 100 números. Ao término da leitura o programa deve fazer a ordenação dos números lidos. Após a ordenação, crie uma lista onde os elementos de índice par são multiplicados por 3 e os elementos de índice ímpar são multiplicados com 5. DICA: Use a função a sorted() ou o método sort() para realizar a ordenação dos valores.


def main():
    lista_numeros = [int(input()) for i in range(100)]

    lista_ordenada = sorted(lista_numeros)
    nova_lista = [valor * 3 if i % 2 == 0 else valor * 5 for i, valor in enumerate(lista_ordenada)]

    print(nova_lista)

if __name__ == "__main__":
    main()
