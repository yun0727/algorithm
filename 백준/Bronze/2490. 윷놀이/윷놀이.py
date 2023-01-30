for i in range(3):
    try1=list(map(int,input().split()))
    if sum(try1) == 4:
        print("E")
    elif sum(try1) == 3:
        print("A")
    elif sum(try1) == 2:
        print("B") 
    elif sum(try1) == 1:
        print("C") 
    elif sum(try1) == 0:
        print("D")  