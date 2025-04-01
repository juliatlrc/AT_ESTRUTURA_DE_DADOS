import time

movimentos = [(-2, -1), (-1, -2), (1, -2), (2, -1),
              (2, 1), (1, 2), (-1, 2), (-2, 1)]

def dentro(x, y, N):
    return 0 <= x < N and 0 <= y < N

def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(f"{c:2}" for c in linha))
    print()

def percurso_cavaleiro_bruto(N):
    tabuleiro = [[-1 for _ in range(N)] for _ in range(N)]
    tabuleiro[0][0] = 0
    if resolver_bruto(tabuleiro, 0, 0, 1, N):
        mostrar_tabuleiro(tabuleiro)

def resolver_bruto(tab, x, y, passo, N):
    if passo == N * N:
        return True
    for dx, dy in movimentos:
        nx, ny = x + dx, y + dy
        if dentro(nx, ny, N) and tab[nx][ny] == -1:
            tab[nx][ny] = passo
            if resolver_bruto(tab, nx, ny, passo + 1, N):
                return True
            tab[nx][ny] = -1
    return False

def percurso_cavaleiro_heuristica(N):
    tab = [[-1 for _ in range(N)] for _ in range(N)]
    tab[0][0] = 0
    if resolver_heuristica(tab, 0, 0, 1, N):
        mostrar_tabuleiro(tab)

def grau(tab, x, y, N):
    count = 0
    for dx, dy in movimentos:
        nx, ny = x + dx, y + dy
        if dentro(nx, ny, N) and tab[nx][ny] == -1:
            count += 1
    return count

def resolver_heuristica(tab, x, y, passo, N):
    if passo == N * N:
        return True
    candidatos = []
    for dx, dy in movimentos:
        nx, ny = x + dx, y + dy
        if dentro(nx, ny, N) and tab[nx][ny] == -1:
            candidatos.append((grau(tab, nx, ny, N), nx, ny))
    candidatos.sort()
    for _, nx, ny in candidatos:
        tab[nx][ny] = passo
        if resolver_heuristica(tab, nx, ny, passo + 1, N):
            return True
        tab[nx][ny] = -1
    return False

print("Força bruta (5x5):")
start = time.time()
percurso_cavaleiro_bruto(5)
print("Tempo:", round(time.time() - start, 4), "s")

print("Heurística (8x8):")
start = time.time()
percurso_cavaleiro_heuristica(8)
print("Tempo:", round(time.time() - start, 4), "s")

