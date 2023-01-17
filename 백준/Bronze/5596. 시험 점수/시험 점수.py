c1,m1,s1,e1=map(int,input().split())
c2,m2,s2,e2=map(int,input().split())
sum1=c1+m1+s1+e1
sum2=c2+m2+s2+e2
if sum1>=sum2:
    print(sum1)
else:
    print(sum2)