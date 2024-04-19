import java.util.Scanner;
public class Multiplicacao {
    public static void main(String[] args) {
        int numero1, numero2, multiplicacao;
        Scanner entrada = new Scanner(System.in);
        System.out.print("Digite o primeiro número inteiro: ");
        numero1 = entrada.nextInt();
        System.out.print("Digite o segundo número inteiro: ");
        numero2 = entrada.nextInt();
        multiplicacao = numero1 * numero2;
        System.out.println("A multiplicacao dos dois números inteiros é: " + multiplicacao);
        entrada.close();
    }
}
