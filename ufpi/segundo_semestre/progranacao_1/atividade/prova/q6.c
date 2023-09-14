/******************************************************************************
Considere a seguinte função em C (o operador && em C significa um “e" lógico):
As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 
se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs
compradas, calcule e escreva o custo total da compra.
*******************************************************************************/
#include<stdio.h>
#include<stdlib.h>

int main() {
	int qtd;
	float macas, valor;
	printf("Quantas maçãs você quer comprar: ");
	scanf("%d", &qtd);
		if(qtd>=12){
		macas = (qtd*1.00);
		}
		else{
		macas = (qtd*1.30);
		}     
	printf("O valor total da compra das maçãs e de: %.2f", macas);
return 0;
}
