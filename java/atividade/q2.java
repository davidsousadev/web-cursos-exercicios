package atividade;
/*
 * 2. Faça um programa que receba dois números, calcule e mostre a divisão do primeiro pelo segundo. Sabe-se que o segundo número não pode ser zero, portanto, não é necessário se preocupar com isso neste exercício. 

Algoritmo “Divisão” 

var

numA, numB: inteiro
div: real

início

leia numA

leia numB

div ← numA / numB

escreva div

fim

 */
public class q2 {
    public static void main(String[] args) {
        double numA, numB, sub;
        System.out.print("Digite um número: ");
        numA = Double.parseDouble(System.console().readLine());
        System.out.print("Digite um número: ");
        numB = Double.parseDouble(System.console().readLine());

        sub = numA / numB;

        System.out.printf("A subtração dos número: %.1f\n", sub);
    }
}
