N = int(input())
T_horas = N//3600
T_minutos = (N%3600)//60
T_segundos = N%3600%60
print(f"{T_horas}:{T_minutos}:{T_segundos}")