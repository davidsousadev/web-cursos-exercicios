'''
05. Escreva um programa que leia o número de matrícula de um aluno, suas notas em 3 provas e a média das notas
obtidas nos exercícios que fazem parte da sua avaliação. Calcule a média final usando a fórmula:

Média Final =

Nota 1 + Nota 2 ∗ 2 + Nota 3 ∗ 3 + Média Exercícios

7

A atribuição dos conceitos obedece a tabela abaixo.

Conceito Média Final
A >= 9.0
B >= 7.5 e < 9.0
C >= 6.0 e < 7.5
D >= 4.0 e < 6.0
E < 4.0

O programa deve escrever a matrícula do aluno, a média final, o conceito correspondente e a mensagem “Aprovado”
se o conceito for A, B ou C ou “Reprovado” se o conceito for D ou E.
'''



def calcular_media_final(n1, n2, n3, media):
    media_final = (nota1 + nota2 * 2 + nota3 * 3 + media_exercicios) / 7
    return media_final

def determinar_conceito(media_final):
    if media_final >= 9.0:
        return "A"
    elif 7.5 <= media_final < 9.0:
        return "B"
    elif 6.0 <= media_final < 7.5:
        return "C"
    elif 4.0 <= media_final < 6.0:
        return "D"
    else:
        return "E"

matricula = str(input().strip())
n1 = float(input())
n2 = float(input())
nota3 = float(input())
media_exercicios = float(input())

media_final = calcular_media_final(nota1, nota2, nota3, media_exercicios)
conceito = determinar_conceito(media_final)

print(f"{matricula}")
print(f"{media_final:.2f}")
print(f"{conceito}")

if conceito in ["A", "B", "C"]:
    print("Aprovado")
else:
    print("Reprovado")
