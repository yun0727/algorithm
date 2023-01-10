#더하기 사이클
n=int(input()) 
m=n
sum=0
while True:
    a=m//10 
    b=m%10 
    c=(a+b)%10
    m=(b*10)+c
    sum += 1
    if m == n:
        break
print(sum)