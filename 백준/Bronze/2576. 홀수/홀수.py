a1=int(input())
a2=int(input())
a3=int(input())
a4=int(input())
a5=int(input())
a6=int(input())
a7=int(input())
num=[a1,a2,a3,a4,a5,a6,a7]
osum=[]
for i in range(7):
    if num[i]%2==1:
        osum.append(num[i])
if len(osum) != 0:
    print(sum(osum))
    print(min(osum))
else:
    print(-1)