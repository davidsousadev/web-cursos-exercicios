def ranking(saldo):
    if saldo <= 10:
        nivel = "Ferro"
    elif 11 <= saldo <= 20:
        nivel = "Bronze"
    elif 21 <= saldo <= 50:
        nivel = "Prata"
    elif 51 <= saldo <= 80:
        nivel = "Ouro"
    elif 81 <= saldo <= 90:
        nivel = "Diamante"
    elif 91 <= saldo <= 100:
        nivel = "Lendario"
    elif saldo >= 10001:
        nivel = "Imortal"
    return nivel

def resultado(qtd_vitorias, qtd_derrotas):
    saldo = qtd_vitorias - qtd_derrotas
    return saldo

def main():
    qtd_vitorias = int(input("Digite a quantidade de vitórias: "))
    qtd_derrotas = int(input("Digite a quantidade de derrotas: "))
    saldoVitorias = resultado(qtd_vitorias, qtd_derrotas)
    nivel = ranking(saldoVitorias)
    print(f"O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivel}**")

if __name__ == '__main__':
    main()