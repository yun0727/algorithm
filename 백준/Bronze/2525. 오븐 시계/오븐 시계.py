#오븐 시계
h,m=map(int,input().split())
t=int(input())
result_m = m+t
if result_m>=60:
    h=h+result_m//60
    if h>=24:
        h=h-24
    result_m= result_m%60
print(h,result_m)