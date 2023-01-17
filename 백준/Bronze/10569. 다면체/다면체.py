t=int(input())
result=[]
for i in range(t):
    v,e=map(int,input().split())
    result.append(2-v+e)
for i in range(t):
    print(result[i])