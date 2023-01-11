#검증수
num=list(map(int,input().split()))
for i in range(5):
    num[i]=num[i]**2
result=(sum(num))%10
print(result)