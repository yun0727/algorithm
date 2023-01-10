#주사위 세개
a,b,c=map(int,input().split())
pr=0
if a==b==c:
    pr=10000+(a*1000)
elif a==b:
    pr=1000+a*100
elif c==b:
    pr=1000+b*100
elif a==c:
    pr=1000+a*100
elif a>b and a>c:
    pr=a*100
elif b>a and b>c:
    pr=b*100
elif c>a and c>b:
    pr=c*100
print(pr)