t=int(input())
option_price=[]
for i in range(t):
    price=int(input())
    option=int(input())
    for j in range(option):
        q,p=map(int,input().split())
        option_price.append(q*p)
    print(sum(option_price)+price)
    option_price=[]