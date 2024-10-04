import java.util.Scanner; // Importação da biblioteca Scanner

 

public class App {

   public static void main(String[] args) {

       Scanner entrada = new Scanner(System.in); // Scanner para entrada de dados

 

       // Declaração das variáveis

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

           if (soma % 2 == 0 ) {

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