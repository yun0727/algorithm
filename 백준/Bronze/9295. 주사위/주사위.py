t=int(input())
sum=[]
for i in range(t):
    a,b=map(int,input().split())
    sum.append(a+b)
for i in range(t):
    print(f"Case {(i+1)}: {sum[i]}")