def somaNumeros(numInteressantePri, numInteressanteUlt):
    soma = numInteressantePri + numInteressanteUlt
    return soma

def numerosInteressantes(inicio, fim):
    contador = 0

    for numero in range(inicio, fim+1):
        if(numero % 2 != 0):
            if(numero % 3 == 0 or numero % 5 == 0):
                contador += 1

                if(contador == 1):
                    numInteressantePri = numero
                    numInteressanteUlt = 0
                if(contador != 1):
                    numInteressanteUlt = numero
                
    soma = somaNumeros(numInteressantePri, numInteressanteUlt)

    print(f"Do número {inicio} ao número {fim} temos um total de {contador} números interessantes")
    print(f"O primeiro número interessante é: {numInteressantePri} e o último: {numInteressanteUlt}")
    if (numInteressanteUlt != 0):
        print(f"A soma do primeiro e do último número interessante é: {soma}")
    else:
        print("Não há com o que somar o primeiro número.")

def main():
    inicio, fim = map(int, input("Insira dois valores: ").split())

    if(inicio>fim):
        temp = inicio
        inicio = fim
        fim = temp

    numerosInteressantes(inicio, fim)

main()