EDAD = int(input())

anios = EDAD // 365
EDAD -= anios * 365
meses = EDAD // 30
EDAD -= meses * 30

print(f'{anios} ano(s)\n{meses} mes(es)\n{EDAD} dia(s)')