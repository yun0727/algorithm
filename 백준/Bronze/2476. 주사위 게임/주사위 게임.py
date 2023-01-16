n=int(input())
result=[]
for i in range(n):
    num=list(map(int,input().split()))
    pr=0
    if num[0]==num[1]==num[2]:
        pr=10000+(num[0]*1000)
    elif num[0]==num[1]:
        pr=1000+num[0]*100
    elif num[2]==num[1]:
        pr=1000+num[1]*100
    elif num[0]==num[2]:
        pr=1000+num[0]*100
    elif num[0]>num[1] and num[0]>num[2]:
        pr=num[0]*100
    elif num[1]>num[0] and num[1]>num[2]:
        pr=num[1]*100
    elif num[2]>num[0] and num[2]>num[1]:
        pr=num[2]*100
    result.append(pr)
print(max(result))