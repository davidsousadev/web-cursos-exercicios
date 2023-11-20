# Leia duas listas A e B contendo 25 elementos inteiros cada, gerar e imprimir uma lista C de 50 elementos, cujos elementos sejam a intercalação dos elementos de A e B.

def main():
    lista_a = [int(input()) for i in range(25)]
    lista_b = [int(input()) for i in range(25)]
    lista_c = [elemento for elementos in zip(lista_a, lista_b) for elemento in elementos]

    print(lista_a)
    print(lista_b)
    print(lista_c)

if __name__ == "__main__":
    main()
