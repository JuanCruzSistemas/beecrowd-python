import sys
from bisect import bisect_left

input = sys.stdin.readline
k = 0

while True:
    N, Q = map(int, input().split())
    
    if N == 0 and Q == 0:
        break
    
    k += 1
    
    canicas = sorted(int(input()) for _ in range(N))
    
    print(f'CASE# {k}:')
    for _ in range(Q):
        consulta = int(input())
        indice = bisect_left(canicas, consulta)
        
        if indice < len(canicas) and canicas[indice] == consulta:
            print(f'{consulta} found at {indice + 1}')
        else:
            print(f'{consulta} not found')