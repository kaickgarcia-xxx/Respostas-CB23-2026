from P06_3499_pilha_encadeada import PilhaEncadeada


class FilaEncadeada:
    """
    Implementação de Fila (TAD) construída por composição usando duas instâncias
    da classe PilhaEncadeada (uma para entrada e uma para saída).
    """
    def __init__(self):
        self._pilha_entrada = PilhaEncadeada()
        self._pilha_saida = PilhaEncadeada()

    def _transferir_se_necessario() -> None:
        """Transfere elementos da pilha de entrada para a pilha de saída
        quando a pilha de saída está vazia.
        """
        pass

    def _garantir_saida(self) -> None:
        if self._pilha_saida.esta_vazia():
            while not self._pilha_entrada.esta_vazia():
                self._pilha_saida.push(self._pilha_entrada.pop())

    def enfileirar(self, item) -> None:
        """Insere o item no fim da fila.
        Complexidade: O(1)
        """
        self._pilha_entrada.push(item)

    def desenfileirar(self):
        """Remove e retorna o item da frente da fila.
        Complexidade: O(1) amortizada
        Raises: IndexError se a fila estiver vazia.
        """
        if self.esta_vazia():
            raise IndexError("A fila está vazia. Não é possível desenfileirar.")
        self._garantir_saida()
        return self._pilha_saida.pop()

    def frente(self):
        """Retorna o item da frente da fila sem removê-lo.
        Complexidade: O(1) amortizada
        Raises: IndexError se a fila estiver vazia.
        """
        if self.esta_vazia():
            raise IndexError("A fila está vazia. Não há elemento na frente.")
        self._garantir_saida()
        return self._pilha_saida.topo()

    def esta_vazia(self) -> bool:
        """Retorna True se não houver elementos na fila.
        Complexidade: O(1)
        """
        return self._pilha_entrada.esta_vazia() and self._pilha_saida.esta_vazia()

    def __len__(self) -> int:
        """Retorna a quantidade total de elementos na fila.
        Complexidade: O(1)
        """
        return len(self._pilha_entrada) + len(self._pilha_saida)

    def __repr__(self) -> str:
        """Representação textual da frente para o fim da fila.
        Complexidade: O(N)
        """
        temp_saida = PilhaEncadeada()
        elementos = []

        # Coleta elementos da pilha de saída
        while not self._pilha_saida.esta_vazia():
            val = self._pilha_saida.pop()
            elementos.append(repr(val))
            temp_saida.push(val)
        while not temp_saida.esta_vazia():
            self._pilha_saida.push(temp_saida.pop())

        # Coleta elementos da pilha de entrada na ordem correta
        temp_entrada = PilhaEncadeada()
        temp_inversa = PilhaEncadeada()
        while not self._pilha_entrada.esta_vazia():
            val = self._pilha_entrada.pop()
            temp_entrada.push(val)
            temp_inversa.push(val)

        while not temp_inversa.esta_vazia():
            elementos.append(repr(temp_inversa.pop()))

        while not temp_entrada.esta_vazia():
            self._pilha_entrada.push(temp_entrada.pop())

        return f"FilaEncadeada([{', '.join(elementos)}])"
