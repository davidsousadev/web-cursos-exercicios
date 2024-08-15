class Main:
    pass
print("ola mundo!")

from Clientes import Clientes

from Conta import Conta

c1 = Clientes("David", "88828-8828")
conta = Conta(c1.nome, 40400.00, 1)
print(conta.titular, " Numero ", conta.numero, "Seu Saldo: ", conta.saldo)