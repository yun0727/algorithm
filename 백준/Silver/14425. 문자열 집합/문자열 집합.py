import sys
input=sys.stdin.readline
n, m=map(int,input().split())
s=set()
for _ in range(n):
    s.add(input())
sum=0
for _ in range(m):
    if input() in s:
        sum+=1

print(sum)