a, b = map(int, input().split())
r = int(a % abs(b))
q = int((a - r)//b)
print(q, r)