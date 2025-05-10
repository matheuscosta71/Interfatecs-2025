def base20(simbolo):
    if simbolo == '*':
        return 0
    return simbolo.count('.') * 1 + simbolo.count('-') * 5

def mudar_decimal(linhas):
    resultados = []
    for linha in linhas:
        if linha.strip() == '*':
            resultados.append(0)
            break
        simbolos = linha.strip().split()
        simbolos.reverse()
        total = 0
        for i, simbolo in enumerate(simbolos):
            total += base20(simbolo) * (20 ** i)
        resultados.append(total)
    return resultados

linhas = []

while True:
        entrada = input()
        linhas.append(entrada)
        if entrada.strip() == '*':
            break

for resultado in mudar_decimal(linhas):
    print(resultado)