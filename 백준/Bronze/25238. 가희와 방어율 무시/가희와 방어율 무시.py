a,b=map(int,input().split())
#a방어율 수치 b 유저의 방무
if (a-a*b*0.01) >= 100:
    print(0)
else:
    print(1)