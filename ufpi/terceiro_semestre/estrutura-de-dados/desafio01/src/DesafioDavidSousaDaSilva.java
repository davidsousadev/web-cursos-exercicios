
/**
 * UNIVERSIDADE FEDERAL DO PIAUÍ
 * CENTRO DE EDUCAÇÃO ABERTA E A DISTÂNCIA
 * CURSO DE LICENCIATURA EM COMPUTAÇÃO
 * DISCIPLINA: ESTRUTURA DE DADOS
 * PROFª Dr. Francisco Airton Silva
 * Aluno: David Sousa da Silva
  
   **/
/**TRABALHO 01
Descrição: (Este trabalho vale 2,0 pontos)

Usando as classes List e Arraylist, nativas da linguagem Java, crie um programa Java que receba uma lista de strings e execute as seguintes operações:

1. Imprima a lista original.

2. Converta todas as strings da lista em maiúsculas.

3. Remova todas as strings que contenham a letra 'a'.

4. Imprima a lista final. **/

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class DesafioDavidSousaDaSilva {
    public static void main(String[] args) throws Exception {
        List<String> listaModificada = new ArrayList<>();
        List<String> listaOriginal = new ArrayList<>();
        Scanner entrada = new Scanner(System.in);
        Scanner itens = new Scanner(System.in);
        String item = null;
        int opcao = 0;
        Boolean modificacao = false;

        do {
            System.out.println("--------------------- Menu ----------------------");
            System.out.println("1 = Adicionar String");
            System.out.println("2 = Imprimir Lista Original");
            System.out.println("3 = Converter lista para maiúsculas");
            System.out.println("4 = Remover strings que contêm a letra 'a'");
            System.out.println("5 = Imprimir Lista Final Modificada");
            System.out.println("0 = Sair");
            System.out.println("-------------------------------------------------");
            System.out.print("Digite uma das opções acima: ");
            opcao = entrada.nextInt();
            System.out.println();
            switch (opcao) {
                case 1:
                    // Adicionar as Strings
                    System.out.print("Digite uma string para adicionar: ");
                    item = itens.nextLine();
                    listaModificada.add(item);
                    if (modificacao != true) {
                        listaOriginal.add(item);
                    }
                    else{
                        listaModificada.add(item);
                    }
                    break;
                case 2:
                    // Imprimir a lista Original
                    if (listaOriginal.size() != 0) {
                        System.out.println("Lista original:");
                        imprimirLista(listaOriginal);
                    } else if (listaOriginal.size() == 0){
                        System.out.println("A lista ainda não foi definida!\n");
                    }
                    break;
                case 3:
                    // Converter lista para letras maiúsculas
                    if (modificacao != true && listaOriginal.size() != 0) {
                        converterParaMaiusculas(listaModificada);
                        modificacao = true;
                        System.out.println("Lista convertida para maiúsculas.\n");
                    } else if (listaOriginal.size() == 0){
                        System.out.println("A lista ainda não foi definida!\n");
                    }
                    break;
                case 4:
                    // Remover strings que contêm a letra 'a'
                    if (modificacao != true && listaOriginal.size() != 0) {
                        removerStringsComLetraA(listaModificada);
                        modificacao = true;
                        System.out.println("Strings contendo 'a' foram removidas.\n");
                    } else if (listaOriginal.size() == 0){
                        System.out.println("A lista ainda não foi definida!\n");
                    }
                    break;
                case 5:
                    // Imprimir Lista Final Modificada
                    if (listaOriginal.size() == 0) {
                        System.out.println("A lista ainda não foi definida!\n");
                    } else if (listaOriginal.equals(listaModificada)) {
                        System.out.println("A lista ainda não foi modificada!\n");
                    } else {
                        System.out.println("Lista final modificada:");
                        imprimirLista(listaModificada);
                    }
                    break;
                case 0:
                    System.out.println("Programa Finalizado!");
                    break;
                default:
                    System.out.println("Opção inválida!\n");
                    break;
            }
        } while (opcao != 0);

        entrada.close();
        itens.close();
    }
    // Métodos

    // 1. Imprima a lista original.
    // 4. Imprima a lista final.
    private static void imprimirLista(List<String> lista) {
        int contador = 1;
        for (String str : lista) {
            System.out.println(contador+" : "+str);
            contador++;
        }
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