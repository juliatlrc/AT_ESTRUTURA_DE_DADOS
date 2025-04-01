import heapq
from typing import List, Optional, Dict


class Pacote:
    def __init__(self, id: int, prioridade: int, tempo_transmissao: int):
        self.id = id
        self.prioridade = prioridade
        self.tempo_transmissao = tempo_transmissao

    def __lt__(self, other: 'Pacote') -> bool:
        return self.prioridade < other.prioridade


class HeapMinimo:
    def __init__(self):
        self.heap: List[Pacote] = []

    def inserir(self, pacote: Pacote) -> None:
        heapq.heappush(self.heap, pacote)

    def remover(self) -> Optional[Pacote]:
        if self.heap:
            return heapq.heappop(self.heap)
        return None

    def atualizar_prioridade(self, id_pacote: int, nova_prioridade: int) -> None:
        for i, pacote in enumerate(self.heap):
            if pacote.id == id_pacote:
                self.heap[i].prioridade = nova_prioridade
                heapq.heapify(self.heap)
                break


def criar_pacote(id: int, prioridade: int, tempo_transmissao: int) -> Pacote:
    return Pacote(id, prioridade, tempo_transmissao)


heap = HeapMinimo()
heap.inserir(criar_pacote(101, 5, 10))
heap.inserir(criar_pacote(102, 1, 8))
heap.inserir(criar_pacote(103, 3, 6))

p = heap.remover()
print(p.id, p.prioridade, p.tempo_transmissao)

heap.atualizar_prioridade(103, 0)
p = heap.remover()
print(p.id, p.prioridade, p.tempo_transmissao)

