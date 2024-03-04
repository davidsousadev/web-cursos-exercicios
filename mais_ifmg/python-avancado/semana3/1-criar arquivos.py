caminho = "mais_ifmg/python-avancado/semana3/arquivos/"
# nome = str(input("Digite o nome do arquivo: ").strip())
print(f"Nome do arquivo: contatos.csv")
arquivo  = open(f"{caminho}contatos.csv", 'a')# Adiciona ao arquivo ja existente ou cria um arquivo
while True:
    nome = str(input("Nome: ").strip())
    numero = str(input("Fone: ").strip())
    if nome=='' or numero=='':
        break
    arquivo.write("Nome: " + nome + "\n" + "Fone: " + numero + "\n")
arquivo.close