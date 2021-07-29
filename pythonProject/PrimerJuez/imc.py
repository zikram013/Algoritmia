peso, altura = map(int, input().strip().split())
altura = altura / 100
imc = peso / altura ** 2
print(f"{imc:.2f}")
