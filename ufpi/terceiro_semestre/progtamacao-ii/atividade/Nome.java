import java.util.Scanner;

public class Nome {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.print("Digite o seu primeiro nome: ");
        String nome = entrada.nextLine();
        System.out.println("Seu primeiro nome é: " + nome);
        entrada.close();
    }
}

