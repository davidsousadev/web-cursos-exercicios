# Desafio: A Aventura do Explorador

# Entrada
quantidade_passos = int(input())

# TODO: Adicione uma condição para verificar se a quantidade de passos é positiva.
# Se a quantidade de passos for zero, imprima "Nenhum passo dado na floresta."
# Caso contrário, utilize um loop for para imprimir a mensagem do explorador, indicando o número do passo.

for i in range(quantidade_passos+1):
  if i==1:
    print(f"Explorador: {i} passo")
  elif i>1:
    print(f"Explorador: {i} passos")
  elif quantidade_passos==0:
    print("Nenhum passo dado na floresta.")