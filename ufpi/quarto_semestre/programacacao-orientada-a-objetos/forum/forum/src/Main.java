/*
Você deverá desenvolver um programa em Java que faça o seguinte:
Solicite ao usuário que digite seu nome completo.
O programa deverá calcular a soma do valor numérico de cada letra do nome, sendo que cada letra deve ter um valor baseado na sua posição no alfabeto (A = 1, B = 2, C = 3, ..., Z = 26).
Se a soma for par, o programa deverá imprimir uma mensagem personalizada de boas-vindas, incluindo o nome do usuário e uma mensagem motivacional.
Se a soma for ímpar, o programa deverá imprimir uma mensagem personalizada informando que o nome do usuário é “único e especial”, também incluindo o nome do usuário.
Postar aqui o código Java e a saída que o código dá quando você insere seu nome completo.

Exemplo de saída com meu nome:
Meu nome deu o valor 305, que é ímpar, assim a saída foi:
FRANCISCO AIRTON PEREIRA DA SILVA, seu nome é único e especial. Continue sendo você mesmo!
*/

import java.util.Scanner; // Importação da biblioteca Scanner

public class Main {
	public static void main(String[] args) {

		Scanner entrada = new Scanner(System.in); // Scanner para entrada de dados

		// Declaração das variaveis 
		String nomeCompleto, parImpar, mensagem; 
		int soma = 0; 
		int acentoCaractereInvalido = 0;

		System.out.println("Digite seu nome completo (Sem Acentos!):");
		nomeCompleto = entrada.nextLine().toUpperCase(); // Lê o nome completo do usuário e converte para maiúsculas

		// For para percorrer o nomeCompleto e retornar a soma das letras baseadas em sua posição no alfabeto e a soma se tiver algum acento ou caractere inválido
		for (char letra : nomeCompleto.toCharArray()) {
			if (letra >= 'A' && letra <= 'Z') {
				soma += letra - 'A' + 1;
			} else if (letra != ' ') {
				acentoCaractereInvalido += 1;
			}
		}

		// Estrutura condicional para verificar se têm acento ou caractere inválido
		if (acentoCaractereInvalido < 1) {

			// Estrutura condicional para verificar se a soma resultou em valor par ou ímpar e qual o conteúdo da mensagem
			if (soma % 2 == 0) {
				parImpar = "Par";
				mensagem = "seja bem-vindo(a), você é incrível!";
			} else {
				parImpar = "Ímpar";
				mensagem = "seu nome é único e especial. Continue sendo você mesmo!";
			}
			System.out.println("Meu nome deu o valor " + soma + ", que é " + parImpar + ", assim a saída foi:");
			System.out.println(nomeCompleto + ", " + mensagem);
		} else {
			System.out.println("Você digitou seu nome com acento ou caractere inválido!");
		}
		entrada.close(); // Fechar o Scanner
	}

}
/*
Entrada:
	David Sousa da Silva
Saída:
	Meu nome deu o valor 183, que é Ímpar, assim a saída foi:
	DAVID SOUSA DA SILVA, seu nome é único e especial. Continue sendo você mesmo!
 */
