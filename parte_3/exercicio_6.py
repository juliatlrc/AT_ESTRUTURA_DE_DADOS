import heapq

mapa_cidades = {
    'Centro': [('A', 4), ('B', 2)],
    'A': [('Centro', 5), ('D', 10)],
    'B': [('A', 3), ('D', 8)],
    'C': [('D', 2), ('E', 4)],
    'D': [('E', 6), ('F', 5)],
    'E': [('F', 3)],
    'F': []
}

def calcular_distancias(mapa, origem):
    distancias = {local: float('inf') for local in mapa}
    predecessores = {local: None for local in mapa}
    distancias[origem] = 0
    fila_prioridade = [(0, origem)]

    while fila_prioridade:
        distancia_atual, local_atual = heapq.heappop(fila_prioridade)
        for vizinho, peso in mapa[local_atual]:
            nova_distancia = distancia_atual + peso
            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                predecessores[vizinho] = local_atual
                heapq.heappush(fila_prioridade, (nova_distancia, vizinho))

    return distancias, predecessores

def recuperar_caminho(predecessores, destino):
    caminho = []
    while destino:
        caminho.insert(0, destino)
        destino = predecessores[destino]
    return caminho

distancias, predecessores = calcular_distancias(mapa_cidades, 'Centro')
caminho = recuperar_caminho(predecessores, 'F')
print("Caminho mais rápido de Centro até F:", " -> ".join(caminho))
print("Distância total percorrida:", distancias['F'], "km")

