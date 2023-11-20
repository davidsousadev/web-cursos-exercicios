print("Calculadora co amor")
print("<3 <3 <3 <3 <3 <3 <3")
nomes = input("Digite o nome de 2 pessoas: ").lower()
nomes = nomes.replace(" ", "")
placar = 0
if nomes in "aeiou":
    placar += 5
if nomes in "amor":
    placar +=10
if placar < 10:
    print("Esqueça esta pessoa! Nunca vai da certo!")
if placar>=10:
    print(f"Sem placar de compatibilidade : {placar}")
    print("Vocês terão um relacionamento muito intenso! <3")