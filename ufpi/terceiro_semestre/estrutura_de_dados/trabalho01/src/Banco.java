import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Scanner;

public class Banco {
    public static void main(String[] args) {
        // Cria a lista de strings
        List<String> lista = new ArrayList<>();
        
        // Recebe entradas do usuário
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite strings para adicionar à lista (digite 'fim' para encerrar):");
        
        while (true) {
            String entrada = scanner.nextLine();
            if (entrada.equalsIgnoreCase("fim")) {
                break;
            }
            lista.add(entrada);
        }
        
        // Imprime a lista original
        System.out.println("Lista original:");
        imprimirLista(lista);
        
        // Converte todas as strings para maiúsculas
        converterParaMaiusculas(lista);
        
        // Remove todas as strings que contêm a letra 'a'
        removerStringsComLetraA(lista);
        
        // Imprime a lista final
        System.out.println("Lista final:");
        imprimirLista(lista);
        
        scanner.close();
    }
    
    // Método para imprimir a lista
    private static void imprimirLista(List<String> lista) {
        for (String str : lista) {
            System.out.println(str);
        }
    }
    
    // Método para converter todas as strings para maiúsculas
    private static void converterParaMaiusculas(List<String> lista) {
        for (int i = 0; i < lista.size(); i++) {
            lista.set(i, lista.get(i).toUpperCase());
        }
    }
    
    // Método para remover todas as strings que contêm a letra 'a'
    private static void removerStringsComLetraA(List<String> lista) {
        Iterator<String> iterator = lista.iterator();
        while (iterator.hasNext()) {
            String str = iterator.next();
            if (str.contains("A")) {
                iterator.remove();
            }
        }
    }
}

