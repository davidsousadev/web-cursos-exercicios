# Lista de palavras para os números em extenso
quantidade = ["", "uma", "duas", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]

# Função para converter um número em extenso
def numero_por_extenso(numero):
    
    centena = numero // 100
    dezena = (numero % 100) // 10
    unidade = numero % 10

    extenso = ""
    
    if centena > 0:
        extenso += f"{quantidade[centena]} centena{'s' if centena > 1 else ''}"
        extenso += f"{' e ' if dezena==0 and unidade > 0 else ''}"
    if dezena > 0:
        if centena > 0 and unidade > 0:
            extenso += ", "
        elif centena > 0:
            extenso += " e "
        if dezena == 1:
            extenso += f"{quantidade[dezena]} dezena{' e ' if unidade > 0 else ''}"
        else:
            extenso += f"{quantidade[dezena]} dezenas{' e ' if unidade > 0 else ''}"
    if unidade == 1:
        extenso += f"{quantidade[unidade]} unidade"
    elif unidade > 0:
        extenso += f"{quantidade[unidade]} unidades"
    
    return extenso

# Entrada do usuário
numero = int(input())
if 1 <= numero <= 999:
# Chama a função e exibe o resultado
    extenso = numero_por_extenso(numero)
    print(f"{extenso}.")
