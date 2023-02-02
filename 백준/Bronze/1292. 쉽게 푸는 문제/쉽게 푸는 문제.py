a,b=map(int,input().split())
num=[]
for i in range(1,b+1):
    for j in range(1,i+1):
        num.append(i)
    if len(num)>b:
        break
sum=0
for i in range(a-1,b):
    sum+=num[i]
print(sum)