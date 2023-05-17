codigo = 10
salario = 1500.00
nome = 'David'
situação = False

tipo = type(salario)

print(salario)
print(tipo)

print("Codigo:", codigo, "Nome:", nome, "O salario atual e de", salario)
print("Codigo: "+ str (codigo) + " Nome: " + nome + " O salario atual e de " + str (salario))

codigo = int(input("Digite o codigo do funcionario: "))
nome = input("Digite o nome do funcionario: ")
salario = float(input("Informe o Salario: "))
ativo = True

print("Codigo: %d \n"% codigo)
print("Nome: %s \t"% nome)
print("Salario: %.2f \v"% salario)
print("Ativo: %r \r" % ativo)
