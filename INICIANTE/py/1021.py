notas = [100, 50, 20, 10, 5, 2]
moedas = [100, 50, 25, 10, 5, 1]
valor = float(input())

print("NOTAS:")
for nota in notas:
    quantNotas = int(valor//nota)
    valor -= int(quantNotas*nota)
    print(f"{quantNotas} nota(s) de R$ {nota:.2f}")

valor *= 100
print("MOEDAS:")
for moeda in moedas:
    quantMoedas = int(valor//moeda)
    valor = valor%moeda
    print(f"{quantMoedas} moeda(s) de R$ {moeda/100:.2f}")