# N = int(input())

# minutos = N // 60
# segundos = N - minutos * 60
# horas = minutos // 60
# minutos -= horas * 60

# print(f'{horas}:{minutos}:{segundos}')

N = int(input())

horas = N // 3600
N -= horas * 3600
minutos = N // 60
N -= minutos * 60

print(f'{horas}:{minutos}:{N}')