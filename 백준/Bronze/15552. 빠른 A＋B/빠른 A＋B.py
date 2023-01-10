#빠른 A+B
import sys
n=int(input())
sum=[]
for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    sum.append(a+b)
for i in range(n):
    print(sum[i])