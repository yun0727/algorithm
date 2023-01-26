n=int(input())
qu=list(range(1,n+1))
while len(qu)>1:
    print(qu.pop(0),end=" ")
    qu.append(qu.pop(0))
print(qu[0])