A, B, C = map(float, input().split())
A_triangulo = A*C/2
A_circulo = 3.14159*C**2
A_trapezio = (A+B)*C/2
A_quadrado = B**2
A_retangulo = A*B
print(f"TRIANGULO: {A_triangulo:.3f}\nCIRCULO: {A_circulo:.3f}\nTRAPEZIO: {A_trapezio:.3f}\nQUADRADO: {A_quadrado:.3f}\nRETANGULO: {A_retangulo:.3f}")