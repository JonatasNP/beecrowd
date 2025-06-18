D = int(input())
anos, meses, dias = D//365, (D%365)//30, D%365%30
print(f"{anos} ano(s)\n{meses} mes(es)\n{dias} dia(s)")