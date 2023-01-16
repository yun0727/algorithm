n=int(input())
#a=창영 b=상덕
A=100
B=100
for i in range(n):
    a,b=map(int,input().split())
    if a>b:
        B=B-a
        A=A
    elif a<b:
        A=A-b
        B=B
    else:
        A=A
        B=B
print(A)
print(B)