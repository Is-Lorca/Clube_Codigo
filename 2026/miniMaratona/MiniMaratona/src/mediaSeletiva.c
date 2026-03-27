#include <stdio.h>

int main(){
    int numero, contador = 0, soma = 0;

    for(int i = 0; i<8; i++){
        printf("Digite o numero: ");
        scanf("%d", &numero);
        if(numero%2 == 0){
            contador++;
            soma += numero;
        }
    }
    if(soma == 0){
        printf("SEM PARES");
    }
    else{
        int calculo = soma/contador;
        printf("A média dos números pares inseridos é: %d", calculo);
    }
}