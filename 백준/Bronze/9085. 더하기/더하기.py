t=int(input())
num=[]
result=[]
for i in range(t):
    n=int(input())
    num=map(int,input().split())
    result.append(sum(num))
for i in range(t):
    print(result[i])