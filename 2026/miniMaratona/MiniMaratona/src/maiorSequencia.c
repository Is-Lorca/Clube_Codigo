#include <stdio.h>

int main(){
    int usuario, maior = 0, contador = 0;

    while(usuario != -1){
        if(contador == 1){
            maior = usuario;
        }
        else if(usuario>maior){
            maior = usuario;
        }
        
        printf("Digite os numeros: ");
        scanf("%d", &usuario);
        contador++;
        if(usuario%2 == 0){
            printf("Par");
        }
    }

    printf("O maior número foi: %d", maior);
}
