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
package src;

import java.util.InputMismatchException;
import java.util.Scanner;

public class BancoEmFuncionamento {
    // Método main
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int opcao = 0;
        FilaAtendentes filaAtendentes = new FilaAtendentes(5);
        String nomeAtendente;
        FilaClientes filaClientes = new FilaClientes(20);
        String nomeCliente;
        String cpfCliente;
        int numeroDoAtendimento = 0;

        System.out.println("----------- Bem vindo ao David Bank -------------");
        do {
            System.out.println("--------------------- Menu ----------------------");
            System.out.println("1 = Adicionar atendentes. Capacidade(5)");
            System.out.println("2 = Listar atendentes.");
            System.out.println("3 = Adicionar clientes. Capacidade(20)");
            System.out.println("4 = Listar Clientes.");
            System.out.println("5 = Iniciar atendimentos.");
            System.out.println("6 = Adicionar em massa 5 atendentes e 20 clientes pré-cadastrados.");
            System.out.println("0 = Sair.");
            System.out.println("-------------------------------------------------");
            System.out.print("Digite uma das opções acima: ");

            // Tratamento de exceções.
            try {
                opcao = entrada.nextInt();
                entrada.nextLine();
                System.out.println();
            } catch (InputMismatchException e) {
                entrada.nextLine();
                opcao = -1;
                System.out.println();
            }
            switch (opcao) {
                case 1:
                    // Criar atendente
                    if(!filaAtendentes.isFull()){
                    System.out.print("Digite o nome do atendente: ");
                    nomeAtendente = entrada.nextLine();
                    filaAtendentes.enqueue(new Atendente(nomeAtendente));
                    System.out.println("Atendente: " + nomeAtendente + ", adicionado com sucesso!\n");
                    } else{
                        System.out.println("Já atingiu o limite total de atendentes!\n");
                    }
                    break;
                case 2:
                    // Listar atendentes
                    if(!filaAtendentes.isEmpty()){
                        System.out.println(filaAtendentes);
                    } else{
                        System.out.println("A lista de atendentes está vazia!\n");
                    }
                    break;
                case 3:
                    // Criar cliente
                    if(!filaClientes.isFull()){
                    System.out.print("Digite o nome do cliente: ");
                    nomeCliente = entrada.nextLine();
                    System.out.print("\nDigite o CPF do cliente (apenas os digitos): ");
                    cpfCliente = entrada.nextLine();
                    filaClientes.enqueue(new Cliente(nomeCliente, cpfCliente));
                    System.out.println("Cliente: " + nomeCliente + ", adicionado com sucesso!\n");
                    } else{
                            System.out.println("Já atingiu o total de clientes!\n");
                    }
                    break;
                case 4:
                    // Listar Clientes
                    if(!filaClientes.isEmpty()){
                    System.out.println(filaClientes);
                    } else{
                        System.out.println("A lista de clientes está vazia!\n");
                    }
                    break;
                case 5:
                    // Cria a instância do Banco e processa a lista de atendimentos
                    if (!filaAtendentes.isEmpty() && !filaClientes.isEmpty()) {
                        Banco banco = new Banco(filaAtendentes, filaClientes);
                        while (!banco.getFilaClientes().isEmpty()) {
                            Atendimento atendimento = banco.atenderClientes();
                            System.out.println("Atendimento #"+(numeroDoAtendimento + 1)+": " + atendimento);
                            numeroDoAtendimento++;
                        }
                    } else {
                        System.out.println("Adicione atendentes e ou clientes!!!!\n");
                    }
                    break;
                case 6:
                    // Adição automática de 5 atendentes e 20 clientes pré-cadastrados para otimizar o processo de avaliação
                    if (filaAtendentes.isEmpty() && filaClientes.isEmpty()) {
                    filaAtendentes.enqueue(new Atendente("Aldemir"));
                    filaAtendentes.enqueue(new Atendente("Berenice"));
                    filaAtendentes.enqueue(new Atendente("Carlos"));
                    filaAtendentes.enqueue(new Atendente("David"));
                    filaAtendentes.enqueue(new Atendente("Edivaldo"));
                    filaClientes.enqueue(new Cliente("Cliente 1", "14785236987"));
                    filaClientes.enqueue(new Cliente("Cliente 2", "14785236987"));
                    filaClientes.enqueue(new Cliente("Cliente 3", "14785236987"));
                    filaClientes.enqueue(new Cliente("Cliente 4", "14785236987"));
                    filaClientes.enqueue(new Cliente("Cliente 5", "14785236987"));
                    filaClientes.enqueue(new Cliente("Cliente 6", "14785236987"));
                    filaClientes.enqueue(new Cliente("Cliente 7", "14785236987"));
                    filaClientes.enqueue(new Cliente("Cliente 8", "14785236987"));
                    filaClientes.enqueue(new Cliente("Cliente 9", "14785236987"));
                    filaClientes.enqueue(new Cliente("Cliente 10", "14785236987"));
                    filaClientes.enqueue(new Cliente("Cliente 11", "14785236987"));
                    filaClientes.enqueue(new Cliente("Cliente 12", "14785236987"));
                    filaClientes.enqueue(new Cliente("Cliente 13", "14785236987"));
                    filaClientes.enqueue(new Cliente("Cliente 14", "14785236987"));
                    filaClientes.enqueue(new Cliente("Cliente 15", "14785236987"));
                    filaClientes.enqueue(new Cliente("Cliente 16", "14785236987"));
                    filaClientes.enqueue(new Cliente("Cliente 17", "14785236987"));
                    filaClientes.enqueue(new Cliente("Cliente 18", "14785236987"));
                    filaClientes.enqueue(new Cliente("Cliente 19", "14785236987"));
                    filaClientes.enqueue(new Cliente("Cliente 20", "14785236987"));
                    System.out.println("5 atendentes e 20 clientes adicionados com sucesso!\n");
                }
                else{
                    System.out.println("Não foi possivel adicionar em massa pois já foram adicionandos atendente(s) e ou cliente(s) continue adicionando!\n");
                }
                    break;

                // Encerrar o programa
                case 0:
                    System.out.println("Atendimentos Finalizados!");
                    System.out.println("Total de atendimentos realizados: " + numeroDoAtendimento);
                    break;
                // Caso seja digitada uma opção inválida
                default:
                    System.out.println("Opção inválida!\n");
                    break;
            }
        } while (opcao != 0);

        // Fechar o Scanner
        entrada.close();
    }
}