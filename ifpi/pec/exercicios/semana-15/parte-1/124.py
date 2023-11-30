# Leia uma população e informe as cidades com população maior que o valor lido. Veja o exemplo: Veja o exemplo para a leitura de 50000 para a população: CIDADES COM MAIS DE 50000 HABITANTES: IBGE: 120040 - Rio Branco(AC) - POPULAÇÃO: 290639 IBGE: 270030 - Arapiraca(AL) - POPULAÇÃO: 202398 IBGE: 270040 - Atalaia(AL) - POPULAÇÃO: 50323 ...

def carrega_cidades(mesA, valor):
    resultado = []
    aniversariantes = []
    print(f"CIDADES COM MAIS DE {valor} HABITANTES E ANIVERSÁRIO EM {meses(mesA)}:")
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            if int(pop)>=valor and int(mes)==mesA:
                print(f"{nome}({uf}) tem {int(pop)} habitantes e faz aniversário em {dia} de {meses(mesA).lower()}.")
    arquivo.close()
    
    return aniversariantes 

def meses(mes):
    if (mes == 1):
        return "JANEIRO"
    elif (mes == 2):
        return "FEVEREIRO"
    elif (mes == 3):
        return "MARÇO"
    elif (mes == 4):
        return "ABRIL"
    elif (mes == 5):
        return "MAIO"
    elif (mes == 6):
        return "JUNHO"
    elif (mes == 7):
        return "JULHO"
    elif (mes == 8):
        return "AGOSTO"
    elif (mes == 9):
        return "SETEMBRO"
    elif (mes == 10):
        return "OUTUBRO"
    elif (mes == 11):
        return "NOVEMBRO"
    elif (mes == 12):
        return "DEZEMBRO"
    
def main():
    mes = int(input())
    valor = int(input())
    cidades = carrega_cidades(mes, valor)

if __name__=='__main__':
    main()
