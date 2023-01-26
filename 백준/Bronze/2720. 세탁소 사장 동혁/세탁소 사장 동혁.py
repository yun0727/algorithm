t=int(input())
for i in range(t):
    money=int(input())
    q=money//25
    d=(money%25)//10
    n=((money%25)%10)//5
    p=((money%25)%10)%5
    print(q,d,n,p,end=" ")
    print("")