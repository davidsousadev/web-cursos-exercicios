'''O dodô é uma ave não voadora, extinta atualmente, e que era endêmica da Ilha Maurítius, na costa leste da África. A partir do ano 1600, durante cada ano, 6% dos animais dos animais vivos no começo do ano morreram e o número de animais nascidos ao longo do ano que sobreviveram foi de 1% da população inicial.

Escreva um programa que leia a população de aves no início do ano 1600 e imprime, anualmente, a partir do fim de 1600, o número de nascimentos, mortes e o total da população por ano (apenas a parte inteira do números, separados por vírgula). O programa encerra sua execução quanto a população total cai para menos de 10% da população original.'''

def populacao(pi):
    pa = pi
    ano = 1600
    pi *= 0.1
    while pa >= pi:
        n = pa / 100
        mortes = pa / 100 * 6
        pa = pa + n - mortes
        print(f"{ano},{round(n)},{round(mortes)},{round(pa)}")
        ano += 1

populacao(int(input()))