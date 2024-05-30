/**
* UNIVERSIDADE FEDERAL DO PIAUÍ
* CENTRO DE EDUCAÇÃO ABERTA E A DISTÂNCIA
* CURSO DE LICENCIATURA EM COMPUTAÇÃO
* DISCIPLINA: ESTRUTURA DE DADOS
* PROFª Dr. Francisco Airton Silva
* Aluno: David Sousa da Silva

TRABALHO 01

Descrição: (Este trabalho vale 2,0 pontos)

Usando as classes List e Arraylist, nativas da linguagem Java, crie um programa Java que receba uma lista de strings e execute as seguintes operações:

1. Imprima a lista original.

2. Converta todas as strings da lista em maiúsculas.

3. Remova todas as strings que contenham a letra 'a'.

4. Imprima a lista final. **/
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.InputMismatchException;

public class TrabalhoDavidSousaDaSilva {
    public static void main(String[] args) throws Exception {
        List<String> listaModificada = new ArrayList<>();
        List<String> listaOriginal = new ArrayList<>();
        Scanner entrada = new Scanner(System.in);
        Scanner itens = new Scanner(System.in);
        Boolean conversao = false;
        Boolean remocao = false;
        String item = null;
        int opcao = 0;
        
        
        //Escolhi usar o Do While para garantir que o loop seja executado pelo menos uma vez.
        do {
            System.out.println("--------------------- Menu ----------------------");
            System.out.println("1 = Adicionar String.");
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
                entrada.nextLine();
                opcao = -1;
                System.out.println();
            }
            switch (opcao) {
                // Adicionar as Strings.
                case 1:
                System.out.print("Digite uma string para adicionar: ");
                item = itens.nextLine();
                if (!remocao && !conversao) {
                    listaOriginal.add(item);
                    listaModificada.add(item);
                }
                else if(remocao || conversao){
                    listaModificada.add(item);
                    remocao = false;
                    conversao = false; 
                }
                System.out.println("String adicionada.\n");
                break;
                // Imprimir a lista Original.
                case 2:
                if (!listaOriginal.isEmpty()) {
                    System.out.println("Lista original:");
                    imprimirLista(listaOriginal);
                } else {
                    System.out.println("A lista ainda não foi definida!\n");
                }
                break;
                // Converter lista para letras maiúsculas.
                case 3:
                if (!conversao && !listaOriginal.isEmpty()) {
                    converterParaMaiusculas(listaModificada);
                    conversao = true;
                    System.out.println("Lista convertida para maiúsculas.\n");
                } else if (listaOriginal.isEmpty()) {
                    System.out.println("A lista ainda não foi definida!\n");
                } else {
                    converterParaMaiusculas(listaModificada);
                    System.out.println("Lista convertida para maiúsculas novamente.\n");
                }
                break;
                // Remover strings que contém a letra 'a'.
                case 4:   
                if (!remocao && !listaOriginal.isEmpty()) {
                    removerStringsComLetraA(listaModificada);
                    remocao = true;
                    System.out.println("Strings contendo 'a' foram removidas.\n");
                } else if (listaOriginal.isEmpty()) {
                    System.out.println("A lista ainda não foi definida!\n");
                } else {
                    removerStringsComLetraA(listaModificada);
                    System.out.println("Strings contendo 'a' foram removidas novamente.\n");
                }
                break;
                // Imprimir Lista Final Modificada
                case 5:
                if (listaOriginal.isEmpty()) {
                    System.out.println("A lista ainda não foi definida!\n");
                } else if (listaOriginal.equals(listaModificada) && (!remocao || !conversao)) {
                    System.out.println("A lista ainda não foi modificada!\n");
                } else {
                    if (remocao && conversao) {
                        System.out.println("Lista final modificada:");
                        imprimirLista(listaModificada);  
                    }
                    else if (remocao || conversao || !listaOriginal.equals(listaModificada)){
                        System.out.println("Lista parcialmente modificada:");
                        imprimirLista(listaModificada);
                    }
                }
                break;
                //Encerrar o programa
                case 0:
                System.out.println("Programa Finalizado!\n");
                break;
                //Caso seja digitada uma opção inválida
                default:
                System.out.println("Opção inválida!\n");
                break;
            }
        } while (opcao != 0);
        
        //Fechar os Scanner's.
        entrada.close();
        itens.close();
    }
    
    // Operações 
    
    // 1. Imprima a lista original.
    // 4. Imprima a lista final.
    private static void imprimirLista(List<String> lista) {
        int contador = 1;
        for (String str : lista) {
            System.out.println(contador + " : " + str);
            contador++;
        }
        System.out.println("\nTotal de Strings: "+lista.size()+"\n");
    }
    
    // 2. Converta todas as strings da lista em maiúsculas.
    private static void converterParaMaiusculas(List<String> lista) {
        for (int i = 0; i < lista.size(); i++) {
            lista.set(i, lista.get(i).toUpperCase());
        }
    }
    
    // 3. Remova todas as strings que contenham a letra 'a'.
    private static void removerStringsComLetraA(List<String> lista) {
        lista.removeIf(str -> str.contains("A") || str.contains("a"));
    }
}