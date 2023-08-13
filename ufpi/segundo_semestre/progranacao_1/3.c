#include <stdio.h>

int main() {
    int n; // Número de espectadores
    int idade, opiniao;
    int excelente = 0, bom = 0, regular = 0;
    int somaIdadeExcelente = 0, somaIdadeBom = 0, somaIdadeRegular = 0;

    printf("Digite o número de espectadores: ");
    scanf("%d", &n);

    for (int i = 1; i <= n; i++) {
        printf("Digite a idade do espectador %d: ", i);
        scanf("%d", &idade);

        printf("Digite a opinião (3 - excelente, 2 - bom, 1 - regular) do espectador %d: ", i);
        scanf("%d", &opiniao);

        switch (opiniao) {
            case 3:
                excelente++;
                somaIdadeExcelente += idade;
                break;
            case 2:
                bom++;
                somaIdadeBom += idade;
                break;
            case 1:
                regular++;
                somaIdadeRegular += idade;
                break;
            default:
                printf("Opinião inválida.\n");
        }
    }

    printf("Quantidade de pessoas em cada opinião:\n");
    printf("Excelente: %d\n", excelente);
    printf("Bom: %d\n", bom);
    printf("Regular: %d\n", regular);

    printf("\nMédia de idade das pessoas em cada opinião:\n");
    if (excelente > 0)
        printf("Excelente: %.2f\n", (float)somaIdadeExcelente / excelente);
    if (bom > 0)
        printf("Bom: %.2f\n", (float)somaIdadeBom / bom);
    if (regular > 0)
        printf("Regular: %.2f\n", (float)somaIdadeRegular / regular);

    printf("\nPorcentagem de resposta para cada opinião:\n");
    printf("Excelente: %.2f%%\n", ((float)excelente / n) * 100);
    printf("Bom: %.2f%%\n", ((float)bom / n) * 100);
    printf("Regular: %.2f%%\n", ((float)regular / n) * 100);

    return 0;
}
