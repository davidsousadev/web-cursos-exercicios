#include <stdio.h>

int main() {
    float valorCompra, valorVenda;
    float lucro;

    // Solicitar ao usuário para digitar o valor de compra
    printf("Digite o valor de compra do produto: ");
    scanf("%f", &valorCompra);

    // Calcular o lucro com base no valor de compra
    if (valorCompra < 20.0) {
        lucro = 0.45; // Lucro de 45% para valor de compra menor que R$ 20,00
    } else {
        lucro = 0.30; // Lucro de 30% para valor de compra igual ou maior que R$ 20,00
    }

    // Calcular o valor de venda
    valorVenda = valorCompra * (1 + lucro);

    // Exibir o valor de venda
    printf("O valor de venda do produto é: R$ %.2f\n", valorVenda);

    return 0;
}
