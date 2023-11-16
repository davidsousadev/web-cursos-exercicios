while True:
    nome = str(input("Digite o nome do Herói: ").strip())
    xp = int(input("Qual o nível de experiência do Herói: "))
    if 0 <= xp <= 1000:
        nivel = "Ferro"
        break
    elif 1001 <= xp <= 2000:
        nivel = "Bronze"
        break
    elif 2001 <= xp <= 5000:
        nivel = "Prata"
        break
    elif 6001 <= xp <= 7000:
        nivel = "Ouro"
        break
    elif 7001 <= xp <= 8000:
        nivel = "Platina"
        break
    elif 8001 <= xp <= 9000:
        nivel = "Ascendente"
        break
    elif 9001 <= xp <= 10000:
        nivel = "Imortal"
        break
    elif xp >= 10001:
        nivel = "Radiante"
        break
    else:
        print("Digite um valor valido!")

print(f"O Herói de nome **{nome}** está no nível de **{nivel}**")