nome, salarioFixo, totalVendas = str(input()), float(input()), float(input())
salarioComBonus = salarioFixo + 0.15*totalVendas
print(f"TOTAL = R$ {salarioComBonus:.2f}")