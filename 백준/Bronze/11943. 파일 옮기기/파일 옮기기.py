a1,o1=map(int,input().split())
a2,o2=map(int,input().split())
if a1+o2>a2+o1:
    print(a2+o1)
else:
    print(a1+o2)