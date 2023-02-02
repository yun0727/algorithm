n=int(input())
num=list(map(int,input().split()))
result=[]
for i in range(n-1):
    result.append(num[i+1]-num[i])
for i in range(1,len(result)):
    if result[i]>0 and result[i-1]>0:
        result[i]=result[i]+result[i-1]
        result[i-1]=0
if max(result)>0:
    print(max(result))
else:
    print(0)