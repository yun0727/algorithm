#A+B-8
n=int(input())
sum=[]
c=[]
d=[]
for i in range(n):
    a,b=map(int,input().split())
    sum.append(a+b)
    c.append(a)
    d.append(b)
for i in range(n):
    print(f"Case #{i+1}: {c[i]} + {d[i]} = {sum[i]}")