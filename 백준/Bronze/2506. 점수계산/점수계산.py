n=int(input())
ans=[]
ans=list(map(int,input().split()))
sum=0
point=0
for i in range(n):
    if ans[i] == 1:
        point=point+1
        sum=sum+point
    else:
        sum+=0
        point=0
print(sum)
        