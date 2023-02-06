num=[]
for i in range(21):
    num.append(i)
for i in range(10):
    a,b=map(int,input().split())
    if a<=20 and b<=20:
        change=[]
        for j in range(a,b+1):
            change.append(num[j])
        for k in range(a,b+1):
            num[k]=change[a-k-1]
for i in range(1,21):
    print(num[i],end=" ")