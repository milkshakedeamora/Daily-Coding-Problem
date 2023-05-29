#include <stdio.h>
int encontrado(int * vector, int tamanho, int k){
  for(int i = 0; i < tamanho ; i++){
    for(int j = i+1; j < tamanho ; j++){
        if(vector[i]+vector[j] == k){
            printf("%d + %d = %d",vector[i],vector[j],k);
            return 1;
    }
  }
  return 0;
}
}

int main()
{   
    int tamanho;
    int k;
    printf("Digite o tamanho do Array:");
    scanf("%d",&tamanho);
    int vetor[tamanho];
    
    for(int i = 0; i < tamanho; i++){        
        scanf("%d",&vetor[i]);
    }
    printf("Digite o k:");
    scanf("%d",&k);
    printf("Encontrado: %d \n",encontrado(vetor,tamanho,k));

    return 0;
}
