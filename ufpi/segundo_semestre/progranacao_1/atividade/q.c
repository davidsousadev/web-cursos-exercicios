#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
int main(){
  int linhas = 0, colunas = 0, opcao, pesquisa;
  int contadorLinhas = 0, contadorColunas = 0;
  int **dados, contador = 0, dado;
  bool verificador=false;
    do{
        fflush(stdin);
        printf ("\nMenu:\n");
        printf ("1 = Definir quantidade de dados:\n");
        printf ("2 = Inserir dados:\n");
        printf ("3 = Apresentar dados:\n");
        printf ("4 = Pesquisar dados:\n");
        printf ("5 = Atualizar dados:\n");
        printf ("6 = Mostrar a quantidade de dados:\n");
        printf ("0 = Sair da aplicação:\n");
        printf ("Escolha uma opção:");
        scanf ("%d", &opcao);
        switch(opcao){
            case 1:
                fflush(stdin);
                printf ("Qual a quantidade de dados a serem inseridos em linhas:");
                scanf ("%d", &linhas);
                printf ("Qual a quantidade de dados a serem inseridos em colunas:");
                scanf ("%d", &colunas);
                contadorLinhas = linhas;
                contadorColunas = colunas;
                dados = malloc(linhas * sizeof(int*));
                    for(linhas = 0; linhas < contadorLinhas; linhas++){
                            dados[linhas] = malloc(colunas * sizeof(int));
                        }
                    break;
            case 2:
                for(linhas = 0; linhas < contadorLinhas; linhas++){
                    for(colunas = 0; colunas < contadorColunas; colunas++){
                        printf("Digite a informacao da linha %d coluna %d:", linhas+1, colunas+1);
                        scanf("%d", &dado);
                        dados[linhas][colunas] = dado;
                    }
                }
                break;
            case 3:
                printf("Dados cadastrados:\n");
                for(linhas = 0; linhas < contadorLinhas; linhas++){
                    for(colunas = 0; colunas < contadorColunas; colunas++){
                        printf(" %d |", dados[linhas][colunas]);
                    }
                    printf("\n");
                }
                    
                break;
            case 4:
                fflush(stdin);
                printf ("Qual o dado que procura:");
                scanf("%d", &pesquisa);
                for(linhas = 0; linhas < contadorLinhas; linhas++){
                    for(colunas = 0; colunas < contadorColunas; colunas++){
                        if(pesquisa==dados[linhas][colunas]){
                            printf("\nO dado ( %d ) esta na linha %d e coluna %d", pesquisa, linhas+1, colunas+1);
                            verificador = true;
                        }
                    }
                }
                if(verificador==false){
                    printf("Nenhum dado encontrado"); 
                }
                verificador=false;
                break;
            case 5:
                fflush(stdin);
                printf("Em que linha e coluna esta o dado que deseja atualizar:\n");
                printf ("Qual a linha:");
                scanf ("%d", &linhas);
                printf ("Qual a coluna:");
                scanf ("%d", &colunas);
                printf ("Digite o novo dado para a linha %d coluna %d:", linhas, colunas);
                scanf ("%d", &dado);
                linhas--;
                colunas--;
                dados[linhas][colunas] = dado;
                break;
            case 6:
                for(linhas = 0; linhas < contadorLinhas; linhas++){
                    for(colunas = 0; colunas < contadorColunas; colunas++){
                        contador++;
                    }
                }
                printf("Quantidade de dados: %d", contador);
                break;
            case 0:
                printf("Saindo da aplicação!");
                break;  
            default:
                printf("Opção invalida!");
        }
    }
  while (opcao != 0);
  return 0;
}
