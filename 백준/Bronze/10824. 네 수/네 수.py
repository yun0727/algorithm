a,b,c,d=map(int,input().split())
lenb=len(str(b))
ab=a*(10**lenb)+b
lend=len(str(d))
cd=c*(10**lend)+d
print(ab+cd)