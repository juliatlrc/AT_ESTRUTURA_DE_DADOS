import heapq
from typing import List, Optional


class Processo:
    def __init__(self, id: int, tempo_execucao: int, prioridade: int):
        self.id = id
        self.tempo_execucao = tempo_execucao
        self.prioridade = prioridade

    def __repr__(self):
        return f"Processo(id={self.id}, tempo_execucao={self.tempo_execucao}, prioridade={self.prioridade})"


class Escalonador:
    def __init__(self):
        self.fila: List[tuple[int, Processo]] = []

    def adicionar_processo(self, processo: Processo) -> None:
        heapq.heappush(self.fila, (processo.prioridade, processo))

    def executar_proximo(self) -> Optional[Processo]:
        if self.fila:
            return heapq.heappop(self.fila)[1]
        return None

    def modificar_prioridade(self, id_processo: int, nova_prioridade: int) -> None:
        for i in range(len(self.fila)):
            if self.fila[i][1].id == id_processo:
                self.fila[i] = (nova_prioridade, self.fila[i][1])
                self.fila[i][1].prioridade = nova_prioridade
                heapq.heapify(self.fila)
                break


escalonador = Escalonador()
escalonador.adicionar_processo(Processo(1, 5, 3))
escalonador.adicionar_processo(Processo(2, 3, 1))
escalonador.adicionar_processo(Processo(3, 2, 2))

p = escalonador.executar_proximo()
print(p.id, p.tempo_execucao, p.prioridade)

escalonador.modificar_prioridade(3, 0)
p = escalonador.executar_proximo()
print(p.id, p.tempo_execucao, p.prioridade)

