INF = float('inf')
cidades = ['Centro', 'Avenida', 'Plaza', 'Lagoa', 'Mercado', 'Parque']
n = len(cidades)

distancia = [[INF] * n for _ in range(n)]
for i in range(n):
    distancia[i][i] = 0

conexoes = [
    ('Centro', 'Avenida', 5), ('Centro', 'Plaza', 10),
    ('Avenida', 'Plaza', 3), ('Avenida', 'Lagoa', 8),
    ('Plaza', 'Lagoa', 2), ('Plaza', 'Mercado', 7),
    ('Lagoa', 'Mercado', 4), ('Lagoa', 'Parque', 6),
    ('Mercado', 'Parque', 5)
]

for u, v, tempo in conexoes:
    i = cidades.index(u)
    j = cidades.index(v)
    distancia[i][j] = tempo

for k in range(n):
    for i in range(n):
        for j in range(n):
            if distancia[i][j] > distancia[i][k] + distancia[k][j]:
                distancia[i][j] = distancia[i][k] + distancia[k][j]

print("Menores tempos de viagem entre todos os pontos (em minutos):")
print("      " + "  ".join(cidades))
for i in range(n):
    linha = []
    for j in range(n):
        if distancia[i][j] == INF:
            linha.append(" ∞")
        else:
            linha.append(str(distancia[i][j]).rjust(2))
    print(cidades[i], " ".join(linha))

inicio_idx = cidades.index('Centro')
fim_idx = cidades.index('Parque')
print("\nTempo mínimo de Centro até Parque:", distancia[inicio_idx][fim_idx], "minutos")

