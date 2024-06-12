

/**
* UNIVERSIDADE FEDERAL DO PIAUÍ
* CENTRO DE EDUCAÇÃO ABERTA E A DISTÂNCIA
* CURSO DE LICENCIATURA EM COMPUTAÇÃO
* DISCIPLINA: ESTRUTURA DE DADOS
* PROFª Dr. Francisco Airton Silva
* Aluno: David Sousa da Silva

TRABALHO 02

Você deve implementar um sistema que representa um banco. Abaixo serão descritos os requisitos deste sistema. Para atingir a nota máxima neste trabalho, deverá atender a todos os tais requisitos.

Você deverá criar as seguintes classes (no mínimo):

Cliente, que possui os atributos: “String nome” e “String cpf”.
Atendente, que possui o atributo: String nome.
FilaClientes que possui o atributo “Clientes[] clientes” e toda a implementação dos métodos de fila mostrado na vídeo-aula.
Banco, que possui os atributos: “Atendente[] atendentes” e “FilaClientes filaClientes”;
Atendimento, que possui os atributos: “Cliente cliente” e “Atendente atendente”
BancoEmFuncionamento, onde, contendo um método main, irá fazer o banco funcionar, criando atendentes, clientes e uma fila de clientes. Vai adicionar os clientes na fila e depois retirá-los da fila para criar atendimentos.

Não se deve usar a classe List (ou derivadas) nativa do Java para este trabalho. Caso use receberá zero na nota.
Esta especificação de sistema acima é só uma base, sinta-se livre para incrementar a ideia e tornar seu trabalho mais rico de detalhes.
Postar no SIGAA um arquivo .zip contendo todas as classes do seu sistema **/

//import java.util.InputMismatchException;
//import java.util.Scanner;

package src;

public class BancoEmFuncionamento {
    public static void main(String[] args) throws Exception {
        
        FilaClientes filaClientes =  new FilaClientes(10);
        System.out.println(filaClientes);
        Cliente cliente = new Cliente("David", "14785236987");
        Cliente cliente2 = new Cliente("David", "14785236987");
        filaClientes.enqueue(cliente);
        filaClientes.enqueue(cliente2);
        System.out.println(filaClientes);
    }
}

/*int 
Scanner entrada = new Scanner(System.in);
        

opcao = 0;
        System.out.println("----------- Bem vindo ao David Bank -------------");
        do {
            System.out.println("--------------------- Menu ----------------------");
            System.out.println("1 = Criar cadastro.");
            
            System.out.println("2 = Imprimir Lista Original.");
            System.out.println("3 = Converter lista para maiúsculas.");
            System.out.println("4 = Remover strings que contêm a letra 'a'.");
            System.out.println("5 = Imprimir Lista Final Modificada.");
            
            System.out.println("0 = Sair.");
            System.out.println("-------------------------------------------------");
            System.out.print("Digite uma das opções acima: ");

            // Tratamento de exceções.
            try {
                opcao = entrada.nextInt();
                entrada.nextLine();
                System.out.println();
            } catch (InputMismatchException e) {
                // entrada.nextLine();
                opcao = -1;
                System.out.println();
            }
            switch (opcao) {
                case 1:
                    System.out.print("Digite seu primeiro nome completo: ");
                    String nome = entrada.nextLine();
                    System.out.print("Digite seu cpf (Apenas os digitos): ");
                    String cpf = entrada.nextLine();
                    System.out.println("\nNome: " + nome + " CPF: " + cpf);
                    // Cliente.cadastro(nome, cpf);
                    System.out.println("Cadastro realizado com sucesso!");
                    break;
                // Encerrar o programa
                case 0:
                    System.out.println("Programa Finalizado!\n");
                    break;
                // Caso seja digitada uma opção inválida
                default:
                    System.out.println("Opção inválida!\n");
                    break;
            }
        } while (opcao != 0);
         // Fechar os Scanner's.
        entrada.close();
        
        */