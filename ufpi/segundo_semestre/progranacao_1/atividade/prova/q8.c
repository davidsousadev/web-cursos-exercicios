/******************************************************************************
A aplicação ler elementos de uma matriz, mostra a matriz e o valor de cada elemento 
na matriz dividido por 2
*******************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
int main(){//faltou o tipo de retorno da função main 
    int lin,col;//removi a variavel tab
    float mat[3][3], mat1[3][3];//mudei para inserir valores em float
        for (lin=0; lin<3; lin++){
            for (col=0;col<3;col++){//faltou for de ler as colunas
            printf("Digite ELEMENTO da linha %d, coluna %d da matriz: ",lin+1,col+1);
            scanf("%f", &mat[lin][col]);  
            }
            printf("\n\n");
        }
        printf("Matriz original\n\n");
        for (lin=0;lin<3;lin++){//alterei para lin<3 so para ficar iguais
            for (col=0;col<3;col++){//faltou as chves
                printf("%.2f\t",mat[lin][col]);
            }
            printf("\n\n");
        }
        printf("Matriz com elementos divididos por 2\n\n");
        for (lin=0;lin<3;lin++){//alterei para lin<3 so para ficar iguais
            for (col=0;col<3;col++){
                mat1[lin][col] = (mat[lin][col])/2;
                //for (lin=0;lin<3;lin++){//for desnecessário
                    //for (col=0;col<3;col++){//for desnecessário
                        printf("%.2f\t",mat1[lin][col]);
                    //}
                //}
            }
            printf("\n\n");
        }
    system("pause");
return 0;
}
