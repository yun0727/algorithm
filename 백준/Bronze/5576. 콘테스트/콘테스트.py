w=[]
k=[]
for i in range(10):
    w.append(int(input()))
for i in range(10):
    k.append(int(input()))
w.sort()
k.sort()
print(w[-1]+w[-2]+w[-3],k[-1]+k[-2]+k[-3])