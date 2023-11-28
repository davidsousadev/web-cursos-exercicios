# Considere uma tupla que guarde temperaturas em Celsius (C) ou Fahrenheit (F) como um valor em duas partes: temperatura e escala. Por exemplo: 32,5 graus Celsius é representado como (32.5, ‘C’) e 45,2 graus Fahrenheit é representado como (45.2, ‘F’). Crie uma função que recebe duas temperaturas e retorna a mais alta. Caso as temperaturas sejam de escalas diferentes, a função deve fazer a conversão antes de compará-las. Faça a leitura de duas temperaturas, com (temperatura, escala), e mostre qual é a maior. Use upper() e colchetes [] para garantir a leitura correta, por exemplo: escala = input('Escala : ').upper()[0]

def converterTemperatura(temp, escala):
    if escala == 'C':
        return (temp * 9/5) + 32, 'F'
    elif escala == 'F':
        return (temp - 32) * 5/9, 'C'

def temperaturaMaior(temp1, temp2):
    temp1, escala1 = temp1
    temp2, escala2 = temp2
    
    if escala1 != escala2:
        temp1, escala1 = converterTemperatura(temp1, escala1)
        temp2, escala2 = converterTemperatura(temp2, escala2)

    if temp1 > temp2:
        return temp1
    else:
        return temp2



def main():
    temp1 = float(input())
    escala1 = input().upper()[0]

    temp2 = float(input())
    escala2 = input().upper()[0]

    maior = temperaturaMaior((temp1, escala1), (temp2, escala2))
    print(maior)

if __name__=='__main__':
    main()