import java.util.Scanner;

public class RestoDaDivisao {
    public static void main(String[] args) {
        int numero1, numero2, resto;
        Scanner entrada = new Scanner(System.in);
        System.out.print("Digite o primeiro número inteiro: ");
        numero1 = entrada.nextInt();
        System.out.print("Digite o segundo número inteiro: ");
        numero2 = entrada.nextInt();
        //Condição da questão
        if (numero1 < 10) {
            resto = numero2 % numero1;
            System.out.println("O resto da divisão inteira de "+ numero2 +" por "+numero1+" é: " + resto);
        }
        else{
            //Resto da divisão
            resto = numero1 % numero2;
            System.out.println("O resto da divisão inteira de "+ numero1 +" por "+ numero2 +" é: " + resto);
        }
        entrada.close();
    }
}
 