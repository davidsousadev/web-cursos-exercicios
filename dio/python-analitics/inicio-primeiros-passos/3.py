capacidade_atual, aumento_percentual = map(int, input().split())

# TODO: Calcule a nova capacidade do disco de Mithril

# TODO: Imprima a nova capacidade

resultado = capacidade_atual + (capacidade_atual/100 * aumento_percentual)
print(int(resultado))