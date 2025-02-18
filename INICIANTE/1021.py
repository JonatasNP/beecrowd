def notas_moedas(valor):
    notas = [100, 50, 20, 10, 5, 2]
    moedas = [100, 50, 25, 10, 5, 1]

    valor_centavos = int(round(valor * 100))

    print("NOTAS:")
    for nota in notas:
        qtd_notas = valor_centavos // (nota * 100)
        print(f"{qtd_notas} nota(s) de R$ {nota:.2f}")
        valor_centavos -= qtd_notas * (nota * 100)

    print("MOEDAS:")
    for moeda in moedas:
        qtd_moedas = valor_centavos // moeda
        print(f"{qtd_moedas} moeda(s) de R$ {moeda / 100:.2f}")
        valor_centavos -= qtd_moedas * moeda

N = float(input())
notas_moedas(N)