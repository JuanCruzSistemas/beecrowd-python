def distance(x1: float, x2: float, y1: float, y2: float) -> float:
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

x1, y1 = map(float, input().split(' '))
x2, y2 = map(float, input().split(' '))

print(f'{distance(x1, x2, y1, y2):.4f}')