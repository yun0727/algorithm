n=int(input())
hansu=0
for n in range(1,n+1):
    if n <=99:
        hansu+=1
    else:
        n=list(map(int,str(n)))
        if n[0]-n[1] == n[1]-n[2]:
            hansu+=1
print(hansu)