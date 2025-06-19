X, Y = map(int, input().split())
i = 1

while i < Y:
    nums = []
    for j in range(X):
        nums.append(i)
        i+=1

    for num in nums:
        print(num, end=' ')
        
    print()