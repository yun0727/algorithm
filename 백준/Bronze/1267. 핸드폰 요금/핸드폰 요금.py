n=int(input())
time=list(map(int,(input().split())))
y=0
m=0
for i in range(n):
    y+=((time[i]//30)+1)*10
    m+=((time[i]//60)+1)*15
if y>m:
    print("M",m)
elif y<m:
    print("Y",y)
elif y==m:
    print("Y M",y)