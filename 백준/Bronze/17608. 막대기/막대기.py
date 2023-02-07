import sys
input=sys.stdin.readline
n=int(input())
num=[]
sum=1
for i in range(n):
    num.append(int(input()))
a=num[0]
for _ in range(n-1):
    if num[-1]>=num[-2]:
        num.pop(-2)
    else:
        sum+=1
        num.pop(-1)
# if num[0] == a:
#     sum+=1
print(sum)