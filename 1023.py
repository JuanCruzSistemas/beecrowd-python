import sys
input = sys.stdin.readline

num_ciudad = 0

while True:
    N = int(input())
    if N == 0: break
    
    num_ciudad += 1
    
    grupos: dict[int, int] = {}
    suma_consumo = 0
    suma_residentes = 0
    
    for i in range(N):
        residentes, consumo = map(int, input().split())
        tasa = consumo // residentes
        grupos[tasa] = grupos.get(tasa, 0) + residentes
        
        suma_consumo += consumo
        suma_residentes += residentes
    
    if num_ciudad > 1: print()
    
    print(f'Cidade# {num_ciudad}:')
    salida = [f'{residentes}-{tasa}' for tasa, residentes in sorted(grupos.items())]
    print(' '.join(salida))
    centesimas = (suma_consumo * 100) // suma_residentes
    print(f'Consumo medio: {centesimas // 100}.{centesimas % 100:02d} m3.')