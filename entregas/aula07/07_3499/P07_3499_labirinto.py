import random
from collections import deque


def gerar_labirinto_dfs_iterativo(largura=21, altura=21):
    """Gera um labirinto usando Busca em Profundidade (DFS) Iterativa.
    Questão 1.
    """
    largura = largura if largura % 2 != 0 else largura + 1
    altura = altura if altura % 2 != 0 else altura + 1

    grid = [["#" for _ in range(largura)] for _ in range(altura)]

    pilha = [(1, 1)]
    grid[1][1] = " "

    movimentos = [(-2, 0), (2, 0), (0, -2), (0, 2)]

    while pilha:
        r, c = pilha[-1]
        vizinhos = []

        for dr, dc in movimentos:
            nr, nc = r + dr, c + dc
            if 0 < nr < altura - 1 and 0 < nc < largura - 1:
                if grid[nr][nc] == "#":
                    vizinhos.append((nr, nc, dr, dc))

        if vizinhos:
            nr, nc, dr, dc = random.choice(vizinhos)
            grid[r + dr // 2][c + dc // 2] = " "
            grid[nr][nc] = " "
            pilha.append((nr, nc))
        else:
            pilha.pop()

    grid[altura - 2][largura - 2] = "Q"
    return grid


def encontrar_caminho_bfs(grid, inicio=(1, 1)):
    """Encontra o menor caminho do início até o Queijo ('Q') usando BFS.
    Questão 2.
    """
    altura = len(grid)
    largura = len(grid[0])

    fila = deque([inicio])
    visitados = {inicio}
    veio_de = {}

    destino = None
    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while fila:
        atual = fila.popleft()
        r, c = atual

        if grid[r][c] == "Q":
            destino = atual
            break

        for dr, dc in movimentos:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < altura
                and 0 <= nc < largura
                and grid[nr][nc] != "#"
                and (nr, nc) not in visitados
            ):
                visitados.add((nr, nc))
                veio_de[(nr, nc)] = atual
                fila.append((nr, nc))

    if not destino:
        return []

    caminho = []
    passo = destino
    while passo != inicio:
        caminho.append(passo)
        passo = veio_de[passo]
    caminho.append(inicio)
    caminho.reverse()

    return caminho


def exibir_labirinto(grid, caminho=None):
    """Exibe no terminal o labirinto com o caminho percorrido."""
    if caminho is None:
        caminho = []

    caminho_set = set(caminho)

    for r, linha in enumerate(grid):
        linha_repr = []
        for c, val in enumerate(linha):
            if (r, c) == (1, 1):
                linha_repr.append("I")
            elif val == "Q":
                linha_repr.append("Q")
            elif (r, c) in caminho_set:
                linha_repr.append(".")
            elif val == "#":
                linha_repr.append("█")
            else:
                linha_repr.append(" ")
        print(" ".join(linha_repr))


if __name__ == "__main__":
    labirinto = gerar_labirinto_dfs_iterativo(19, 19)
    caminho = encontrar_caminho_bfs(labirinto)

    print("=== LABIRINTO SOLUCIONADO ===")
    exibir_labirinto(labirinto, caminho)
    print(f"\nTamanho do caminho encontrado: {len(caminho)} passos.")
