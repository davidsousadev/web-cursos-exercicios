package atividade;
/* 
1. Faça um programa que receba dois números, calcule e mostre a subtração do primeiro número pelo segundo.
Algoritmo “Subtração” 

var

numA, numB, sub: inteiro

início

leia numA

leia numB

sub ← numA - numB

escreva sub

fim
 */
public class q1 {
    public static void main(String[] args) {
        double numA, numB, sub;
        System.out.print("Digite um número: ");
        numA = Double.parseDouble(System.console().readLine());
        System.out.print("Digite um número: ");
        numB = Double.parseDouble(System.console().readLine());

        sub = numA - numB;

        System.out.printf("A subtração dos número: %.1f\n", sub);
    }
}
