from sys import stdin
from math import gcd
input = stdin.readline

N = int(input())

for _ in range(N):
    print(gcd(*map(int, input().split())))