h,m=map(int,input().split())
bef_m = h*60+m-45
a=bef_m//60
b=bef_m%60
if a<0:
    a = a+24
    
print(a,b)