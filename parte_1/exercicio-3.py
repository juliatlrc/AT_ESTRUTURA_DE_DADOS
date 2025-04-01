import heapq
from typing import Set, List


class TrieNode:
    def __init__(self):
        self.filhos = {}
        self.fim = False


class Trie:
    def __init__(self):
        self.raiz = TrieNode()

    def inserir(self, palavra: str, palavras: Set[str]) -> None:
        no = self.raiz
        for letra in palavra:
            if letra not in no.filhos:
                no.filhos[letra] = TrieNode()
            no = no.filhos[letra]
        no.fim = True
        palavras.add(palavra)

    def autocompletar(self, prefixo: str) -> List[str]:
        no = self.raiz
        for letra in prefixo:
            if letra not in no.filhos:
                return []
            no = no.filhos[letra]
        return self._buscar(prefixo, no)

    def _buscar(self, prefixo: str, no: TrieNode) -> List[str]:
        palavras = []
        if no.fim:
            palavras.append(prefixo)
        for letra, filho in no.filhos.items():
            palavras.extend(self._buscar(prefixo + letra, filho))
        return palavras


def correção(palavra: str, palavras: Set[str], max_dist: int = 2) -> List[str]:
    similares = [
        (p, levenshtein(palavra, p))
        for p in palavras
        if levenshtein(palavra, p) <= max_dist
    ]
    similares.sort(key=lambda x: x[1])
    return [p[0] for p in similares]


def levenshtein(a: str, b: str) -> int:
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[-1][-1]


def main():
    trie = Trie()
    palavras = set()
    livros = [
        "it ends with us", "verity", "november 9", "ugly love", 
        "confess", "heart bones", "all your perfects", "reminders of him", 
        "sugar daddy", "the seven husbands of evelyn hugo", 
        "where the crawdads sing", "the night circus"
    ]
    
    for titulo in livros:
        trie.inserir(titulo.lower(), palavras)

    while True:
        entrada = input("Digite parte do título (ou 'sair'): ").lower()
        if entrada == "sair":
            break

        sugestoes = trie.autocompletar(entrada)
        correcao = correção(entrada, palavras)

        print("- Sugestões de Autocomplete:", sugestoes if sugestoes else "nenhuma")
        print("- Sugestões de Correção:", correcao if correcao else "nenhuma")
        print()


if __name__ == "__main__":
    main()

