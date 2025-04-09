from datetime import date


class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)


class Transacao:
    def registrar(self, conta):
        raise NotImplementedError("O método registrar deve ser implementado.")


class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if self.valor > 0:
            conta._saldo += self.valor
            conta._historico.adicionar_transacao(self)
            print("=== Depósito realizado com sucesso! ===")
        else:
            print("@@@ Operação falhou! Valor inválido. @@@")


class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if self.valor > conta._saldo:
            print("@@@ Operação falhou! Saldo insuficiente. @@@")
        elif self.valor > conta._limite:
            print("@@@ Operação falhou! Valor excede o limite. @@@")
        elif conta._numero_saques >= conta._limite_saques:
            print("@@@ Operação falhou! Limite de saques excedido. @@@")
        elif self.valor > 0:
            conta._saldo -= self.valor
            conta._numero_saques += 1
            conta._historico.adicionar_transacao(self)
            print("=== Saque realizado com sucesso! ===")
        else:
            print("@@@ Operação falhou! Valor inválido. @@@")


class Conta:
    def __init__(self, cliente, numero, agencia="0001"):
        self._saldo = 0.0
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = Historico()

    def saldo(self):
        return self._saldo

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)

    def sacar(self, valor):
        saque = Saque(valor)
        saque.registrar(self)

    def depositar(self, valor):
        deposito = Deposito(valor)
        deposito.registrar(self)


class ContaCorrente(Conta):
    def __init__(self, cliente, numero, limite=500, limite_saques=3):
        super().__init__(cliente, numero)
        self._limite = limite
        self._limite_saques = limite_saques
        self._numero_saques = 0


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento


# Funções auxiliares
def criar_usuario():
    cpf = input("Informe o CPF (somente número): ")
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço: ")
    return PessoaFisica(nome, cpf, data_nascimento, endereco)


def criar_conta(numero, cliente):
    conta = ContaCorrente(cliente, numero)
    cliente.adicionar_conta(conta)
    return conta


def exibir_extrato(conta):
    print("\n================ EXTRATO ================")
    for transacao in conta._historico.transacoes:
        tipo = transacao.__class__.__name__
        print(f"{tipo}:\tR$ {transacao.valor:.2f}")
    print(f"\nSaldo:\t\tR$ {conta.saldo():.2f}")
    print("==========================================")


# Programa principal
def main():
    usuarios = []
    contas = []

    while True:
        opcao = input("""
================ MENU ================
[nu]\tNovo usuário
[nc]\tNova conta
[d]\tDepositar
[s]\tSacar
[e]\tExtrato
[q]\tSair
=> """)

        if opcao == "nu":
            usuario = criar_usuario()
            usuarios.append(usuario)
            print("=== Usuário criado com sucesso! ===")

        elif opcao == "nc":
            cpf = input("Informe o CPF do usuário: ")
            usuario = next((u for u in usuarios if u.cpf == cpf), None)

            if usuario:
                numero = len(contas) + 1
                conta = criar_conta(numero, usuario)
                contas.append(conta)
                print("=== Conta criada com sucesso! ===")
            else:
                print("@@@ Usuário não encontrado. @@@")


        elif opcao == "d":
            cpf = input("Informe o CPF do titular: ")
            usuario = next((u for u in usuarios if u.cpf == cpf), None)
            if usuario and usuario.contas:
                valor = float(input("Informe o valor do depósito: "))
                usuario.realizar_transacao(usuario.contas[0], Deposito(valor))
            else:
                print("@@@ Usuário ou conta não encontrados. @@@")


        elif opcao == "s":
            cpf = input("Informe o CPF do titular: ")
            usuario = next((u for u in usuarios if u.cpf == cpf), None)
            if usuario and usuario.contas:
                valor = float(input("Informe o valor do saque: "))
                usuario.realizar_transacao(usuario.contas[0], Saque(valor))
            else:
                print("@@@ Usuário ou conta não encontrados. @@@")


        elif opcao == "e":
            cpf = input("Informe o CPF do titular: ")
            usuario = next((u for u in usuarios if u.cpf == cpf), None)
            if usuario and usuario.contas:
                exibir_extrato(usuario.contas[0])
            else:
                print("@@@ Usuário ou conta não encontrados. @@@")


        elif opcao == "q":
            break

        else:
            print("@@@ Opção inválida! @@@")


if __name__ == "__main__":
    main()
