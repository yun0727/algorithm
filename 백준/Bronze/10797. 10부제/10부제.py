d=int(input())
car=list(map(int,input().split()))
sum=0
for i in range(5):
    if d == car[i]:
        sum+=1
print(sum)