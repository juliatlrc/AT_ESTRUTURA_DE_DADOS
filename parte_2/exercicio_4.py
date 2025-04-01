cidade_grafo = {
    'Centro': [('Jardim', 4), ('Parque', 2)],
    'Jardim': [('Centro', 4), ('Praia', 5)],
    'Parque': [('Centro', 2), ('Praia', 8), ('Shopping', 3)],
    'Praia': [('Jardim', 5), ('Parque', 8), ('Hospital', 6)],
    'Shopping': [('Parque', 3), ('Hospital', 1)],
    'Hospital': [('Praia', 6), ('Shopping', 1)],
}

# Exibindo a Lista de Adjacência
print("Lista de Conexões entre os Bairros:")
for bairro, vizinhos in cidade_grafo.items():
    conexoes = " -> ".join([f"{destino} ({distancia} km)" for destino, distancia in vizinhos])
    print(f"{bairro} -> {conexoes}")

# Exibindo a Matriz de Adjacência
print("\nMatriz de Conexões entre os Bairros:")
bairros = ['Centro', 'Jardim', 'Parque', 'Praia', 'Shopping', 'Hospital']
num_bairros = len(bairros)

# Inicializando a matriz com valores zero
matriz_conexoes = [[0] * num_bairros for _ in range(num_bairros)]

# Preenchendo a matriz com as distâncias
for origem in cidade_grafo:
    for destino, distancia in cidade_grafo[origem]:
        i = bairros.index(origem)
        j = bairros.index(destino)
        matriz_conexoes[i][j] = distancia

# Exibindo a matriz de adjacência
print("   ", "  ".join(bairros))
for i in range(num_bairros):
    linha = "  ".join(str(matriz_conexoes[i][j]).rjust(2) for j in range(num_bairros))
    print(bairros[i], linha)

# Exibindo o Grafo como uma Matriz
print("\nRepresentação Matricial do Grafo:")
for i in range(num_bairros):
    origem = bairros[i]
    print(f"{origem}")
    for j in range(num_bairros):
        if matriz_conexoes[i][j] != 0:
            destino = bairros[j]
            print(f"  -> {destino} ({matriz_conexoes[i][j]} km)")

