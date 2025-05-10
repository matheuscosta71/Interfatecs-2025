import math

numero = int(input())

for i in range (numero):
    entrada = input().strip()
    temperatura, umidade, chuva = map(float, entrada.split())
    
    if temperatura > 30 and umidade < 50:
        if chuva==0: 
            print ("REGAR")
        else:
            print ("NAO REGAR")
    else :
        print("NAO REGAR")
    
