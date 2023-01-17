a,b=map(int,input().split())
numa=set()
numb=set()
ab=[]
for i in range(1,a+1):
    if a%i==0:
        numa.add(i)
for j in range(1,b+1):
    if b%j==0:
        numb.add(j)
ab=list(numa&numb)
lg=max(ab)
sm=lg*(a//lg)*(b//lg)
print(lg)
print(sm)