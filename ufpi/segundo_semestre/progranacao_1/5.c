#include <stdio.h>
#include <stdlib.h>
int main() {
    float valor, aVista, aPrazo, total;
    int n, opcao;
    char cod;

    printf("Digite o número de transações: ");
    scanf("%d", &n);
    aVista = 0;
    aPrazo = 0;
    total = 0;
    for (int i = 1; i <= n; i++) {
        printf("\nDigite o código (V) - à vista e (P) - a prazo\n");
        printf("Transacao %d: ", i);
        scanf(" %c", &cod);
        printf("\nDigite o valor: ");
        scanf("%f", &valor);
        
        if(cod == 'V' || cod == 'v'){
           aVista = aVista + valor; 
        }
        else if(cod == 'P' || cod == 'p'){
            aPrazo = aPrazo + valor;
        }
        else{
            printf("Codigo ( %c ) invalido digite novamente\n", cod);
            i--;
            system ("PAUSE");
        }
        total = total + valor;
    }
    printf("\nValor total das compras à vista: R$ %.2f\n", aVista);
/*
    do {
        printf("\nMenu:\n");
        printf("1. Valor total das compras à vista\n");
        printf("2. Valor total das compras a prazo\n");
        printf("3. Valor total das compras efetuadas\n");
        printf("4. Sair da aplicação\n");
        printf("Escolha uma opção: ");
        scanf("%d", &escolha);

        switch (escolha) {
            case 1:
                printf("Valor total das compras à vista: R$ %.2f\n", totalVista);
                break;
            case 2:
                printf("Valor total das compras a prazo: R$ %.2f\n", totalPrazo);
                break;
            case 3:
                printf("Valor total das compras efetuadas: R$ %.2f\n", totalCompras);
                break;
            case 4:
                printf("Saindo da aplicação.\n");
                break;
            default:
                printf("Opção inválida.\n");
        }
    } while (escolha != 4);
*/
    return 0;
}

/*#include <stdio.h>

int main() {
    int n; // Número de transações
    float valor, totalVista = 0, totalPrazo = 0, totalCompras = 0;
    char codigo;

    printf("Digite o número de transações: ");
    scanf("%d", &n);

    for (int i = 1; i <= n; i++) {
        printf("Digite o código da transação (V para à vista, P para a prazo): ");
        scanf(" %c", &codigo);

        printf("Digite o valor da transação: ");
        scanf("%f", &valor);

        switch (codigo) {
            case 'V':
            case 'v':
                totalVista += valor;
                break;
            case 'P':
            case 'p':
                totalPrazo += valor;
                break;
            default:
                printf("Código inválido.\n");
        }

        totalCompras += valor;
    }

    int escolha;
    do {
        printf("\nMenu:\n");
        printf("1. Valor total das compras à vista\n");
        printf("2. Valor total das compras a prazo\n");
        printf("3. Valor total das compras efetuadas\n");
        printf("4. Sair da aplicação\n");
        printf("Escolha uma opção: ");
        scanf("%d", &escolha);

        switch (escolha) {
            case 1:
                printf("Valor total das compras à vista: R$ %.2f\n", totalVista);
                break;
            case 2:
                printf("Valor total das compras a prazo: R$ %.2f\n", totalPrazo);
                break;
            case 3:
                printf("Valor total das compras efetuadas: R$ %.2f\n", totalCompras);
                break;
            case 4:
                printf("Saindo da aplicação.\n");
                break;
            default:
                printf("Opção inválida.\n");
        }
    } while (escolha != 4);

    return 0;
}
*/