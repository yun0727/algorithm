import sys
input=sys.stdin.readline
n,m=map(int,input().split())
num=list(map(int,input().split()))
result=[0]
temp=0
for i in num:
    temp+=i
    result.append(temp)
for i in range(m):
    a,b=map(int,input().split())
    print(result[b]-result[a-1])