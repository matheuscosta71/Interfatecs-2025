n = int(input())
saldo = 0
min_saldo = 0

for _ in range(n):
    t = int(input())
    saldo += t
    if saldo < min_saldo:
        min_saldo = saldo

print(-min_saldo)