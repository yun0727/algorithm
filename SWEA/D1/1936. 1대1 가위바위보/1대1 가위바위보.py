#일대일 가위바위보
a=list(map(int,input().split()))
if a[0]==1:
    if a[1]==2:
        print("B")
    elif a[1]==3:
        print("A")
elif a[0]==2:
    if a[1]==1:
        print("A")
    elif a[1]==3:
        print("B")
elif a[0]==3:
    if a[1]==1:
        print("B")
    if a[1]==2:
        print("A")