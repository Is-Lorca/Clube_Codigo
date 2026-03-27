#include <stdio.h>

int main(){
    int numero, soma = 0;

    do{
        printf("Digite os numeros a serem somados: ");
        scanf("%d", &numero);
        soma += numero;
    }while(numero != 0);

    printf("A soma é: %d", soma);
}
