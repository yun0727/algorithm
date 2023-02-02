n=int(input())
num=[1,2,3]
for i in range(n):
    a,b=map(int,input().split())
    c=num[a-1]
    d=num[b-1]
    num[a-1]=d
    num[b-1]=c
print(num.index(1)+1)