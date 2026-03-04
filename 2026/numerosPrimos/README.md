# 1️⃣ Descobrindo Números Primos
### Desafio: Descubra os números primos de 0 a 100.
---
## 🧠 Como solucionei:
Utilizei do Crivo de Eratóstenes para solucionar o problema.

#### Crivo de Eratóstenes:
Ao invés de testar cada número individualmente para saber se ele é primo (verificando divisibilidade), o crivo funciona eliminando sistematicamente os múltiplos dos números primos.

A lógica é:
* Comece assumindo que todos os números são primos.
* Escolha o primeiro número primo (2).
* Elimine todos os múltiplos dele.
* Vá para o próximo número que ainda não foi eliminado.
* Repita o processo.
* Os números que restarem são primos.

---
Exemplo: Queremos os números primos de 0 a 30.

0 e 1 já não são primos, podemos descartar.

1. Começamos listando os números de 2 até 30.
    * Inicialmente, todos são considerados primos.

2. Começamos pelo número 2
    * 2 é primo. Eliminamos seus múltiplos: 4, 6, 8, 10, 12...

3. Próximo número não eliminado: 3
    * 3 é primo. Eliminamos seus múltiplos: 6, 9, 12, 15...

    (Alguns já tinham sido eliminados pelo 2.)

4. Próximo número não eliminado: 5
    * Eliminamos: 10, 15, 20...

5. Continuamos o processo

Paramos quando o número atual for maior que a raiz quadrada do limite.

No caso de 30: **√30 ≈ 5,47**

Ou seja, só precisamos processar até o **5**.

Depois disso, todos os números restantes são primos automaticamente.

---

#### Porque paramos na raiz quadrada:
Se um número n é composto, ele pode ser escrito como:
                       
                         n = a × b

Se ambos a e b fossem maiores que √n, então:

a × b seria maior que n

O que é impossível.

Portanto:

👉 Todo número composto possui pelo menos um divisor menor ou igual à sua raiz quadrada.

Isso torna o algoritmo muito mais eficiente, sem a necessidade de chegar até o final da amostra.

---

## Linguagens disponíveis:
**Python**: [numerosPrimos.py](numerosPrimos.py)

**Java**: [numerosPrimos.jav](numerosPrimos.jav)

**C**: [numerosPrimos.c](numerosPrimos.c)