import sys
input=sys.stdin.readline
n=int(input())
num=[]
for i in range(n):
    num.append(int(input()))
print((sum(num))-(len(num)-1))  