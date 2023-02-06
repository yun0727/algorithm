A,B=map(int,input().split())
a=min(A,B)
b=max(A,B)
tmp=b-a-1
if tmp<=0:
    print(0)
else:
    print(tmp)
    for i in range(a+1,b):
        print(i,end=" ")