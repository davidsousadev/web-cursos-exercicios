'''
Escreva um programa que gere a seguinte sequência: 10, 20, 30, 40, ..., 990, 1000. Considere a separação dos números por vírgula seguido de espaço em brando e o pontos no final da sequência.
'''
media = ""
for i in range(1,991):
    if(i%10==0):
        media = f"{media}"+f"{i}"+f", "
media = f"{media}"+f"1000"+f"."
print(media)



if __name__ == '__main__':
    main()