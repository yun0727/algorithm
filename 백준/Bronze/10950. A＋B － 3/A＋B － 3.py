#A+B-3
T=int(input())
a=[]
for i in range(0,T):
    A,B = map(int, input().split())
    a.append(A+B)

for i in range(T):
    print(a[i])

