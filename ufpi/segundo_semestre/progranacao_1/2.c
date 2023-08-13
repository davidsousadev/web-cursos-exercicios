#include <stdio.h>

int main() {
    float salario, valorEmprestimo, taxaJuros;
    int prestacoes;

    // Solicitar ao usuário para digitar os valores
    printf("Digite o valor do salário: ");
    scanf("%f", &salario);

    printf("Digite o valor do empréstimo: ");
    scanf("%f", &valorEmprestimo);

    printf("Digite a quantidade de prestações: ");
    scanf("%d", &prestacoes);

    printf("Digite a taxa de juros (em porcentagem): ");
    scanf("%f", &taxaJuros);

    // Calcular o valor máximo da prestação (30% do salário)
    float valorMaxPrestacao = salario * 0.3;

    // Calcular o valor da prestação
    float taxaJurosDecimal = taxaJuros / 100.0;
    float valorPrestacao = (valorEmprestimo * taxaJurosDecimal) / prestacoes;

    // Verificar se o empréstimo é permitido
    if (valorPrestacao <= valorMaxPrestacao) {
        printf("Empréstimo permitido!\n");
        printf("Valor da prestação: R$ %.2f\n", valorPrestacao);
        printf("Valor total a pagar: R$ %.2f\n", valorEmprestimo * (1 + taxaJurosDecimal));
    } else {
        printf("Empréstimo não permitido. A prestação excede 30%% do salário.\n");
    }

    return 0;
}
