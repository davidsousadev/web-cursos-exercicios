def signos(dia, mes):
    if (dia >= 21 and mes == 3) or (dia <= 19 and mes == 4):
        return "Áries"
    if (dia >= 20 and mes == 4) or (dia <= 20 and mes == 5):
        return "Touro"
    if (dia >= 21 and mes == 5) or (dia <= 21 and mes == 6):
        return "Gêmeos"
    if (dia >= 22 and mes == 6) or (dia <= 22 and mes == 7):
        return "Câncer"
    if (dia >= 23 and mes == 7) or (dia <= 22 and mes == 8):
        return "Leão"
    if (dia >= 23 and mes == 8) or (dia <= 22 and mes == 9):
        return "Virgem"
    if (dia >= 23 and mes == 9) or (dia <= 22 and mes == 10):
        return "Libra"
    if (dia >= 23 and mes == 10) or (dia <= 21 and mes == 11):
        return "Escorpião"
    if (dia >= 22 and mes == 11) or (dia <= 21 and mes == 12):
        return "Sagitário"
    if (dia >= 22 and mes == 12) or (dia <= 19 and mes == 1):
        return "Capricórnio"
    if (dia >= 20 and mes == 1) or (dia <= 18 and mes == 2):
        return "Aquário"
    if (dia >= 19 and mes == 2) or (dia <= 20 and mes == 3):
        return "Peixes"
    else:
        return "Data invalida"

def main():
    dia = int(input("Digite o dia em que você nasceu: "))
    mes = int(input("Digite o mês em que voce nasceu: "))
    resultado = signos(dia, mes)
    print(f'Seu signo é {resultado}.')



if __name__ == '__main__':
    main()
