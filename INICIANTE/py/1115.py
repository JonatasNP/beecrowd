while True:
    A, B = map(int, input().split())
    
    if A > 0 and B > 0:
        print("primeiro")
    elif A < 0 and B > 0:
        print("segundo")
    elif A < 0 and B < 0:
        print("terceiro")
    elif A > 0 and B < 0:
        print("quarto")
    else:
        break