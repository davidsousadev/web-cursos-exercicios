import java.util.Scanner;

public class Soma {
    public static void main(String[] args) {
        int numero1, numero2, soma;
        Scanner entrada = new Scanner(System.in);
        System.out.print("Digite o primeiro número inteiro: ");
        numero1 = entrada.nextInt();
        System.out.print("Digite o segundo número inteiro: ");
        numero2 = entrada.nextInt();
        soma = numero1 + numero2;
        System.out.println("A soma dos dois números inteiros é: " + soma);
        entrada.close();
    }
}