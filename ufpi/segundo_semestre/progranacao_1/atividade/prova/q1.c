/******************************************************************************

Um professor, muito legal, fez 4 provas durante um semestre mas só vai levar em 
conta as três notas mais altas para calcular a média. Utilizando Função faça uma 
aplicação em C que peça o valor das 4 notas, mostre como seria a média com essas 
4 provas, a média com as 3 notas mais altas, bem como sua nota mais alta e sua nota mais baixa.

*******************************************************************************/
#include<stdio.h>
#include<stdlib.h>
float media(float media){
    media = (media/4);
    return(media);    
}
int main() {
	int i;
    float notas[4], mediatotal;
    float mediamaior, maiornota, menornota = 0;
	for(i=0; i<4; i++){
        printf("Digite a nota  %d: ",i+1);
        scanf("%f", &notas[i]);
        if(notas[i]>=maiornota){
        	if(notas[i]>=menornota){
        		maiornota = notas[i];
				if(menornota==0){
				menornota = notas[i];	
			}
        	}
        	else{
        		menornota = notas[i];	
			}
		}
		else{
			 if(notas[i]<=menornota){
			 	menornota = notas[i];
			 }
		}
        mediatotal += notas[i];
    }
    mediamaior = ((mediatotal-menornota)/3);
    mediatotal = media(mediatotal);
    printf("\nMedia de todas notas: %.2f\n", mediatotal);
    printf("Media das 3 notas mais altas: %.2f\n", mediamaior);
    printf("Nota maior: %.2f\n", maiornota);
    printf("Nota menor: %.2f\n", menornota);   
return 0;
}
