class Heroi:
    def __init__(self,nome,idade,tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
    def ataque(self):
        if self.tipo =="mago":
            self.tipo = "magia"
        elif self.tipo =="guerreiro":
            self.tipo = "espada"
        elif self.tipo =="monge":
            self.tipo = "artes marciais"
        elif self.tipo =="ninja":
            self.tipo = "shuriken"
        else:
            self.tipo = "Nada"
        
        return self.tipo  
while True:
    nome = str(input("\nQual o nome do guerreiro? "))
    idade = str(input("Qual a idade do guerreiro? "))
    tipo = str(input("Qual o tipo do guerreiro? ex: guerreiro, mago, monge, ninja: "))
    heroi = Heroi(nome, idade, tipo)
    print(f"o {tipo} atacou usando {heroi.ataque()} \n")
    pergunta = str(input("Deseja continuar a exibir heróis: S - Sim | N - Não"))
    if pergunta == "n" or pergunta == "N":
        break