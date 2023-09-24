#include<stdio.h>
#include<stdlib.h>
int main(){

 int vet1[8], x, cont = 0, soma, soma2;//contador em 0

for(x=0;x<=7;x++){
    printf("\n Digite o %d valor: ", x+1);
    scanf("%d",&vet1[x]);
        if(vet1[x]<30){
           cont++;
           soma=soma+vet1[x];
           }
          }
         for(x=0;x<=7;x++)
           printf("\n %d",vet1[x]);
           printf("\n \n %d - Numeros sao menores que 30",cont);
        // nao tem variavel declarada soma1  
        //printf("\n \n A Soma dos numeros menores que 30 e = %d",soma1);
        printf("\n \n A Soma dos numeros menores que 30 e = %d",soma);//variavel soma1 substituida por soma
        for(x=0;x<=7;x++)
            soma2=soma2+vet1[x];
            printf("\n\n A Soma dos numeros digitados e = %d",soma2);
            printf("\n\n");
system("pause");

return(0);

}
