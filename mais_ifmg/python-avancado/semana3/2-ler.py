def carrega_cidades(valor):
    resultado = []
    aniversariantes = []
    print(f"CIDADES COM MAIS DE {valor} HABITANTES:")
    with open('mais_ifmg/python-avancado/semana3/arquivos/cidades-pi.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            nome, pop = linha.split(';')
            if int(pop)>=valor:
                print(f"Nome:  {nome} - POPULAÇÃO: {pop}", end="")
    arquivo.close()
    
    return aniversariantes 

    
def main():
    valor = int(input("Digite o valor da quantidade de habitantes: "))
    cidades = carrega_cidades(valor)

if __name__=='__main__':
    main()
