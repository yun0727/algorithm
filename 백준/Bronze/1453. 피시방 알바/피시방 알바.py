n=int(input())
num=list(map(int,input().split()))
sum=0
for i in range(101):
    if num.count(i) >1:
        sum+=(num.count(i)-1)
print(sum)