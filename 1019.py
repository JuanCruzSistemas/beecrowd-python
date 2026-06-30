N = int(input())

minutos = N // 60
segundos = N - minutos * 60
horas = minutos // 60
minutos -= horas * 60

print(f'{horas}:{minutos}:{segundos}')