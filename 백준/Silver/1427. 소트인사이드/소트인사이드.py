n=list(map(int,input()))
result=[]
while len(n)>1:
    temp=max(n)
    result.append(temp)
    n.remove(temp)
result.append(n[0])
for i in result:
    print(i, end="")