# Considere uma tupla que guarde temperaturas em Celsius (C) ou Fahrenheit (F) como um valor em duas partes: temperatura e escala. Por exemplo: 32,5 graus Celsius é representado como (32.5, ‘C’) e 45,2 graus Fahrenheit é representado como (45.2, ‘F’). Crie uma função que recebe duas temperaturas e retorna a mais alta. Caso as temperaturas sejam de escalas diferentes, a função deve fazer a conversão antes de compará-las. Faça a leitura de duas temperaturas, com (temperatura, escala), e mostre qual é a maior. Use upper() e colchetes [] para garantir a leitura correta, por exemplo: escala = input('Escala : ').upper()[0]

def converter_celsius(temperatura, escala):

    if escala == 'F':
        return (temperatura - 32) * 5/9
    else:
        return temperatura

def temperatura_mais_alta(temp1, temp2):

    valor1, escala1 = temp1
    valor2, escala2 = temp2

    valor1 = converter_celsius(valor1, escala1)
    valor2 = converter_celsius(valor2, escala2)

    return temp1 + temp2 

def main():
    tupla = ()
    temp1 = float(input())
    escala1 = str(input().upper()[0])
    temp2 = float(input())
    escala2 = str(input().upper()[0])
    resultado = temperatura_mais_alta((temp1, escala1), (temp2, escala2))
    soma = resultado[0] + resultado[2]
    tupla += (soma,)
    tupla += (resultado[1],)
    print(f"{tupla}")

if __name__ == "__main__":
    main()