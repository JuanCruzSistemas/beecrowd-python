number = int(input())
billetes = [100, 50, 20, 10, 5, 2, 1]

print(number)
for b in billetes:
    cantidad_billetes = number // b
    number -= cantidad_billetes * b
    print(f'{cantidad_billetes} nota(s) de R$ {b},00')