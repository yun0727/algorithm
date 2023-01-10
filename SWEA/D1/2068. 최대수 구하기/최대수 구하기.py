#최대수 구하기
t=int(input())
m=[]
for i in range(t):
    num=list(map(int,input().split()))
    m.append(max(num))
for i in range(t):
    print(f"#{i+1} {m[i]}")