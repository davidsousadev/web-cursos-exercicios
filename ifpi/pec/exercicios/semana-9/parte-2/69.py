# Preços das frutas
preco_morango_ate_5kg = 2.50
preco_morango_acima_5kg = 2.20
preco_maca_ate_5kg = 1.80
preco_maca_acima_5kg = 1.50

# Leitura da quantidade de morangos e maçãs
quantidade_morango = float(input())
quantidade_maca = float(input())

# Cálculo do valor a ser pago sem desconto
valor_morango = 0
valor_maca = 0

if quantidade_morango <= 5:
    valor_morango = quantidade_morango * preco_morango_ate_5kg
else:
    valor_morango = quantidade_morango * preco_morango_acima_5kg

if quantidade_maca <= 5:
    valor_maca = quantidade_maca * preco_maca_ate_5kg
else:
    valor_maca = quantidade_maca * preco_maca_acima_5kg

valor_total_sem_desconto = valor_morango + valor_maca

# Verificação do desconto
if quantidade_morango + quantidade_maca > 8 or valor_total_sem_desconto > 25:
    desconto = 0.10 * valor_total_sem_desconto
else:
    desconto = 0

# Cálculo do valor final a ser pago
valor_final = valor_total_sem_desconto - desconto

# Exibição do valor a ser pago pelo cliente
print(f"{valor_final:.2f}")
