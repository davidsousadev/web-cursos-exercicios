import java.util.Scanner;

public class ParOuImpar {
    public static void main(String[] args) {
        int numero;
        Scanner entrada = new Scanner(System.in);
        System.out.print("Digite o número inteiro: ");
        numero = entrada.nextInt();
        
        // Condição da questão
        if (numero % 2 == 0) {
            System.out.println("O número intero "+numero+" é par.");
        } else {
            System.out.println("O número intero "+numero+" é ímpar.");
        }
        entrada.close();
    }
}