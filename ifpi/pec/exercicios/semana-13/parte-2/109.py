# Escreva um programa que leia uma quantidade indeterminada de números reais, terminada pela leitura de um número 0 (zero). O programa deve mostrar uma nova lista onde cada elemento é a soma dos elementos anteriores da lista original. IMPORTANTE: Crie uma função chamada soma_cumulativa() que receba a lista original e retorna uma lista com a soma cumulativa. Por exemplo:

# minha_lista = [1, 2, 3, 4, 5]

# somacumulativa(minhalista)

# [1, 3, 6, 10, 15]



def soma_cumulativa(lista_original):
    soma = 0
    lista_soma_cumulativa = []

    for elemento in lista_original:
        soma += elemento
        lista_soma_cumulativa.append(soma)

    return lista_soma_cumulativa

def main():
    numeros = []
    while True:
        numero = int(input())
        if numero == 0:
            break
        numeros.append(numero)
    lista_soma_cumulativa = soma_cumulativa(numeros)
    print(lista_soma_cumulativa)

if __name__ == "__main__":
    main()
