import java.util.Scanner;  

class ContaTerminal {
  public static void main(String[] args) {
    try (Scanner entrada = new Scanner(System.in)) {
      System.out.print("Digite o numero da conta: ");
      int numeroConta = entrada.nextInt(); 
      entrada.nextLine();
      System.out.print("Digite a agência da conta: ");
      String agenciaConta = entrada.nextLine(); 
      System.out.print("Digite o nome do cliente: ");
      String nomeConta = entrada.nextLine(); 
      System.out.print("Digite o saldo da conta: ");
      Double saldoConta = entrada.nextDouble(); 
      System.out.println("Olá " + nomeConta + ", obrigado por criar uma conta no nosso banco, sua asua agência é "
      + agenciaConta + " conta " + numeroConta + " e seu saldo " + saldoConta + " já esta disponivel para saque.");
    } 
  }
}