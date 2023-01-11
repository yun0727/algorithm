c=int(input())
num=[]
sc=[]
re=[]
for i in range(c):
    num=list(map(int,input().split()))
    sc.append(num)
for i in range(c):
    avg=(sum(sc[i])-sc[i][0])/sc[i][0]
    plus=0
    for j in range(0,len(sc[i])-1):
        if avg<sc[i][j+1]:
            plus+=1
    re.append(round(plus/sc[i][0]*100,3))
for i in range(c):
    print("{0:0.3f}%".format(re[i]))
    