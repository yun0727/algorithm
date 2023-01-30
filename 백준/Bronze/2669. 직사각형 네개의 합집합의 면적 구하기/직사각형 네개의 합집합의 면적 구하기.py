a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
d=list(map(int,input().split()))
square=set()
for x in range(a[0]+1,a[2]+1):
    for y in range(a[1]+1,a[3]+1):
        square.add(str(x)+str(y))
for x in range(b[0]+1,b[2]+1):
    for y in range(b[1]+1,b[3]+1):
        square.add(str(x)+str(y))
for x in range(c[0]+1,c[2]+1):
    for y in range(c[1]+1,c[3]+1):
        square.add(str(x)+str(y))
for x in range(d[0]+1,d[2]+1):
    for y in range(d[1]+1,d[3]+1):
        square.add(str(x)+str(y))
print(len(square))