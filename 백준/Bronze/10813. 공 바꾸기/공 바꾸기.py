n,m=map(int,(input().split()))
num=[0]*(n+1)
for i in range(n+1):
    num[i] = i
tmp=0
for _ in range(m):
    i,j=map(int,input().split())
    tmp=num[i]
    num[i] =num[j] 
    num[j]=tmp
for i in range(1,n+1):
    print(num[i],end=" ")