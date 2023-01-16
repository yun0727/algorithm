#A+B-7
n=int(input())
sum=[]
for i in range(n):
    a,b=map(int,input().split())
    sum.append(a+b)
for i in range(n):
    print(f"Case #{i+1}: {sum[i]}")