n,k=map(int,input().split())
number=[]
for i in range(1,n+1):
    if n%i ==0:
        number.append(i)
if  k > len(number):
    print(0)
else:
    print(number[k-1])