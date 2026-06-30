# xf = xi + v*t
# t = (xf - xi) / v

# Xfx = 60*t
# Xfy = 90*t
# Xfy - Xfx = distancia
# 90*t - 60*t = distancia
# 30*t = distancia
# t = distancia / 30

DISTANCIA = int(input())
TIEMPO = (DISTANCIA / 30) * 60

print(f'{int(TIEMPO)} minutos')