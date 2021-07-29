precio, mes = map(int, input().strip().split())
total = int
if mes == 2:
    total = precio * 28
elif mes == 7 or mes == 8 or mes == 12 or mes == 10:
    total = precio * 31
elif mes % 2 == 0 or mes == 9 or mes == 11:
    total = precio * 30
else:
    total = precio * 31
print(int(total))
