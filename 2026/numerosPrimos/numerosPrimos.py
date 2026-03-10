import numpy as np

def crivoEratostenes(limite):
    #cria uma array que assume que todos os numeros são primos, no inicio
    numerosPrimos = [True] * (limite + 1) 

    """por numero no range de 2 a 10, no caso fazemos a raiz quadrada de 100 (limite ** 0.5) + 1, 
    pois é excluido o último valor (basicamente range(2, 11)).
    Não precismos checar até o 100, pois a partir do 10, o que restar serão primos
    o 0 e o 1 não são primos, entao nem contaremos com eles"""
    for i in range(2, int(limite ** 0.5) + 1):
        #se o numeroPrimo na posição de i for True...
        if numerosPrimos[i]:
            #será checado o múltiplo, agora no range de i*i, ex. 2*2, limite + 1 = 101, ao passo do i
            for multiplo in range(i * i, limite + 1, i):
                #se o número for multiplo, ele não será primo, logo, False
                numerosPrimos[multiplo] = False

    #de numero em numero no range de (2, 101), se o numeroPrimos[numero] for True, ele é realmente um número primo
    primos = [numero for numero in range(2, limite+1) if numerosPrimos[numero]]

    #retorna a array
    return primos

def somaPrimos(arrayNumerosPrimos):
    ultimoValor = arrayNumerosPrimos[len(arrayNumerosPrimos)-1]
    soma = arrayNumerosPrimos[0] + ultimoValor

    return soma

def main():
    #função armazenando o limite, sendo 100
    limite = int(input("Insira o número: "))
    numerosPrimos = crivoEratostenes(limite)
    soma = somaPrimos(numerosPrimos)

    print(numerosPrimos)
    print("Soma do primeiro e último números primos do limite inserido: ", soma)

main()