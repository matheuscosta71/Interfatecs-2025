temp_gast = int(input())
vale = int(input())
colina = int(input())
mont = int(input())


def tempo_total(T, V, C, M):
    tempo_nivel_1 = V * 0 + C * 2 * T + M * 4 * T
    tempo_nivel_2 = V * 2 * T + C * 0 + M * 2 * T
    tempo_nivel_3 = V * 4 * T + C * 2 * T + M * 0
    return min(tempo_nivel_1, tempo_nivel_2, tempo_nivel_3)

print(tempo_total(temp_gast, vale, colina, mont))