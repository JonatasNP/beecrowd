n = int(input())
numeros = ["one", "two", "three"]

for i in range(n):
    palavra = input()

    for numero in numeros:
        if len(palavra) != len(numero):
            continue

        erros = 0
        for j in range(len(palavra)):
            if palavra[j] != numero[j]:
                erros += 1
            if erros > 1:
                break

        if erros <= 1:
            if numero == "one":
                print(1)
            elif numero == "two":
                print(2)
            elif numero == "three":
                print(3)
            break