// 1. Faça um programa que leia dois valores numéricos inteiros e apresente
// o resultado da diferença do maior valor pelo menor valor. Se os valores
// forem iguais, o programa deve mostrar zero.

import java.util.Scanner;

public class Q1 {
    public static void main(String[] args) {
        int numero1, numero2, resultado;
        Scanner entrada = new Scanner(System.in);
        numero1 = entrada.nextInt();
        numero2 = entrada.nextInt();
        if (numero1 > numero2) {
            resultado = numero1 - numero2;
        }

        System.out.println(resultado);

        entrada.close();
    }
}
