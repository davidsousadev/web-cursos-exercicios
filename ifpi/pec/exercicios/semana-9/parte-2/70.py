# Inicializa o contador de respostas "Sim"
contador_sim = 0

# Faz as perguntas e registra as respostas
resposta_a = input().strip().upper()
resposta_b = input().strip().upper()
resposta_c = input().strip().upper()
resposta_d = input().strip().upper()
resposta_e = input().strip().upper()

# Verifica as respostas e incrementa o contador de "Sim"
if resposta_a == "S":
    contador_sim += 1
if resposta_b == "S":
    contador_sim += 1
if resposta_c == "S":
    contador_sim += 1
if resposta_d == "S":
    contador_sim += 1
if resposta_e == "S":
    contador_sim += 1

# Classificação com base no número de respostas "Sim"
if contador_sim == 2:
    classificacao = "Suspeito"
elif contador_sim == 3 or contador_sim == 4:
    classificacao = "Cúmplice"
elif contador_sim == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"

# Exibe a classificação
print(f"{classificacao}")
