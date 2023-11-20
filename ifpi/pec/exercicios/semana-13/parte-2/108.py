#Escreva um programa que ler a nota de 50 alunos. Mostre uma lista apenas com os índices dos alunos que tem nota maior ou igual a 6 (seis).


def main():
    notas = [float(input()) for i in range(50)]
    indices_notas_altas = [i for i, nota in enumerate(notas) if nota >= 6]
    print(indices_notas_altas)

if __name__ == "__main__":
    main()
