# Escreva um programa que leia uma quantidade indeterminada de números inteiros, terminada pela leitura de um número 0 (zero). Depois, leia um valor inteiro constante. O programa deve mostrar uma nova lista onde cada valor da lista original é a multiplicado pelo valor da constante.

# IMPORTANTE: Crie uma função chamada multiplica_constante() que receba a lista original e o valor da constante e retorna uma nova lista com os elementos multiplicados.



def multiplica_constante(lista, constante):
    return [elemento * constante for elemento in lista]



def main():
    numeros = []
    while True:
        numero = int(input())
        if numero == 0:
            break
        numeros.append(numero)

    constante = int(input())
    nova_lista = multiplica_constante(numeros, constante)
    print(nova_lista)
    
    
    
if __name__ == "__main__":
    main()
