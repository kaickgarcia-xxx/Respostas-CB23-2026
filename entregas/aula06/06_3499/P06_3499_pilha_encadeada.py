class _No:
    """Classe auxiliar privada que representa um nó da lista encadeada."""
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo


class PilhaEncadeada:
    """
    Implementação de Pilha (TAD) sobre uma Lista Encadeada Simples.
    Mantedores: apenas a referência para o topo e o contador do tamanho.
    """
    def __init__(self):
        self._topo = None
        self._tamanho = 0

    def push(self, item) -> None:
        """Insere um item no topo da pilha.
        Complexidade: O(1)
        """
        novo_no = _No(item, self._topo)
        self._topo = novo_no
        self._tamanho += 1

    def pop(self):
        """Remove e retorna o item do topo da pilha.
        Complexidade: O(1)
        Raises: IndexError se a pilha estiver vazia.
        """
        if self.esta_vazia():
            raise IndexError("A pilha está vazia. Não é possível remover elementos.")
        
        valor = self._topo.valor
        self._topo = self._topo.proximo
        self._tamanho -= 1
        return valor

    def topo(self):
        """Retorna o item do topo sem removê-lo.
        Complexidade: O(1)
        Raises: IndexError se a pilha estiver vazia.
        """
        if self.esta_vazia():
            raise IndexError("A pilha está vazia. Não há elemento no topo.")
        return self._topo.valor

    def esta_vazia(self) -> bool:
        """Retorna True se a pilha estiver vazia.
        Complexidade: O(1)
        """
        return self._tamanho == 0

    def __len__(self) -> int:
        """Retorna a quantidade de elementos armazenados.
        Complexidade: O(1)
        """
        return self._tamanho

    def __repr__(self) -> str:
        """Representação textual do topo para a base.
        Complexidade: O(N)
        """
        elementos = []
        atual = self._topo
        while atual is not None:
            elementos.append(repr(atual.valor))
            atual = atual.proximo
        return f"PilhaEncadeada([{', '.join(elementos)}])"
