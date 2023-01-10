#몫과 나머지 출력하기
n=int(input())
c=[]
d=[]
for i in range(1, n+1):
    a,b=map(int,input().split())
    c.append(a//b)
    d.append(a%b)
for i in range(0,n):    
    print(f"#{i+1} {c[i]} {d[i]}")