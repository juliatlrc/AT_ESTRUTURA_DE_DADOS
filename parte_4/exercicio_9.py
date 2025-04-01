armazens = {
    "A1": {"L1", "L2", "L3"},
    "A2": {"L3", "L4"},
    "A3": {"L4", "L5"},
    "A4": {"L5", "L6"},
    "A5": {"L2", "L6"},
}

lojas = {"L1", "L2", "L3", "L4", "L5", "L6"}
cobertos = set()
selecionados = []

while cobertos != lojas:
    melhor = None
    cobertos_agora = set()
    for nome, cobre in armazens.items():
        nova_cobertura = cobre - cobertos
        if len(nova_cobertura) > len(cobertos_agora):
            melhor = nome
            cobertos_agora = nova_cobertura
    selecionados.append(melhor)
    cobertos.update(armazens[melhor])

print("Armazéns selecionados:", selecionados)
