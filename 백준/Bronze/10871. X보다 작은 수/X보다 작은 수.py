#x보다 작은 수
n,x=map(int,input().split())
min=[]
num=list(map(int,input().split()))
for i in range(0,n):
    if num[i] < x:
        min.append(num[i])
for i in range(0,len(min)):
    print(min[i],end=" ")
