n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
result=[]
for i in range(n):
    result.append(a[i])
for i in range(m):
    result.append(b[i])
result.sort()
for i in result:
    print(i,end=" ")