# Análise de Complexidade - Aula 06 (Pilha e Fila Encadeadas)

## Análise da Complexidade Amortizada da Operação `desenfileirar()`

### 1. Por que `desenfileirar()` pode custar $O(N)$ em uma chamada isolada?
Quando a fila possui $N$ elementos acumulados na `_pilha_entrada` e a `_pilha_saida` está totalmente vazia, a chamada do método `desenfileirar()` necessita transferir todos os $N$ elementos de uma pilha para a outra. 

Nessa chamada específica, ocorrem $N$ operações de `pop()` e $N$ operações de `push()`. Como cada uma dessas operações em uma pilha encadeada possui custo $O(1)$, o custo total dessa chamada isolada é proporcional a $N$, ou seja, $O(N)$.

---

### 2. Por que o custo amortizado é $O(1)$?
Apesar de uma transferência pontual custar $O(N)$, essa operação acontece com pouca frequência. Analisando o ciclo de vida completo de cada elemento inserido na fila, ele passa rigorosamente por **4 operações básicas**:

1. **1 inserção (`push`)** na `_pilha_entrada` no momento em que é enfileirado — $O(1)$
2. **1 remoção (`pop`)** da `_pilha_entrada` durante a transferência — $O(1)$
3. **1 inserção (`push`)** na `_pilha_saida` durante a transferência — $O(1)$
4. **1 remoção (`pop`)** da `_pilha_saida` no momento em que é desenfileirado — $O(1)$

Como **cada elemento é manipulado exatamente 4 vezes com custo $O(1)$ cada**, o custo total para processar $N$ elementos ao longo de toda a execução é $4N \times O(1) = O(N)$.

Dividindo o custo total acumulado pelo número de operações $N$:
$$\text{Custo Amortizado por Operação} = \frac{O(N)}{N} = O(1)$$

Portanto, garantimos que a complexidade amortizada de `desenfileirar()` é **$O(1)$**.
