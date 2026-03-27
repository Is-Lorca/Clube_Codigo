#include <stdio.h>

int main(){
    int numero, maior = 0, contador = 0;

    while(numero != -1){
        if(contador == 1){
            maior = numero;
        }
        else if(numero>maior){
            maior = numero;
        }
        printf("Digite os numeros: ");
        scanf("%d", &numero);
        contador++;
    }

    printf("O maior número foi: %d", maior);
}
