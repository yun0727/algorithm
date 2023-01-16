#영수증
pr=int(input())
n=int(input())
sum=0
for i in range(n):
    a,b=map(int,input().split())
    sum += a*b
if sum == pr:
    print("Yes")
else:
    print("No")