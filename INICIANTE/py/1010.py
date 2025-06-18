linha1, linha2 = input().split(), input().split()
c1, n1, v1 = int(linha1[0]), int(linha1[1]), float(linha1[2])
c2, n2, v2 = int(linha2[0]), int(linha2[1]), float(linha2[2])
valorFinal = n1*v1 + n2*v2
print(f"VALOR A PAGAR: R$ {valorFinal:.2f}")