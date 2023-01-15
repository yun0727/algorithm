t=int(input())
# a=300 b=60 c=10
if t%10 != 0:
    print(-1)
else:
    a=t//300 #1
    b=(t%300)//60 #70
    c=(t-a*300-b*60)//10
    print(a,b,c)