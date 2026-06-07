import math

# Coordenadas das palavras no espaço semântico (X, Y)
palavras = {
    "Verão": (8, 7),
    "Sol":   (9, 8),
    "Gelo":  (2, 1)
}

def distancia_euclidiana(p1, p2):
    """Calcula a distância entre dois pontos (X, Y)"""
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Palavra de referência
referencia = "Verão"
candidatas = ["Sol", "Gelo"]

print("=== RADAR DE SEMELHANÇA ===\n")
print(f"Palavra de referência: {referencia} {palavras[referencia]}\n")

distancias = {}
for palavra in candidatas:
    d = distancia_euclidiana(palavras[referencia], palavras[palavra])
    distancias[palavra] = d
    print(f"Distância de '{referencia}' até '{palavra}' {palavras[palavra]}: {d:.4f}")

# Identificar a mais próxima
mais_proxima = min(distancias, key=distancias.get)

print(f"\n✅ Resultado: '{mais_proxima}' está semanticamente mais próxima de '{referencia}'")