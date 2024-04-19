package atividade;

import java.util.Scanner;

public class Media {
    public static void main(String[] args) {
        float media, nota1, nota2;
        Scanner entrada = new Scanner(System.in);
        System.out.print("Digite a primeira nota: ");
        nota1 = entrada.nextFloat();
        System.out.print("Digite a segunda nota: ");
        nota2 = entrada.nextFloat();
        media = (nota1 + nota2) / 2;
        System.out.println("A média das duas notas é: " + media);
        entrada.close();
    }
}