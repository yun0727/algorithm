#평균
n=int(input())
num=list(map(int,input().split()))
m=max(num)
sco=[]
for i in range(n):
    sco.append((num[i]/m)*100)
print(sum(sco)/n)