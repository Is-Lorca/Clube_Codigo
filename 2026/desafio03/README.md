# 🔢 Números Interessantes

Neste desafio escrevi um algoritmos que encontram os chamados **números interessantes** dentro de um intervalo informado pelo usuário.

## 📌 O que são números interessantes?

Um número é considerado **interessante** quando:

* É **ímpar**
* É **múltiplo de 3 ou de 5**

O algoritmo:

* Percorre um intervalo definido pelo usuário
* Conta quantos números interessantes existem
* Identifica o **primeiro** e o **último** número interessante
* Calcula a **soma entre o primeiro e o último**
* Exibe os resultados no terminal

---

## 🧠 Lógica do Algoritmo

1. O usuário informa dois valores (início e fim)
2. O algoritmo percorre todos os números do intervalo
3. Para cada número:

   * Verifica se é ímpar
   * Verifica se é múltiplo de 3 ou 5
4. Se for interessante:

   * Incrementa o contador
   * Armazena o primeiro e o último número encontrado
5. Ao final:

   * Soma o primeiro e o último número interessante
   * Exibe os resultados

---

## 📊 Exemplo de saída

```
Do número 1 ao número 15 temos um total de 4 números interessantes
O primeiro número interessante é: 3 e o último: 15
A soma dos números interessantes é: 18
```
