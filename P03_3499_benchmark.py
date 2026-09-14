import random
import time

try:
    import AP_03_ordenacao as ordenacao
except ImportError:
    import ap_03_ordenacao as ordenacao

TAMANHOS_N = [100, 500, 1000, 5000]
REPETICOES_K = 10

def gerar_caso_medio(n):
    return [random.randint(0, 100000) for _ in range(n)]

def gerar_pior_caso(n):
    return list(range(n, 0, -1))

def medir_tempo_medio(funcao_ordenacao, dados_originais, k):
    tempo_total = 0.0
    for _ in range(k):
        dados = dados_originais.copy()
        inicio = time.perf_counter()
        funcao_ordenacao(dados)
        fim = time.perf_counter()
        tempo_total += (fim - inicio)
    return tempo_total / k

def executar_benchmark():
    algoritmos = [
        (nome, getattr(ordenacao, nome))
        for nome in dir(ordenacao)
        if callable(getattr(ordenacao, nome)) and not nome.startswith("__")
    ]

    print(f"\n{'ALGORITMO':<20} | {'N':<6} | {'CENÁRIO':<12} | {'TEMPO MÉDIO (s)':<15}")
    print("-" * 62)

    for nome_alg, func in algoritmos:
        for n in TAMANHOS_N:
            for cenario_nome, funcao_geradora in [("Caso Médio", gerar_caso_medio), ("Pior Caso", gerar_pior_caso)]:
                dados = funcao_geradora(n)
                tempo_medio = medir_tempo_medio(func, dados, REPETICOES_K)
                print(f"{nome_alg:<20} | {n:<6} | {cenario_nome:<12} | {tempo_medio:.6f}")

if __name__ == "__main__":
    executar_benchmark()
