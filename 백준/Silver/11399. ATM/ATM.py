n=int(input())
p=list(map(int,input().split()))
num=[]
p.sort()
sum=0
for i in range(n):
    sum+=p[i]*(n-i)
print(sum)