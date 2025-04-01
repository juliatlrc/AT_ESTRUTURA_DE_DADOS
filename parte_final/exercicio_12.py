import itertools
import random
import time
from functools import lru_cache

localidades = ['A', 'B', 'C', 'D', 'E']
distancia_entre = {
    ('A', 'B'): 5, ('A', 'C'): 10, ('A', 'D'): 8, ('A', 'E'): 9,
    ('B', 'C'): 3, ('B', 'D'): 7, ('B', 'E'): 4,
    ('C', 'D'): 2, ('C', 'E'): 6,
    ('D', 'E'): 5
}
for (a, b), v in list(distancia_entre.items()):
    distancia_entre[(b, a)] = v

def calcular_custo(rota):
    total = 0
    for i in range(len(rota) - 1):
        total += distancia_entre[(rota[i], rota[i+1])]
    total += distancia_entre[(rota[-1], rota[0])]
    return total

def tsp_held_karp():
    n = len(localidades)
    indices = {c: i for i, c in enumerate(localidades)}

    @lru_cache(None)
    def dp(mask, pos):
        if mask == (1 << n) - 1:
            return distancia_entre[(localidades[pos], localidades[0])]
        res = float('inf')
        for nxt in range(n):
            if mask & (1 << nxt) == 0:
                res = min(res, distancia_entre[(localidades[pos], localidades[nxt])] + dp(mask | (1 << nxt), nxt))
        return res

    mask = 1
    pos = 0
    rota = [localidades[0]]
    while mask != (1 << n) - 1:
        nxt = min(
            (distancia_entre[(localidades[pos], localidades[i])] + dp(mask | (1 << i), i), i)
            for i in range(n) if mask & (1 << i) == 0
        )[1]
        rota.append(localidades[nxt])
        mask |= (1 << nxt)
        pos = nxt
    return rota, dp(1, 0)

def tsp_algoritmo_genetico(tamanho_populacao=100, geracoes=500, taxa_mutacao=0.1):
    def gerar_populacao():
        return [random.sample(localidades, len(localidades)) for _ in range(tamanho_populacao)]

    def aptidao(rota):
        return 1 / calcular_custo(rota)

    def cruzamento(pai1, pai2):
        ponto_corte = random.randint(1, len(localidades) - 2)
        filho = pai1[:ponto_corte] + [c for c in pai2 if c not in pai1[:ponto_corte]]
        return filho

    def mutacao(rota):
        if random.random() < taxa_mutacao:
            i, j = random.sample(range(len(rota)), 2)
            rota[i], rota[j] = rota[j], rota[i]

    populacao = gerar_populacao()
    for _ in range(geracoes):
        populacao = sorted(populacao, key=aptidao, reverse=True)
        nova_populacao = populacao[:tamanho_populacao // 2]
        while len(nova_populacao) < tamanho_populacao:
            pai1, pai2 = random.sample(populacao[:tamanho_populacao // 2], 2)
            filho = cruzamento(pai1, pai2)
            mutacao(filho)
            nova_populacao.append(filho)
        populacao = nova_populacao

    melhor_rota = max(populacao, key=aptidao)
    return melhor_rota, calcular_custo(melhor_rota)

print("Método Held-Karp (Programação Dinâmica):")
inicio = time.time()
rota, custo = tsp_held_karp()
print(" -> ".join(rota), f"(custo: {custo})")
print("Tempo:", round(time.time() - inicio, 4), "s")

print("\nUtilizando Algoritmo Genético:")
inicio = time.time()
rota, custo = tsp_algoritmo_genetico()
print(" -> ".join(rota), f"(custo: {custo})")
print("Tempo:", round(time.time() - inicio, 4), "s")

