'''
Utilizando a linguagem python, implemente a classe e o objeto que você pensou na aula passada.
Dica: 
1.A classe tem que ter pelo menos um atributo mutável.
2. Os métodos devem ter relação com algum atributo mutável.
'''
class computador:
    modelo=None
    marca=None
    cpu=None
    memoria_atual=0
    memori_ram_max=None
    capacidade_hd=0
    capacidade_hd_max=None
    arquivos = {}
    quantidade_arquivos = 0      
    estado='desligado'
    
    def ligar(self):
        self.estado = 'ligado'
    def desligar(self):
        self.estado = 'deligado'
    
    def criar_arquivo(self, nome_arquivo, tamanho):
        if self.estado == 'ligado':
            if self.capacidade_hd_max-tamanho > 0:
                self.capacidade_hd_max-=tamanho
                self.quantidade_arquivos +=1
                self.arquivos[self.quantidade_arquivos] = (nome_arquivo,tamanho)
                print(f"Arquivo de {tamanho} GB adicionado no HD.")
            else:
                print("Memoria Cheia!")
        else:
            print("Computador Desligado!")


        
    def listar_arquivos(self):
        if self.estado == 'ligado':
            for x in range(len(self.arquivos)):
                if self.arquivos[x+1]:
                    print(f"Nome: {self.arquivos[x+1][0]} | {self.arquivos[x+1][1]}")
            return f"{len(self.arquivos)} arquivos"

        

    def deletar_arquivo(self):
        if self.estado == 'ligado':
            nome_arquivo = str(input("Qual o nome do arquivo: ").strip())
            for x in range(len(self.arquivos)):
                if self.arquivos[x+1][0]==nome_arquivo:
                    self.capacidade_hd_max += self.arquivos[x+1][1]
                    if self.arquivos.pop(x+1):
                        return f"Apagado com sucesso!!!"
                else:
                    return f"Arquivo invalido!!!" 

    
         
dell_inspiron = computador()
dell_inspiron.modelo = "Inpirion 3360"
dell_inspiron.marca = "Dell"
dell_inspiron.cpu = "I5"
dell_inspiron.memori_ram_max = "8GB"
dell_inspiron.capacidade_hd_max = 1000

while True:
    opcao = int(input("""
=============== MENU INICIAR ===============
Escolha uma opção:
1 - Liga o computador
2 - Desliga o computador
3 - Adicionar arquivo
4 - Status da capacidade do HD
5 - Listar arquivos
6 - Deletar arquivo
0 - Sair
"""))
    
    if opcao==1:
       dell_inspiron.ligar()
       print(f"Computador {dell_inspiron.estado}.\n")
    elif opcao==2:  
        dell_inspiron.estado = 'desligado'
        print(f"Computador {dell_inspiron.estado}.\n")
    elif opcao==3:
        if dell_inspiron.estado == 'ligado':
            nome = str(input("Digite nome do arquivo: ").strip())
            tamanho = int(input("Digite o Tamanho do arquivo em GB: "))
            dell_inspiron.criar_arquivo(nome, tamanho)
        else:
            print("Computador Desligado!")       
    elif opcao==4:
        print(f"Capacidade disponivel do HD está em {dell_inspiron.capacidade_hd_max} GB")

    elif opcao==5:
        print(dell_inspiron.listar_arquivos())
        
    elif opcao==6:
        
        print(dell_inspiron.deletar_arquivo())    
    elif opcao==0:
        break
    else:
        print("Opcao invalida!")