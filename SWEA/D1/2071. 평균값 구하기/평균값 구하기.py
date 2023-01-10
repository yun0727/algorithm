# 평균값 구하기
t= int(input())
avg=[]
for i in range(t):
    num=list(map(int,input().split()))
    avg.append(round(sum(num)/10))
for i in range(t):
    print(f"#{i+1} {avg[i]}")