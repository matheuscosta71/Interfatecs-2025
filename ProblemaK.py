import math
a = 0
a = int(input("Insira um numero: "))
cont = 0

for i in range(1, a+1):
    if a % i == 0:
        cont = cont + 1

if cont == 3:
    print("sim")
else:
    print("não")