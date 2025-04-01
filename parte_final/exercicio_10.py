import heapq

def arvores_minimas(grafo, inicio):
    visitados = set()
    arvore = []
    fila = [(0, inicio, None)]

    while fila:
        custo, atual, anterior = heapq.heappop(fila)
        if atual in visitados:
            continue
        visitados.add(atual)
        if anterior:
            arvore.append((anterior, atual, custo))
        for vizinho, peso in grafo[atual]:
            if vizinho not in visitados:
                heapq.heappush(fila, (peso, vizinho, atual))
    return arvore

rede = {
    'A': [('B', 5), ('C', 10)],
    'B': [('A', 5), ('C', 3), ('D', 8)],
    'C': [('A', 10), ('B', 3), ('D', 2), ('E', 7)],
    'D': [('B', 8), ('C', 2), ('E', 4), ('F', 6)],
    'E': [('C', 7), ('D', 4), ('F', 5)],
    'F': [('D', 6), ('E', 5)]
}

resultado = arvores_minimas(rede, 'A')
for u, v, custo in resultado:
    print(f"{u} - {v} (custo: {custo})")

