result=[]
sum=0
while True:
    a,b=map(int,input().split())
    result.append(a+b)
    sum+=1
    if a == 0 and b==0:
        break
for i in range(0,sum-1):
    print(result[i])