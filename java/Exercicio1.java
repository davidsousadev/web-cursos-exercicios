public class Exercicio1 {
     public static void main(String[] args) {
        double anoNasc, anoAtual, idadeAnos, idadeMeses, idadeDias, idadeSemanas;
        System.out.print("Digite o ano de nascimento: ");
        anoNasc = Double.parseDouble(System.console().readLine());
        System.out.print("Digite o ano atual: ");
        anoAtual = Double.parseDouble(System.console().readLine());

        idadeAnos = anoAtual - anoNasc;
        idadeMeses = idadeAnos * 12;
        idadeDias = idadeAnos * 365; // Considerando anos comuns
        idadeSemanas = idadeAnos * 52; // Aproximação de semanas em um ano

        System.out.println("Idade em anos: " + idadeAnos);
        System.out.println("Idade em meses: " + idadeMeses);
        System.out.println("Idade em dias: " + idadeDias);
        System.out.println("Idade em semanas: " + idadeSemanas);

     
    }
}
//      Double.parseDouble(System.console().readLine());