n,m=map(int,(input().split()))
num=[0]*n
for _ in range(m):
    i,j,k=map(int,(input().split()))
    for x in range(i,j+1):
        num[x-1] = k
for i in range(n):
    print(num[i],end=" ")