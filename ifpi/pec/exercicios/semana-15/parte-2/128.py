# Fazer um programa para ler uma matriz n x m de números inteiros. Os valores de n e m são inteiros, positivos e devem ser informados pelo usuário, calcular e armazenar em uma tupla para mostrar, respectivamente: a) a soma dos elementos da primeira linha b) a soma dos elementos da última coluna c) a média de todos os elementos d) o menor elemento e) o maior elemento


def ler_matriz(n, m):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(m):
            elemento = int(input())
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def calcular_estatisticas(matriz):
    primeira_linha = sum(matriz[0])
    ultima_coluna = sum(matriz[i][-1] for i in range(len(matriz)))
    
    todos_elementos = [elemento for linha in matriz for elemento in linha]
    media = round((sum(todos_elementos) / len(todos_elementos)), 4)
    menor = min(todos_elementos)
    maior = max(todos_elementos)
    
    return primeira_linha, ultima_coluna, media, menor, maior

def main():
    n = int(input())
    m = int(input())

    matriz = ler_matriz(n, m)

    estatisticas = calcular_estatisticas(matriz)

    print(f"{estatisticas}")

if __name__ == "__main__":
    main()
