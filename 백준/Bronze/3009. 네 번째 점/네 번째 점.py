x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
x=[x1,x2,x3]
y=[y1,y2,y3]
if x.count(x1) == 2:
    x.remove(x1)
    x.remove(x1)
elif x.count(x2) == 2:
    x.remove(x2)
    x.remove(x2)
elif x.count(x3) == 2:
    x.remove(x3)
    x.remove(x3)
if y.count(y1) == 2:
    y.remove(y1)
    y.remove(y1)
elif y.count(y2) == 2:
    y.remove(y2)
    y.remove(y2)
elif y.count(y3) == 2:
    y.remove(y3)
    y.remove(y3)
print(x[0],y[0])