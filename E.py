import math

while True:
    entrada = input().strip()
    a, b, teta = map(float, entrada.split())

    if a == 0 and b == 0 and teta == 0:
        break

    theta_rad = math.radians(teta)    

    area = 0.5 * a * b * math.sin(theta_rad)

    print(f"{area:.4f}")