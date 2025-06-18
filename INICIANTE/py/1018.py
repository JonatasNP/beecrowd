valor = int(input())
notas100 = valor//100
notas50 = (valor%100)//50
notas20 = (valor%100%50)//20
notas10 = (valor%100%50%20)//10
notas5 = (valor%100%50%20%10)//5
notas2 = (valor%100%50%20%10%5)//2
notas1 = valor%100%50%20%10%5%2
print(f"{valor}\n{notas100} nota(s) de R$ 100,00\n{notas50} nota(s) de R$ 50,00\n{notas20} nota(s) de R$ 20,00\n{notas10} nota(s) de R$ 10,00\n{notas5} nota(s) de R$ 5,00\n{notas2} nota(s) de R$ 2,00\n{notas1} nota(s) de R$ 1,00")