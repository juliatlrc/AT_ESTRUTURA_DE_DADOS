from collections import deque

rede_metro = {
    'Estação1': ['Estação2', 'Estação3'],
    'Estação2': ['Estação1', 'Estação4', 'Estação5'],
    'Estação3': ['Estação1', 'Estação6'],
    'Estação4': ['Estação2', 'Estação5'],
    'Estação5': ['Estação2', 'Estação4', 'Estação6'],
    'Estação6': ['Estação3', 'Estação5']
}

def busca_largura(grafo, inicio):
    explorados = set()
    fila = deque([inicio])

    while fila:
        atual = fila.popleft()
        if atual not in explorados:
            print(f"Visitando: {atual}", end=' ')
            explorados.add(atual)
            for vizinho in grafo[atual]:
                if vizinho not in explorados:
                    fila.append(vizinho)

print("\nBusca em Largura (BFS) a partir da Estação1:")
busca_largura(rede_metro, 'Estação1')

def busca_profundidade(grafo, inicio, explorados=None):
    if explorados is None:
        explorados = set()
    explorados.add(inicio)
    print(f"Visitando: {inicio}", end=' ')
    for vizinho in grafo[inicio]:
        if vizinho not in explorados:
            busca_profundidade(grafo, vizinho, explorados)

print("\nBusca em Profundidade (DFS) a partir da Estação1:")
busca_profundidade(rede_metro, 'Estação1')

print("\nRepresentação do Metrô como Lista de Conexões:")
for estacao, vizinhos in rede_metro.items():
    conexoes = " -> ".join(vizinhos)
    print(f"{estacao} conecta-se a: {conexoes}")

print("\nGrafo como Lista de Adjacências:")
for origem in rede_metro:
    print(f"\nOrigem: {origem}")
    for destino in rede_metro[origem]:
        print(f"  -> Destino: {destino}")

