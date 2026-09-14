# Discussão Teórica - Aula 07 (Grafos e Labirintos)

## Algoritmo Utilizado na Resolução do Caminho
Para encontrar o caminho entre a posição inicial `(1, 1)` e a posição do queijo (`Q`), foi utilizada a **Busca em Largura (BFS - Breadth-First Search)**.

---

## Justificativa da Escolha da Busca em Largura (BFS)

1. **Garantia de Menor Caminho**: O labirinto é um grafo não ponderado (todas as arestas têm peso igual a 1). A Busca em Largura expande a busca em "camadas" ou níveis de distância uniformes a partir do ponto de origem, garantindo matematicamente a descoberta do **menor caminho em número de passos**.
2. **Comparação com a Busca em Profundidade (DFS)**:
   * A **DFS** segue por um único ramo até atingir um beco sem saída antes de retroceder (*backtracking*). Em um labirinto com múltiplos caminhos, a DFS pode facilmente encontrar um caminho válido, porém **muito mais longo e ineficiente** em comparação ao caminho ótimo.
   * A **BFS** utiliza uma fila (FIFO) para explorar todas as alternativas a uma distância $d$ antes de avançar para a distância $d+1$, tornando-a ideal para otimização de rota.
