while True:
    X = int(input())
    
    for i in range(1, X+1):
        if i == X:
            print(i)
        else:
            print(i, end = " ")
        
    if X == 0:
        break